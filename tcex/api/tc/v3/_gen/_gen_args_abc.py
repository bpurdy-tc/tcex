"""Generate Docs for ThreatConnect API"""
# standard library
import importlib
import sys
from abc import ABC
from textwrap import TextWrapper
from typing import Any, Dict, Optional

# first-party
from tcex.api.tc.v3._gen._gen_abc import GenerateABC


class GenerateArgsABC(GenerateABC, ABC):
    """Generate docstring for Model."""

    def __init__(self, type_: Any) -> None:
        """Initialize class properties."""
        super().__init__(type_)
        self.type_ = self.utils.snake_string(self._type_map(type_))

    @staticmethod
    def _format_description(description: str, length: int, indent: str) -> str:
        """Format description for field."""
        # fix descriptions coming from core API endpoint
        if description[-1] not in ('.', '?', '!'):
            description += '.'

        # fix core descriptions that are not capitalized.
        description_words = description.split(' ')
        description = f'{description_words[0].title()} ' + ' '.join(description_words[1:])

        textwrapper = TextWrapper(
            subsequent_indent=indent,
            width=length,
            expand_tabs=True,
            tabsize=len(indent),
            break_long_words=False,
        )
        return '\n'.join(textwrapper.wrap(description))

    @staticmethod
    def _import_model(module, class_name) -> Any:
        """Import the appropriate model."""
        return getattr(importlib.import_module(module), class_name)

    def _prop_type(self, prop_data: dict) -> str:
        """Return the appropriate arg type."""
        prop_type = None
        if 'type' in prop_data:
            prop_type = self._prop_type_map(prop_data.get('type'))
        elif 'allOf' in prop_data and prop_data.get('allOf'):
            ref = prop_data.get('allOf')[0].get('$ref')
            prop_type = ref.split('/')[-1].replace('Model', '')
        elif 'items' in prop_data and prop_data.get('items'):
            ref = prop_data.get('items').get('$ref')
            prop_type = ref.split('/')[-1].replace('Model', '')
        return prop_type

    @staticmethod
    def _prop_type_map(prop_type: str) -> str:
        """Return hint type."""
        _prop_types = {
            'boolean': 'bool',
            'integer': 'int',
            'string': 'str',
        }
        return _prop_types.get(prop_type, prop_type)

    def gen_args(
        self,
        i1: Optional[str] = None,
        i2: Optional[str] = None,
        nested_objects: Optional[bool] = True,
        updatable: Optional[bool] = True,
    ) -> str:
        """Model Map"""
        i1 = i1 or self.i1
        i2 = i2 or self.i2

        module_data = self._module_data(self.type_)
        model = self._import_model(module_data.get('model_module'), module_data.get('model_class'))
        _doc_string = [f'{i1}Args:']

        # get properties from schema
        schema = model().schema(by_alias=False)
        if '$ref' in schema:
            model_name = schema.get('$ref').split('/')[-1]
            properties = schema.get('definitions').get(model_name).get('properties')
        elif 'properties' in schema:
            properties = schema.get('properties')
        else:
            print('WTH???')
            print(model().schema_json(by_alias=False))
            sys.exit()

        # iterate over properties to build docstring
        for arg, prop_data in properties.items():
            # for all doc string read-only args should not be included.
            if prop_data.get('read_only', False) is True:
                continue

            # for add_xxx method doc string non-updatable args should not be included.
            if updatable is False and prop_data.get('updatable', True) is False:
                continue

            # get arg type
            prop_type = self._prop_type(prop_data)

            # for add_xxx method doc string nested object args should not be included.
            # TODO: [low] there should be an easier way than maitaining the list of types here.
            if nested_objects is False and prop_type in [
                'AdversaryAssets',
                'Artifact',
                'Artifacts',
                'ArtifactType',
                'Assignee',
                'Attributes',
                'Case',
                'Cases',
                'FileAction',
                'FileOccurrences',
                'Groups',
                'Indicators',
                'Note',
                'Notes',
                'SecurityLabels',
                'Tag',
                'Tags',
                'Task',
                'Tasks',
                'User',
                'Users',
                'Victims',
                'VictimAssets',
                'WorkflowEvent',
                'WorkflowEvents',
                'WorkflowTemplate',
                None,
            ]:
                continue

            # arg
            _arg_doc = f'{i2}{arg} ({prop_type}, kwargs): '

            # description
            description = prop_data.get('description')
            d_indent = i2 + self.i1
            _arg_doc = self._format_description(
                description=f'{_arg_doc}{description}',
                length=100,
                indent=d_indent,
            )

            # add arg to doc string
            _doc_string.append(_arg_doc)

        if len(_doc_string) > 1:
            return '\n'.join(_doc_string)
        return ''
