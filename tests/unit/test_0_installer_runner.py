import pytest
from modules import convert_number_to_string


def describe_dummy_kata():
    def should_eror_when_not_integer():
        """🧪 should show an error when receive something other than an integer"""

        with pytest.raises(ValueError, match="Input must be a number"):
            convert_number_to_string.number_to_string("not a number")

    def should_return_string_of_123():
        """🧪 should get '123' when the input is 123"""
        assert convert_number_to_string.number_to_string(123) == "123"

    def should_return_string_of_999():
        """🧪 should get '999' when the input is 999"""
        assert convert_number_to_string.number_to_string(999) == "999"

    def should_return_string_of_negative_100():
        """🧪 should get '-100' when the input is -100"""
        assert convert_number_to_string.number_to_string(-100) == "-100"
