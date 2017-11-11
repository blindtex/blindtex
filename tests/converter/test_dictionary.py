import pytest
from blindtex.converter import dictionary

def test_showReading():
    assert 'alfa' == dictionary.showReading('alpha')