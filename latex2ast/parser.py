#-*-:coding:utf-8-*-

import ply.lex
import ply.yacc
import lexer

from ast import Node
from ast import Child
from ast import interpreter

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
    p[0] = p[1]

def p_simple(p):
	"""
    simple : symbol_operation
           | symbol_ordinary
	       | symBlock
    """
	p[0] = p[1]

def p_symbol_ordinary(p):
	"""
    symbol_ordinary : ordinary
    """
	p[0] = p[1]


def p_symbol_operation(p):
	"""
    symbol_operation | binOp
    """
	p[0] = p[1]

def p_symBlock(p):
	"""
    symBlock  : BEGINBLOCK symbol ENDBLOCK
    """
	p[0] = p[2]

def p_binOp(p):
    """
    binOp : start KBINOP start
          | start KBINOP ordinary
          | ordinary KBINOP start
          | ordinary KBINOP ordinary
    """
    p[0] = Node(p[1],p[2],p[3],'BINARY')

def p_root(p):
    """
    root : ROOT simple
         | ROOT block
         | ROOT KDELIMITER start KDELIMITER simple
         | ROOT KDELIMITER start KDELIMITER block
    """

#def p_expression_group(p):
#    """
#    expression : KDELIMITER expression KDELIMITER
#    """
#    p[0] = '('+ p[2] +')'

def p_ordinary(p):
    """
    ordinary : NUM
             | CHAR
    """
    p[0] = Child(p[1],'ORDINARY')

parser = ply.yacc.yacc()

if __name__ == "__main__":
    latex_string = "a+6"
    custom_lexer = lexer.get_lexer()
    cv = parser.parse(latex_string,custom_lexer)
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
