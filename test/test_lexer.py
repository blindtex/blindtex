import pytest
from latex2ast import lexer

def get_list_token(lexer):
    list_of_tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        list_of_tokens.append(tok.type)

    return list_of_tokens

def test_token_sqrt():
    simple_sqrt = '\sqrt a'
    simple_sqrt_tokens = ['ROOT','CHAR']
    lexer_test = lexer.get_lexer()
    lexer_test.input(simple_sqrt)
    list_of_tokens = get_list_token(lexer_test)
    assert list_of_tokens == simple_sqrt_tokens

def test_t_BEGINBLOCK():
    BEGINBLOCK = '{'
    lexer_test = lexer.get_lexer()
    lexer_test.input(BEGINBLOCK)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['BEGINBLOCK' == token for token in list_of_tokens ])

def test_t_ENDBLOCK():
    ENDBLOCK = '}'
    lexer_test = lexer.get_lexer()
    lexer_test.input(ENDBLOCK)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['ENDBLOCK' == token for token in list_of_tokens ])

def test_t_KDELIMITER():
    KDELIMITER = '()[]'
    lexer_test = lexer.get_lexer()
    lexer_test.input(KDELIMITER)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['KDELIMITER' == token for token in list_of_tokens ])

def test_t_CHAR():
    CHAR = 'blindtex'
    lexer_test = lexer.get_lexer()
    lexer_test.input(CHAR)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['CHAR' == token for token in list_of_tokens ])

def test_t_NUM():
    NUM = '1234567890'
    lexer_test = lexer.get_lexer()
    lexer_test.input(NUM)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['NUM' == token for token in list_of_tokens ])

def test_t_KBINOP():
    KBINOP = '+-*/'
    lexer_test = lexer.get_lexer()
    lexer_test.input(KBINOP)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['KBINOP' == token for token in list_of_tokens ])

def test_t_SUP():
    SUP = '^'
    lexer_test = lexer.get_lexer()
    lexer_test.input(SUP)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['SUP' == token for token in list_of_tokens ])

def test_t_COMMAND():
    COMMAND = '\\'
    lexer_test = lexer.get_lexer()
    lexer_test.input(COMMAND)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['COMMAND' == token for token in list_of_tokens ])

def test_t_command_ROOT():
    command_ROOT = '\\sqrt'
    lexer_test = lexer.get_lexer()
    lexer_test.input(command_ROOT)
    list_of_tokens = get_list_token(lexer_test)
    assert all(['ROOT' == token for token in list_of_tokens ])
