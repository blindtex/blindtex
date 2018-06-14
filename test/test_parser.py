import pytest
from latex2ast import lexer
from latex2ast import parser

#def test_kbinop():
#    custom_parser = parser.get_parser()
#    latex_string = 'x+3'
#    custom_lexer = lexer.get_lexer()
#    cv = custom_parser.parse(latex_string,custom_lexer)
#    assert cv.left.content == 'x'
#    assert cv.content == '+'
#    assert cv.right.content == '3'

#def test_sqrt():
#    custom_parser = parser.get_parser()
#    latex_string = '\sqrt[8]{x}'
#    custom_lexer = lexer.get_lexer()
#    cv = custom_parser.parse(latex_string,custom_lexer)
#    assert cv.left is None
#    assert cv.content == 'sqrt'
#    assert cv.superscript.content == '8'
#    assert cv.right.content == 'x'

def test_symbol():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = 'a'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	latex_string = '1'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == '1'
	latex_string = r'\alpha'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'alpha'
#EOF
def test_block():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = '{a}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
#EOF
def test_concatenation():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = 'ab'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.left.content == 'a'
	assert cv.right.content == 'b'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'a\beta'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.left.content == 'a'
	assert cv.right.content == 'beta'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = '2a'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.left.content == '2'
	assert cv.right.content == 'a'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = '{a}b'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.left.content == 'a'
	assert cv.right.content == 'b'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = 'a{b}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.left.content == 'a'
	assert cv.right.content == 'b'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = 'abc'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.left.content == 'concatenation'
	assert cv.left.left.content == 'a'
	assert cv.left.right.content == 'b'
	assert cv.right.content == 'c'
	
#EOF
def test_delimiters():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = '(a)'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.left_delimiter == '('
	assert cv.right_delimiter == ')'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = '[a)'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.left_delimiter == '['
	assert cv.right_delimiter == ')'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\{a\}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.left_delimiter == '{'
	assert cv.right_delimiter == '}'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\langle a \rangle'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.left_delimiter == 'langle'
	assert cv.right_delimiter == 'rangle'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'(ab)'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.left.content == 'a'
	assert cv.right.content == 'b'
	assert cv.left_delimiter == '('
	assert cv.right_delimiter == ')'

def test_accent():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\hat{a}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.accent == 'hat'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\acute a'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.accent == 'acute'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\hat{ab}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.accent == 'hat'
	assert cv.left.content == 'a'
	assert cv.right.content == 'b'

def test_style():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\mathit{a}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.style == 'mathit'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\mathbf a'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.style == 'mathbf'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'\mathrm{ab}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'concatenation'
	assert cv.style == 'mathrm'
	assert cv.left.content == 'a'
	assert cv.right.content == 'b'

def test_simple_indexes():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = 'a^b'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.superscript.content == 'b'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'a^{b}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.superscript.content == 'b'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = 'a_b'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.subscript.content == 'b'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'a_{b}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.subscript.content == 'b'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'a_{b^c}'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.subscript.content == 'b'
	assert cv.subscript.superscript.content == 'c'

def test_compound_indexes():
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = 'a^b_c'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.superscript.content == 'b'
	assert cv.subscript.content == 'c'
	custom_parser = parser.get_parser()
	custom_lexer = lexer.get_lexer()
	latex_string = r'a_c^b'
	cv = custom_parser.parse(latex_string,custom_lexer)
	assert cv.content == 'a'
	assert cv.superscript.content == 'b'
	assert cv.subscript.content == 'c'

	
	
	
	
	
	
