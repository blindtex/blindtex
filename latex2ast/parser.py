#-*-:coding:utf-8-*-

import ply.lex
import ply.yacc
import lexer

from ast import Node
from ast import Child
from ast import interpreter

tokens = lexer.tokens

def p_expression(p):
    """
    expression : expression KBINOP expression
               | expression KBINOP ordinary
               | ordinary KBINOP expression
               | ordinary KBINOP ordinary
    """
    p[0] = Node(p[1],p[2],p[3],'BINARY')


def p_expression_group(p):
    """
    expression : KDELIMITER expression KDELIMITER
    """
    p[0] = '('+ p[2] +')'

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
