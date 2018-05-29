import pytest
from latex2ast import lexer

def test_get_lexer_KBINOP():
    KBINOP = '+-*/'
    NO_KBINOP = "\sum"
    lexer_test = lexer.get_lexer()
    lexer_test.input(KBINOP)
    assert 'KBINOP' == lexer_test.token().type
    assert 'KBINOP' == lexer_test.token().type
    assert 'KBINOP' == lexer_test.token().type
    assert 'KBINOP' == lexer_test.token().type
