"""Generate Models for ThreatConnect V3 API"""
# standard library
import os
from enum import Enum
from pathlib import Path

# third-party
import typer

# first-party
from tcex.api.tc.v3._gen._gen_args_abc import GenerateArgsABC
from tcex.api.tc.v3._gen._gen_filter_abc import GenerateFilterABC
from tcex.api.tc.v3._gen._gen_model_abc import GenerateModelABC
from tcex.api.tc.v3._gen._gen_object_abc import GenerateObjectABC
from tcex.api.tc.v3.api_endpoints import ApiEndpoints
from tcex.utils import Utils

# initialize Utils module
utils = Utils()


class GenerateArgs(GenerateArgsABC):
    """Generate Models for TC API Types"""


class GenerateFilter(GenerateFilterABC):
    """Generate Models for TC API Types"""

    def __init__(self, type_: str) -> None:
        """Initialize class properties."""
        super().__init__(type_)

        # properties
        _api_endpoint = getattr(ApiEndpoints, type_.upper()).value
        self.api_url = f'{self._api_server}{_api_endpoint}'


class GenerateModel(GenerateModelABC):
    """Generate Models for TC API Types"""

    def __init__(self, type_: str) -> None:
        """Initialize class properties."""
        super().__init__(type_)

        # properties
        _api_endpoint = getattr(ApiEndpoints, type_.upper()).value
        self.api_url = f'{self._api_server}{_api_endpoint}'


class GenerateObject(GenerateObjectABC):
    """Generate Models for TC API Types"""

    def __init__(self, type_: str) -> None:
        """Initialize class properties."""
        super().__init__(type_)

        # properties
        _api_endpoint = getattr(ApiEndpoints, type_.upper()).value
        self.api_url = f'{self._api_server}{_api_endpoint}'


def gen_args(type_: str, indent_blocks: int) -> None:
    """Generate args code."""
    # get instance of doc generator
    gen = GenerateArgs(type_)

    # run model code first so that requirements can be determined
    i1 = ' ' * (4 * indent_blocks)
    i2 = i1 + ' ' * 4
    print(gen.gen_args(i1=i1, i2=i2))


def gen_filter(type_: str) -> None:
    """Generate the filter code."""
    # get instance of filter generator
    gen = GenerateFilter(type_)

    # set the output filename using the appropriate tcex api path
    out_path = gen.tap(type_).split('.') + [type_, f'{type_.singular()}_filter.py']
    out_file = Path(os.path.join(*out_path))

    if not out_file.is_file():
        typer.secho(f'\nCould not find file {out_file}.', fg=typer.colors.RED)
        typer.Exit(code=1)

    # generate class methods first so requirements can be updated
    class_methods = gen.gen_class_methods()

    with out_file.open(mode='w') as fh:
        fh.write(gen.gen_doc_string())
        fh.write(gen.gen_requirements())
        fh.write(gen.gen_class())
        fh.write(class_methods)
        fh.write('')  # newline at the end of the file

    typer.secho(f'Successfully wrote {out_file}.', fg=typer.colors.GREEN)


def gen_model(type_: str) -> None:
    """Generate model code."""
    # get instance of model generator
    gen = GenerateModel(type_)

    # set the output filename using the appropriate tcex api path
    out_path = gen.tap(type_).split('.') + [type_, f'{type_.singular()}_model.py']
    out_file = Path(os.path.join(*out_path))

    if not out_file.is_file():
        typer.secho(f'\nCould not find file {out_file}.', fg=typer.colors.RED)
        typer.Exit(code=1)

    # generate model fields code first so that requirements can be determined
    model_fields = gen.gen_model_fields()

    gen.gen_doc_string()
    gen.gen_requirements()
    gen.gen_container_class()
    gen.gen_container_fields()
    gen.gen_data_class()
    gen.gen_data_fields()
    gen.gen_model_class()
    gen.gen_validator_methods()
    gen.gen_requirements_first_party_forward_reference()
    gen.gen_forward_reference()

    with out_file.open(mode='w') as fh:
        fh.write(gen.gen_doc_string())
        fh.write(gen.gen_requirements())
        # add container model
        fh.write(gen.gen_container_class())
        fh.write(gen.gen_container_fields())
        # add data model
        fh.write(gen.gen_data_class())
        fh.write(gen.gen_data_fields())
        # add data model
        fh.write(gen.gen_model_class())
        fh.write(model_fields)
        # add validators
        fh.write(gen.gen_validator_methods())
        # add forward reference requirements
        fh.write(gen.gen_requirements_first_party_forward_reference())
        # add forward references
        fh.write(gen.gen_forward_reference())
        # fh.write('')  # newline at the end of the file

    typer.secho(f'Successfully wrote {out_file}.', fg=typer.colors.GREEN)


def gen_object(type_: str) -> None:
    """Generate object code."""
    # get instance of filter generator
    gen = GenerateObject(type_)

    # set the output filename using the appropriate tcex api path
    out_path = gen.tap(type_).split('.') + [type_, f'{type_.singular()}.py']
    out_file = Path(os.path.join(*out_path))

    if not out_file.is_file():
        typer.secho(f'\nCould not find file {out_file}.', fg=typer.colors.RED)
        typer.Exit(code=1)

    # generate class method code first so that requirements can be determined
    container_methods = gen.gen_container_methods()
    object_methods = gen.gen_object_methods()

    with out_file.open(mode='w') as fh:
        fh.write(gen.gen_doc_string())
        fh.write(gen.gen_requirements())
        fh.write(gen.gen_container_class())
        fh.write(container_methods)
        fh.write(gen.gen_object_class())
        fh.write(object_methods)
        # fh.write('')  # newline at the end of the file

    typer.secho(f'Successfully wrote {out_file}.', fg=typer.colors.GREEN)


#
# CLI
#


class ObjectTypes(str, Enum):
    """Object Types"""

    adversary_assets = 'adversary_assets'
    artifacts = 'artifacts'
    artifact_types = 'artifact_types'
    cases = 'cases'
    # case_attributes = 'case_attributes'
    # group_attributes = 'group_attributes'
    groups = 'groups'
    # indicator_attributes = 'indicator_attributes'
    indicators = 'indicators'
    notes = 'notes'
    owners = 'owners'
    owner_roles = 'owner_roles'
    security_labels = 'security_labels'
    system_roles = 'system_roles'
    tags = 'tags'
    tasks = 'tasks'
    users = 'users'
    user_groups = 'user_groups'
    victims = 'victims'
    victim_assets = 'victim_assets'
    workflow_events = 'workflow_events'
    workflow_templates = 'workflow_templates'


class GenTypes(str, Enum):
    """Object Types"""

    all = 'all'
    filter = 'filter'
    model = 'model'
    object = 'object'


app = typer.Typer()


@app.command()
def all(  # pylint: disable=redefined-builtin
    gen_type: GenTypes = typer.Option(
        'all', '--gen_type', help='Generate filter, model, or object file.'
    ),
):
    """Generate Args."""
    gen_type = gen_type.value.lower()
    for type_ in ObjectTypes:
        type_ = utils.snake_string(type_.value)

        if gen_type in ['all', 'filter']:
            gen_filter(type_)
        if gen_type in ['all', 'model']:
            gen_model(type_)
        if gen_type in ['all', 'object']:
            gen_object(type_)


@app.command()
def args(
    type_: ObjectTypes = typer.Option(
        ..., '--type', help='Generate Args for the provided object type.'
    ),
    indent_blocks: int = typer.Option(
        1, help='The number of four space blocks to indent the args.'
    ),
):
    """Generate Args."""
    type_ = utils.snake_string(type_.value)
    gen_args(type_, indent_blocks)


@app.command()
def code(
    type_: ObjectTypes = typer.Option(
        ..., '--type', help='Generate filter, model, and object files for the provided type.'
    ),
):
    """Generate Args."""
    type_ = utils.snake_string(type_.value)
    gen_filter(type_)
    gen_model(type_)
    gen_object(type_)


@app.command()
def filter(  # pylint: disable=redefined-builtin
    type_: ObjectTypes = typer.Option(
        ..., '--type', help='Generate filter object file for the provided type.'
    ),
):
    """Generate the filter code."""
    type_ = utils.snake_string(type_.value)
    gen_filter(type_)


@app.command()
def model(
    type_: ObjectTypes = typer.Option(
        ..., '--type', help='Generate model file for the provided type.'
    ),
):
    """Generate the model"""
    type_ = utils.snake_string(type_.value)
    gen_model(type_)


@app.command()
def object(  # pylint: disable=redefined-builtin
    type_: ObjectTypes = typer.Option(
        ..., '--type', help='Generate object file for the provided type.'
    ),
):
    """Generate the filter class"""
    type_ = utils.snake_string(type_.value)
    gen_object(type_)


if __name__ == '__main__':
    app()