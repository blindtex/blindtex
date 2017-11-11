from blindtex.converter import parser
import pytest

def test_formulate():
    assert '<span aria-label="alpha"></span>' == parser.formulate('alpha')

def test_convert():
	assert '<span aria-label="comienza fracci&oacute;n"></span>a<span aria-label="sobre"></span>b<span aria-label="fin fracci&oacute;n"></span>' == parser.convert('\\frac{a}{b}')
