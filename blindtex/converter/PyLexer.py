#Lexer of LaTeX math content

import ply.lex as lex

tokens = ('CHAR', 'SUP', 'SUB','BEGINBLOCK','ENDBLOCK', 'BEGINSBLOCK','ENDSBLOCK', 'ORD', 'FRAC','SPACE', 'ROOT')

states = (('command', 'exclusive'),)



def t_BEGINBLOCK(t):
	r'\{'
	return t

def t_ENDBLOCK(t):
	r'\}'
	return t

def t_BEGINSBLOCK(t):
	r'\['
	return t

def t_ENDSBLOCK(t):
	r'\]'
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
	pass

def t_command_ORD(t):
	r'(alpha)|(beta)'
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

def t_CHAR(t):
	r'[A-Za-z0-9]+?'
	return t

t_ignore_SPACE=r'[ \t]+'


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
