#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
from PyLexer import tokens
#TODO Insertar la lectura lineal!!!
def p_start(p):
	'''start : content'''
	#TODO: Insert the appropiate id.
	p[0] =  p[1]

def p_block(p):
	'''block : BEGINBLOCK content ENDBLOCK'''
	p[0] = p[2]

def p_content(p):
	'''content :  block'''
	p[0] =  p[1] 
def p_contentChar(p):
	'''content : CHAR'''
	p[0] =  p[1] 
def p_contentCon(p):
	'''content : block content
				  | content block
				  | CHAR content
				  | content CHAR'''
	p[0] = p[1] + p[2]

def p_tree(p):
	'''content : fraction
			  | scripted'''
	p[0] =  p[1] 

#------------------------------------------------------------------------------------------------------


def p_fraction(p):
	'''fraction : FRAC block block
					| FRAC CHAR CHAR'''
	p[0] =  'Comienza fracción comienza numerador '+ p[2] + ' termina numerador comienza denominador ' + p[3] + ' termina denominador termina fracción. '  

def p_scriptedSup(p):
	'''scripted : CHAR SUP block
			| CHAR SUP CHAR
			| CHAR SUP block SUB block
			| CHAR SUP CHAR SUB CHAR'''
	if(len(p) == 4):
		p[0] = 'Base ' + p[1] + ' Super indice ' + p[3] + ' termina Super índice. '
	else:
		p[0] = 'Base ' + p[1] + ' Comienza Super indice ' + p[3] + ' Comienza Sub Indice ' + p[5]+ ' termina Sub Indice. '

def p_scriptedSub(p):
	'''scripted : CHAR SUB block
			| CHAR SUB CHAR
			| CHAR SUB block SUP block
			| CHAR SUB CHAR SUP CHAR'''
	if(len(p) == 4):
		p[0] = 'Base ' + p[1] + ' Sub indice ' + p[3] + ' termina Sub índice. '
	else: 
		p[0] = 'Base ' + p[1] + ' Comienza Sub indice ' + p[3] + ' Comienza Super Indice ' + p[5]+ ' termina Super Indice. '
	


def p_error(p):
	print "Syntaxes Error."

parser = yacc.yacc()

def convert(String):
	return parser.parse(String)

