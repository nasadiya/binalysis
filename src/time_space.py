"""
Auxiliary functions to facilitate time conversions.
"""

from datetime import datetime, timedelta

EPOCH = datetime(1970, 1, 1)


class TimeType:
    """
    to create a time object which can then be converted to any desired format
    """
    def __init__(self, value, time_type='datetime',
                 time_format=None):
        """
        :param value: time expressed in any format
        :param time_type: type e.g. 'seconds', '%d%b%Y' etc. or a 'datetime'
        object.
        :param time_format: format of the datetime object
        format specification should be ACCURATE
        """
        self.orig_value = value
        self.orig_type = time_type
        self.orig_format = time_format

        if time_type == 'datetime':
            self.datetime = value
        elif time_type == 'sometime':
            self.datetime = datetime.strptime(value, time_format)
        else:
            argument = {time_type: value}
            self.datetime = EPOCH + timedelta(**argument)

    def add_to(self, value, time_type):
        """
        add time to the object
        :param value: value
        :param time_type: seconds, milliseconds etc.
        :return: update the datetime object
        """
        argument = {time_type: value}
        self.datetime += timedelta(**argument)

    def to_millis(self):
        """
        converts datetime to milliseconds
        """
        return int((self.datetime - EPOCH).total_seconds() * 1000)
