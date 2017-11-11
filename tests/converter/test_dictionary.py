import pytest
from blindtex.converter import dictionary

def test_showReading():
    assert 'alfa' == dictionary.showReading('alpha')

def test_showlatex():
    assert 'alpha'  == dictionary.showlatex('alfa')
def test_showlatex():
    assert 'The value does not key'  == dictionary.showlatex('alffa')