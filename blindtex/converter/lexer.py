#-*-:coding:utf-8-*-
#Lexer of LaTeX math content

import ply.lex as lex
from ply.lex import TOKEN
import json
import re
import os
import sys

tokens = ('CHAR', 'SUP', 'SUB','BEGINBLOCK','ENDBLOCK', 'ORD', 'FRAC', 'ROOT', 'LARGEOP',
          'BINOP','KBINOP','KBINREL', 'BINREL', 'NOT', 'FUNC', 'ARROW', 'KDELIMITER', 'DELIMITER',
          'ACCENT','STYLE','DOTS','LIM', 'UNKNOWN', 'BEGARRAY', 'ENDARRAY', 'LINEBREAK', 'COL','CHOOSE',
          'BINOM', 'PMOD','PHANTOM','TEXT','LABEL','ANYTHING','ARRAYTEXT', 'USER')

states = (('command', 'exclusive'),('anything','exclusive'),)
        
# Put global scope 
#dictOfDicts = dict()

# try:
with open(os.path.join('converter','dicts','regexes.json'), 'r') as myFile:
    dictOfDicts = json.load(myFile)
# except IOError:
	# print('[Error] File could not be opened.')

# Put variable out of the scope
#dictOfDicts = json.load(myFile)


literals = [ '!',"'",]


def t_BEGINBLOCK(t):
	r'\{'
	return t

def t_ENDBLOCK(t):
	r'\}'
	return t

def t_SUP(t):
	r'\^'
	return t

def t_SUB(t):
	r'_'
	return t

def t_COMMAND(t):
	r'\\'
	t.lexer.begin('command')
	return

def t_command_PMOD(t):
	r'pmod'
	t.lexer.begin('INITIAL')
	return t

def t_command_PHANTOM(t):
	r'[hv]?phantom'
	t.lexer.begin('INITIAL')
	return t

def t_command_BEGARRAY(t):
	r'(begin\{array\}|begin\{[pbBvV]?matrix(\*)?\})(\[.*?\])?(\{.*?\})?'
	t.lexer.begin('INITIAL')
	return t

def t_command_ENDARRAY(t):
	r'end\{array\}|end\{[pbBvV]?matrix(\*)?\}'
	t.lexer.begin('INITIAL')
	return t

def t_command_LINEBREAK(t):
	r'\\'
	t.lexer.begin('INITIAL')
	return t

def t_COL(t):
	r'[&]'
	return t

@TOKEN(dictOfDicts['LargeOperators'])
def t_command_LARGEOP(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['Ordinary'])
def t_command_ORD(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_FRAC(t):
	r'frac|tfrac|dfrac'
	t.lexer.begin('INITIAL')
	return t

def t_command_ROOT(t):
	r'sqrt'
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['Arrows'])
def t_command_ARROW(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_leftRight(t):
	r'(left)|(right)|left\.|right\.'
	t.lexer.begin('INITIAL')
	pass

def t_KBINOP(t):#Binary operators that can be made from the keyboard.
	r'\+|-|\*|/'
	return t

@TOKEN(dictOfDicts['Dots'])
def t_command_DOTS(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['BinaryOperators'])	
def t_command_BINOP(t):
	
	t.lexer.begin('INITIAL')
	return t


def t_KBINREL(t):
	r'[=<>]'	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['BinaryRelations'])
def t_command_BINREL(t):
		
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['MathFunctions'])
def t_command_FUNC(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_NOT(t):
	r'not'
	t.lexer.begin('INITIAL')
	return t

def t_KDELIMITER(t):
	r'\(|\)|\[|\]'
	return t

@TOKEN(dictOfDicts['Delimiters'])
def t_command_DELIMITER(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['Accents'])
def t_command_ACCENT(t):

	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['Styles'])
def t_command_STYLE(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_LIM(t):
	r'lim'
	t.lexer.begin('INITIAL')
	return t

def t_command_CHOOSE(t):
	r'choose'
	t.lexer.begin('INITIAL')
	return t

def t_command_BINOM(t):
	r'binom'
	t.lexer.begin('INITIAL')
	return t

def t_command_MATHSPACE(t):
	r'[,!:;]|quad|qquad'
	t.lexer.begin('INITIAL')
	pass

def t_command_TEXT(t):
        r'(text(rm)?|mbox)\{'
        t.lexer.begin('anything')
        return t

def t_command_LABEL(t):
        r'label\{'
        t.lexer.begin('anything')
        return t
def t_ARRAYTEXT(t):
        r'~text\{'
        t.lexer.begin('anything')
        return t

def t_anything_ANYTHING(t):
        r'[^}]'
        return t

def t_anything_ENDANY(t):
        r'(?<!\\)\}'
        t.lexer.begin('INITIAL')
        pass
        
def t_CHAR(t):
	r'[A-Za-z0-9 "%\',.:;|]+?'
	return t

@TOKEN(dictOfDicts['UserDict'])
def t_command_USER(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_UNKNOWN(t):
	r'[A-Za-z ]+'
	t.lexer.begin('INITIAL')
	return t

t_ignore_SPACE=r'[ \t\n]+'
#---------------Error Handling-----------------
class illegalCharacter(Exception):
        def __init__(self):
                return
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	raise illegalCharacter

#---------------------------------------------
lexer= lex.lex()

if __name__ =="__main__":
	while True:
		s = raw_input()
		lexer.input(s)
		while True:
			tok = lexer.token()
			if not tok:
				break
			print tok
