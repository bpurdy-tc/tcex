# -*- coding: utf-8 -*-
"""Validation file for testing profiles."""


class Validation:
    """Validation base class for App output validation."""

    def __init__(self, validator):
        """Initialize class properties."""
        self.validator = validator

    def validation(self, output_variables):
        """Validate Redis output data."""
        if output_variables is None:
            return
        % for data in output_data:

        if '${data['variable']}' in output_variables:
            data = output_variables.get('${data['variable']}')
            self.${data['method']}(data)
        % endfor
    % for data in output_data:

    def ${data['method']}(self, data):
        """Assert output data for variable ${data['data['variable']}."""
        assert self.validator.redis.data(
            '${data['variable']}',
            data.get('expected_output'),
            data.get('op', '='),
        )
    % endfor
