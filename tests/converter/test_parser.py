from blindtex.converter import parser
import pytest

def test_formulate():
    assert '<span aria-label="alpha"></span>' == parser.formulate('alpha')

def test_convert():
	assert 'a' + parser.formulate("s&uacute;per") + 'b' + parser.formulate('fin s&uacute;per') == parser.convert('a^b')
	assert 'a' + parser.formulate("s&uacute;per") + 'b' + parser.formulate('fin s&uacute;per') == parser.convert('a^{b}')
	assert 'a' + parser.formulate('sub') + 'b' + parser.formulate('fin sub') == parser.convert('a_b')
	assert 'a' + parser.formulate('sub') + 'b' + parser.formulate('fin sub') == parser.convert('a_{b}')
	assert 'a' + parser.formulate('s&uacute;per') + 'b' + parser.formulate('fin s&uacute;per') + parser.formulate('sub') + 'c' + parser.formulate('fin sub') == parser.convert('a^b_c')
	assert 'a' + parser.formulate('s&uacute;per') + 'b' + parser.formulate('fin s&uacute;per') + parser.formulate('sub') + 'c' + parser.formulate('fin sub') == parser.convert('a^{b}_c')
	assert 'a' + parser.formulate('s&uacute;per') + 'b' + parser.formulate('fin s&uacute;per') + parser.formulate('sub') + 'c' + parser.formulate('fin sub') == parser.convert('a^{b}_{c}')
	assert 'a' + parser.formulate('s&uacute;per') + 'b' + parser.formulate('fin s&uacute;per') + parser.formulate('sub') + 'c' + parser.formulate('fin sub') == parser.convert('a^b_{c}')
	assert parser.formulate('comienza fracci&oacute;n') + 'a' + parser.formulate('sobre') + 'b' + parser.formulate('fin fracci&oacute;n') == parser.convert('\\frac ab')
	assert parser.formulate('comienza fracci&oacute;n') + 'a' + parser.formulate('sobre') + 'b' + parser.formulate('fin fracci&oacute;n') == parser.convert('\\frac a b')
	assert parser.formulate('comienza fracci&oacute;n') + 'a' + parser.formulate('sobre') + 'b' + parser.formulate('fin fracci&oacute;n') == parser.convert('\\frac{a}{b}')
	assert parser.formulate('comienza fracci&oacute;n') + 'a' + parser.formulate('sobre') + 'b' + parser.formulate('fin fracci&oacute;n') == parser.convert('\\frac{a}b')
	assert parser.formulate('comienza fracci&oacute;n') + 'a' + parser.formulate('sobre') + 'b' + parser.formulate('fin fracci&oacute;n') == parser.convert('\\frac a{b}')
	assert parser.formulate('ra&iacute;z cuadrada de') + 'a' + parser.formulate('termina ra&iacute;z') == parser.convert('\\sqrt a')	
	assert parser.formulate('ra&iacute;z cuadrada de') + 'a' + parser.formulate('termina ra&iacute;z') == parser.convert('\\sqrt{a}')
	assert parser.formulate('ra&iacute;z') + 'b' + parser.formulate('de') + 'a' + parser.formulate('termina ra&iacute;z') == parser.convert('\\sqrt[b]{a}')
	assert parser.formulate('ra&iacute;z') + 'b' + parser.formulate('de') + 'a' + parser.formulate('termina ra&iacute;z') == parser.convert('\\sqrt[b]a')


