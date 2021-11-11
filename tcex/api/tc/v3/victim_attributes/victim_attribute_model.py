"""Victim_Attribute / Victim_Attributes Model"""
# pylint: disable=no-member,no-self-argument,no-self-use,wrong-import-position
# standard library
from datetime import datetime
from typing import List, Optional

# third-party
from pydantic import BaseModel, Extra, Field, validator

# first-party
from tcex.api.tc.v3.v3_model_abc import V3ModelABC
from tcex.utils import Utils

# json-encoder
json_encoders = {datetime: lambda v: v.isoformat()}


class VictimAttributesModel(
    BaseModel,
    title='VictimAttributes Model',
    alias_generator=Utils().snake_to_camel,
    validate_assignment=True,
):
    """Victim_Attributes Model"""

    data: Optional[List['VictimAttributeModel']] = Field(
        [],
        description='The data for the VictimAttributes.',
        methods=['POST', 'PUT'],
        title='data',
    )


class VictimAttributeDataModel(
    BaseModel,
    title='VictimAttribute Data Model',
    alias_generator=Utils().snake_to_camel,
    validate_assignment=True,
):
    """Victim_Attributes Data Model"""

    data: Optional[List['VictimAttributeModel']] = Field(
        [],
        description='The data for the VictimAttributes.',
        methods=['POST', 'PUT'],
        title='data',
    )


class VictimAttributeModel(
    V3ModelABC,
    alias_generator=Utils().snake_to_camel,
    extra=Extra.allow,
    title='VictimAttribute Model',
    validate_assignment=True,
    json_encoders=json_encoders,
):
    """Victim_Attribute Model"""

    created_by: Optional['UserModel'] = Field(
        None,
        allow_mutation=False,
        description='The **created by** for the Victim_Attribute.',
        read_only=True,
        title='createdBy',
    )
    date_added: Optional[datetime] = Field(
        None,
        allow_mutation=False,
        description='The date and time that the Attribute was first created.',
        read_only=True,
        title='dateAdded',
    )
    default: bool = Field(
        None,
        description=(
            'A flag indicating that this is the default attribute of its type within the object. '
            'Only applies to certain attribute and data types.'
        ),
        methods=['POST', 'PUT'],
        read_only=False,
        title='default',
    )
    id: Optional[int] = Field(
        None,
        description='The ID of the item.',
        read_only=True,
        title='id',
    )
    last_modified: Optional[datetime] = Field(
        None,
        allow_mutation=False,
        description='The date and time that the Attribute was last modified.',
        read_only=True,
        title='lastModified',
    )
    source: Optional[str] = Field(
        None,
        description='The attribute source.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='source',
    )
    type: Optional[str] = Field(
        None,
        description='The attribute type.',
        methods=['POST'],
        read_only=False,
        title='type',
        updatable=False,
    )
    value: Optional[str] = Field(
        None,
        description='Attribute value.',
        methods=['POST', 'PUT'],
        min_length=1,
        read_only=False,
        title='value',
    )
    victim_id: Optional[int] = Field(
        None,
        description='Victim associated with attribute.',
        methods=['POST'],
        read_only=False,
        title='victimId',
        updatable=False,
    )

    @validator('created_by', always=True)
    def _validate_created_by(cls, v):
        if not v:
            return UserModel()
        return v


# first-party
from tcex.api.tc.v3.security.users.user_model import UserModel

# add forward references
VictimAttributeDataModel.update_forward_refs()
VictimAttributeModel.update_forward_refs()
VictimAttributesModel.update_forward_refs()
