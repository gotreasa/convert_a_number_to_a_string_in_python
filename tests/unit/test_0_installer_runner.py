import os

from modules import convert_number_to_string


def describe_dummy_kata():
    def should_print_title(capsys):
        """🧪 expect the dummy kata prints the title"""
        convert_number_to_string.print_the_title()
        out, _err = capsys.readouterr()
        assert "😊 Welcome to Dummy Kata" in out
