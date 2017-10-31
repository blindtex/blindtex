import pytest
from blindtex.converter import ecuation

def test_latexToGramatic():
	ecuationResult = ecuation.latexToGramatic("Dummy")
	assert "X plus Y" == ecuationResult
