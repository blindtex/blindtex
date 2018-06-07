#-*-:coding:utf-8-*-

import ply.lex
import ply.yacc
import lexer

from ast import Node

tokens = lexer.tokens

def p_start(p):
    """
    start : formula
    """
    p[0] = p[1]

def p_formula(p):
    """
    formula : simple
            | command
            | block
    """
    p[0] = p[1]

def p_block(p):
    """
    block : BEGINBLOCK start ENDBLOCK
    """
    p[0] = p[2]

def p_simple(p):
    """
    simple : symbol_operation
           | symbol_ordinary
           | symbol_block
    """
    p[0] = p[1]

def p_symbol_ordinary(p):
	"""
    symbol_ordinary : ordinary
    """
	p[0] = p[1]


def p_symbol_operation(p):
    """
    symbol_operation : binary_operator
    """
    p[0] = p[1]

def p_symBlock(p):
	"""
    symbol_block  : BEGINBLOCK symbol_ordinary ENDBLOCK
                  | BEGINBLOCK symbol_operation ENDBLOCK
    """
	p[0] = p[2]

def p_binOp(p):
    """
    binary_operator : start KBINOP start
    """
    p[0] = Node(left=p[1], content=p[2], right=p[3])

def p_command(p):
    """
    command : root
    """
    p[0] = p[1]

def p_root(p):
    """
    root : ROOT start
         | ROOT KDELIMITER start KDELIMITER start
    """
    if(len(p)==3): # \sqrt{x}
        p[0] = Node(content=p[1], right=p[2])
    elif(len(p)==6): # \sqrt[4]{y}
        p[0] = Node(content=p[1], right=p[5], superscript=p[3])

def p_ordinary(p):
    """
    ordinary : NUM
             | CHAR
    """
    p[0] = Node(content=p[1])

def get_parser():
    return ply.yacc.yacc()

if __name__ == "__main__":
    parser = get_parser()
    latex_string = "\sqrt{2+3}"
    custom_lexer = lexer.get_lexer()
    cv = parser.parse(latex_string,custom_lexer)#,debug=1)
    print(interpreter(cv))
    while True:
        try:
            try:
                s = raw_input()
            except NameError: # Python3
                s = input('spi> ')

            cv_s = parser.parse(s,custom_lexer)
            print(interpreter(cv_s))
        except EOFError:
            break
