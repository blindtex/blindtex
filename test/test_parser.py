import pytest
from latex2ast import lexer
from latex2ast import parser

def test_kbinop():
    custom_parser = parser.get_parser()
    latex_string = 'x+3'
    custom_lexer = lexer.get_lexer()
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert cv.left.content == 'x'
    assert cv.content == '+'
    assert cv.right.content == '3'

def test_sqrt():
    custom_parser = parser.get_parser()
    latex_string = '\sqrt[8]{x}'
    custom_lexer = lexer.get_lexer()
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert cv.left is None
    assert cv.content == 'sqrt'
    assert cv.superscript.content == '8'
    assert cv.right.content == 'x'
