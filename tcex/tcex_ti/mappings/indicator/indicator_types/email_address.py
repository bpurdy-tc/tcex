# -*- coding: utf-8 -*-
"""ThreatConnect TI Email Address"""
from tcex.tcex_ti.mappings.indicator.tcex_ti_indicator import Indicator


class EmailAddress(Indicator):
    """Unique API calls for Email Address API Endpoints"""

    def __init__(self, tcex, address, **kwargs):
        """Initialize Class Properties.

        Args:
            address (str): The value for this Indicator.
            active (bool, kwargs): If False the indicator is marked "inactive" in TC.
            confidence (str, kwargs): The threat confidence for this Indicator.
            date_added (str, kwargs): The date timestamp the Indicator was created.
            last_modified (str, kwargs): The date timestamp the Indicator was last modified.
            private_flag (bool, kwargs): If True the indicator is marked as private in TC.
            rating (str, kwargs): The threat rating for this Indicator.
            xid (str, kwargs): The external id for this Indicator.
        """
        super(EmailAddress, self).__init__(tcex, 'emailAddresses', **kwargs)
        self.api_entity = 'emailAddress'
        self._data['address'] = address
        self.unique_id = address or kwargs.get('address', None)

    def can_create(self):
        """
        If the address has been provided returns that the EmailAddress can be created, otherwise
        returns that the EmailAddress cannot be created.

        Returns:

        """
        if self.data.get('address'):
            return True
        return False

    def _set_unique_id(self, json_response):
        """
        Sets the unique_id provided a json response.

        Args:
            json_response:
        """
        self.unique_id = json_response.get('emailAddress', '')
