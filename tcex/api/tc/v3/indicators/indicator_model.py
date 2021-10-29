"""Indicator / Indicators Model"""
# pylint: disable=no-member,no-self-argument,no-self-use,wrong-import-position
# standard library
from datetime import datetime
from typing import List, Optional

# third-party
from pydantic import BaseModel, Extra, Field, validator

# first-party
from tcex.utils import Utils


class IndicatorsModel(
    BaseModel,
    title='Indicators Model',
    alias_generator=Utils().snake_to_camel,
    validate_assignment=True,
):
    """Indicators Model"""

    data: Optional[List['IndicatorModel']] = Field(
        [],
        description='The data for the Indicators.',
        methods=['POST', 'PUT'],
        title='data',
    )


class IndicatorDataModel(
    BaseModel,
    title='Indicator Data Model',
    alias_generator=Utils().snake_to_camel,
    validate_assignment=True,
):
    """Indicators Data Model"""

    data: Optional[List['IndicatorModel']] = Field(
        [],
        description='The data for the Indicators.',
        methods=['POST', 'PUT'],
        title='data',
    )


class IndicatorModel(
    BaseModel,
    alias_generator=Utils().snake_to_camel,
    extra=Extra.allow,
    title='Indicator Model',
    validate_assignment=True,
):
    """Indicator Model"""

    # slot attributes are not added to dict()/json()
    __slot__ = ('_privates_',)

    def __init__(self, **kwargs):
        """Initialize class properties."""
        super().__init__(**kwargs)
        super().__setattr__('_privates_', {'_modified_': 0})

    def __setattr__(self, name, value):
        """Update modified property on any update."""
        super().__setattr__('_privates_', {'_modified_': self.privates.get('_modified_', 0) + 1})
        super().__setattr__(name, value)

    @property
    def modified(self):
        """Return int value of modified (> 0 means modified)."""
        return self._privates_.get('_modified_', 0)

    @property
    def privates(self):
        """Return privates dict."""
        return self._privates_

    active: bool = Field(
        None,
        description='Is the indicator active?',
        methods=['POST', 'PUT'],
        read_only=False,
        title='active',
    )
    active_locked: bool = Field(
        None,
        description='Lock the indicator active value?',
        methods=['POST', 'PUT'],
        read_only=False,
        title='activeLocked',
    )
    address: Optional[str] = Field(
        None,
        description=(
            'The email address associated with this indicator (EmailAddress specific summary '
            'field).'
        ),
        methods=['POST', 'PUT'],
        read_only=False,
        title='address',
    )
    associated_groups: Optional['GroupsModel'] = Field(
        None,
        description='A list of groups that this indicator is associated with.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='associatedGroups',
    )
    associated_indicators: Optional['IndicatorsModel'] = Field(
        None,
        description='A list of indicators associated with this indicator.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='associatedIndicators',
    )
    attributes: Optional['AttributesModel'] = Field(
        None,
        description='A list of Attributes corresponding to the Indicator.',
        methods=['POST', 'PUT'],
        max_size=1000,
        read_only=False,
        title='attributes',
    )
    confidence: Optional[int] = Field(
        None,
        description='The indicator threat confidence.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='confidence',
    )
    date_added: Optional[datetime] = Field(
        None,
        allow_mutation=False,
        description='The date and time that the item was first created.',
        read_only=True,
        title='dateAdded',
    )
    description: Optional[str] = Field(
        None,
        description='The indicator description text.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='description',
    )
    dns_active: bool = Field(
        None,
        description='Is dns active for the indicator?',
        methods=['POST', 'PUT'],
        read_only=False,
        title='dnsActive',
    )
    false_positive_count: Optional[int] = Field(
        None,
        allow_mutation=False,
        description='The number of false positives reported for this indicator.',
        read_only=True,
        title='falsePositiveCount',
    )
    false_positive_last_reported: Optional[datetime] = Field(
        None,
        allow_mutation=False,
        description='The date and time of the last false positive reported for this indicator.',
        read_only=True,
        title='falsePositiveLastReported',
    )
    host_name: Optional[str] = Field(
        None,
        description='The host name of the indicator (Host specific summary field).',
        methods=['POST', 'PUT'],
        read_only=False,
        title='hostName',
    )
    id: Optional[int] = Field(
        None,
        description='The ID of the item.',
        read_only=True,
        title='id',
    )
    ip: Optional[str] = Field(
        None,
        description=(
            'The ip address associated with this indicator (Address specific summary field).'
        ),
        methods=['POST', 'PUT'],
        read_only=False,
        title='ip',
    )
    last_modified: Optional[datetime] = Field(
        None,
        allow_mutation=False,
        description='The date and time that the indicator was last modified.',
        read_only=True,
        title='lastModified',
    )
    last_observed: Optional[datetime] = Field(
        None,
        allow_mutation=False,
        description='The date and time that the indicator was last observed.',
        read_only=True,
        title='lastObserved',
    )
    md5: Optional[str] = Field(
        None,
        description='The md5 associated with this indicator (File specific summary field).',
        methods=['POST', 'PUT'],
        read_only=False,
        title='md5',
    )
    observation_count: Optional[int] = Field(
        None,
        allow_mutation=False,
        description='The number of times this indicator has been observed.',
        read_only=True,
        title='observationCount',
    )
    private_flag: bool = Field(
        None,
        description='Is this indicator private?',
        methods=['POST', 'PUT'],
        read_only=False,
        title='privateFlag',
    )
    rating: Optional[int] = Field(
        None,
        description='The indicator threat rating.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='rating',
    )
    security_labels: Optional['SecurityLabelsModel'] = Field(
        None,
        description=(
            'A list of Security Labels corresponding to the Intel item (NOTE: Setting this '
            'parameter will replace any existing tag(s) with the one(s) specified).'
        ),
        methods=['POST', 'PUT'],
        max_size=1000,
        read_only=False,
        title='securityLabels',
    )
    sha1: Optional[str] = Field(
        None,
        description='The sha1 associated with this indicator (File specific summary field).',
        methods=['POST', 'PUT'],
        read_only=False,
        title='sha1',
    )
    sha256: Optional[str] = Field(
        None,
        description='The sha256 associated with this indicator (File specific summary field).',
        methods=['POST', 'PUT'],
        read_only=False,
        title='sha256',
    )
    size: Optional[int] = Field(
        None,
        description='The size of the file.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='size',
    )
    source: Optional[str] = Field(
        None,
        description='The source for this indicator.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='source',
    )
    summary: Optional[str] = Field(
        None,
        allow_mutation=False,
        description='The indicator summary.',
        read_only=True,
        title='summary',
    )
    tags: Optional['TagsModel'] = Field(
        None,
        description=(
            'A list of Tags corresponding to the item (NOTE: Setting this parameter will replace '
            'any existing tag(s) with the one(s) specified).'
        ),
        methods=['POST', 'PUT'],
        max_size=1000,
        read_only=False,
        title='tags',
    )
    text: Optional[str] = Field(
        None,
        description='The url text value of the indicator (Url specific summary field).',
        methods=['POST', 'PUT'],
        read_only=False,
        title='text',
    )
    threat_assess_confidence: Optional[float] = Field(
        None,
        allow_mutation=False,
        description='The Threat Assess confidence for this indicator.',
        read_only=True,
        title='threatAssessConfidence',
    )
    threat_assess_rating: Optional[float] = Field(
        None,
        allow_mutation=False,
        description='The Threat Assess rating for this indicator.',
        read_only=True,
        title='threatAssessRating',
    )
    threat_assess_score: Optional[int] = Field(
        None,
        allow_mutation=False,
        description='The Threat Assess score for this indicator.',
        read_only=True,
        title='threatAssessScore',
    )
    type: Optional[str] = Field(
        None,
        description='The **type** for the Indicator.',
        methods=['POST', 'PUT'],
        min_length=1,
        read_only=False,
        title='type',
    )
    value1: Optional[str] = Field(
        None,
        description='Custom Indicator summary field value1.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='value1',
    )
    value2: Optional[str] = Field(
        None,
        description='Custom Indicator summary field value2.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='value2',
    )
    value3: Optional[str] = Field(
        None,
        description='Custom Indicator summary field value3.',
        methods=['POST', 'PUT'],
        read_only=False,
        title='value3',
    )
    whois_active: bool = Field(
        None,
        description='Is whois active for the indicator?',
        methods=['POST', 'PUT'],
        read_only=False,
        title='whoisActive',
    )

    @validator('attributes', always=True)
    def _validate_attributes(cls, v):
        if not v:
            return AttributesModel()
        return v

    @validator('associated_groups', always=True)
    def _validate_associated_groups(cls, v):
        if not v:
            return GroupsModel()
        return v

    @validator('associated_indicators', always=True)
    def _validate_associated_indicators(cls, v):
        if not v:
            return IndicatorsModel()
        return v

    @validator('security_labels', always=True)
    def _validate_security_labels(cls, v):
        if not v:
            return SecurityLabelsModel()
        return v

    @validator('tags', always=True)
    def _validate_tags(cls, v):
        if not v:
            return TagsModel()
        return v


# first-party
from tcex.api.tc.v3.attributes.attribute_model import AttributesModel
from tcex.api.tc.v3.groups.group_model import GroupsModel
from tcex.api.tc.v3.security_labels.security_label_model import SecurityLabelsModel
from tcex.api.tc.v3.tags.tag_model import TagsModel

# add forward references
IndicatorDataModel.update_forward_refs()
IndicatorModel.update_forward_refs()
IndicatorsModel.update_forward_refs()