#-*-:coding:utf-8-*-

import json
import ply.lex as lex
from ply.lex import TOKEN

tokens = ('KDELIMITER',
          'KBINOP', 'NUM', 'CHAR',
          'BEGINBLOCK', 'ENDBLOCK',
          'ROOT','SUP'
          )

def get_lexer():

    states = (('command', 'exclusive'),)
              #('anything','exclusive'),)

    literals = [ '!',"'",]

    BEGINBLOCK = r'\{'
    ENDBLOCK = r'\}'
    KDELIMITER = r'\(|\)|\[|\]'

    KBINOP = r'\+|-|\*|/' #Binary operators that can be made from the keyboard.
    SUP = r'\^'

    CHAR = r'[A-Za-z"%\',.:;|]+?'
    NUM = r'[0-9]{1,}' # TAG numbers with at least one digit

    COMMAND = r'\\'
    command_ROOT = r'sqrt'

    @TOKEN(BEGINBLOCK)
    def t_BEGINBLOCK(t):
    	return t

    @TOKEN(ENDBLOCK)
    def t_ENDBLOCK(t):
    	return t

    @TOKEN(KDELIMITER)
    def t_KDELIMITER(t):
    	return t

    @TOKEN(CHAR)
    def t_CHAR(t):
    	return t

    @TOKEN(NUM)
    def t_NUM(t):
        return t

    @TOKEN(KBINOP)
    def t_KBINOP(t):
    	return t

    @TOKEN(SUP)
    def t_SUP(t):
    	return t

    @TOKEN(COMMAND)
    def t_COMMAND(t):
    	t.lexer.begin('command')
    	return

    @TOKEN(command_ROOT)
    def t_command_ROOT(t):
    	t.lexer.begin('INITIAL') # Back to the initial state
    	return t

    def t_command_error(t):
        print("Illegal character '%s'" % t.value[0])
        #t.lexer.skip(1)
        #raise illegalCharacter

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        #t.lexer.skip(1)
        #raise illegalCharacter

    return lex.lex()

if __name__ =="__main__":
    lexer = get_lexer()
    while True:
        try:
            try:
                s = raw_input()
            except NameError: # Python3
                s = input('spi> ')
        except EOFError:
            break

        lexer.input(s)
        while True:
            tok = lexer.token()
            if not tok:
                break

            print(tok)
