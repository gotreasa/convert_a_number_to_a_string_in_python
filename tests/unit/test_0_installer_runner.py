import pytest
from modules import convert_number_to_string


def describe_dummy_kata():
    def should_eror_when_not_integer(capsys):
        """🧪 should show an error when receive something other than an integer"""

        with pytest.raises(ValueError, match="Input must be a number"):
            convert_number_to_string.number_to_string("not a number")
