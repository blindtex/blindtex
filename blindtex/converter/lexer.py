#Lexer of LaTeX math content

import ply.lex as lex
from ply.lex import TOKEN
import json
import re


fileName = 'regexes.json'
 
tokens = ('CHAR', 'SUP', 'SUB','BEGINBLOCK','ENDBLOCK', 'ORD', 'FRAC', 'ROOT', 'LARGEOP', 'BINOP','KBINOP','KBINREL', 'BINREL', 'NOT', 'FUNC', 'ARROW', 'KDELIMITER', 'DELIMITER', 'ACCENT','STYLE','DOTS','LIM', 'UNKNOWN', 'BEGARRAY', 'ENDARRAY', 'LINEBREAK', 'COL')

states = (('command', 'exclusive'),)

try:
	myFile = open(fileName, 'r')
	dictOfDicts = json.load(myFile)
	myFile.close()
except IOError:
	print 'File %s was not found.'%fileName


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
def t_command_BEGARRAY(t):
	r'begin\{array\}(\{.*?\})?'
	t.lexer.begin('INITIAL')
	return t

def t_command_ENDARRAY(t):
	r'end\{array\}'
	t.lexer.begin('INITIAL')
	return t

def t_command_LINEBREAK(t):
	r'\\'
	t.lexer.begin('INITIAL')
	return t

def t_COL(t):
	r'[&]'
	return t

@TOKEN(dictOfDicts['largeOperator'])
def t_command_LARGEOP(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['ordinary'])
def t_command_ORD(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_FRAC(t):
	r'frac'
	t.lexer.begin('INITIAL')
	return t

def t_command_ROOT(t):
	r'sqrt'
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['arrow'])
def t_command_ARROW(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_leftRight(t):
	r'(left)|(right)'
	t.lexer.begin('INITIAL')
	pass

def t_KBINOP(t):#Binary operators that can be made from the keyboard.
	r'\+|-|\*|/'
	return t

@TOKEN(dictOfDicts['dots'])
def t_command_DOTS(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['binOp'])	
def t_command_BINOP(t):
	
	t.lexer.begin('INITIAL')
	return t


def t_KBINREL(t):
	r'[=<>]'	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['binRel'])
def t_command_BINREL(t):
		
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['func'])
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

@TOKEN(dictOfDicts['delimiter'])
def t_command_DELIMITER(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['accent'])
def t_command_ACCENT(t):

	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['style'])
def t_command_STYLE(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_LIM(t):
	r'lim'
	t.lexer.begin('INITIAL')
	return t

def t_CHAR(t):
	r'[A-Za-z0-9]+?'
	return t

def t_command_UNKNOWN(t):
	r'[A-Za-z]+'
	t.lexer.begin('INITIAL')
	return t

t_ignore_SPACE=r'[ \t\n]+'


def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


lexer= lex.lex()
#while True:
#	s = raw_input()
#	lexer.input(s)
#	while True:
#		tok = lexer.token()
#		if not tok:
#			break
#		print tok
