#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
from PyLexer import tokens


#TODO Que esto sea una estructura de datos, con funciones para cambiar la lectura(value) con mayor facilidad.
Ordinary = {'alpha': 'alfa', 'beta': 'beta'}
#TODO Insertar la lectura lineal!!!

precedence = (
	('left','SUP','SUB', 'FRAC'),
)

def p_start(p):
	'''start : content'''
	p[0] =  p[1] 

def p_block(p):
	'''block : BEGINBLOCK content ENDBLOCK'''
	p[0] = p[2]

def p_contentOrd(p):
	'''content : CHAR
				| ord
				| block '''
	p[0] = p[1]

def p_ord(p):
	'''ord : ORD '''
	p[0] =  '<span aria-label=\"' + Ordinary[p[1]] + '\"></span>'	

def p_space(p):
	'''content : SPACE'''
	pass

def p_tree(p):
	'''content : scripted
					| command '''
	p[0] = p[1]

def p_command(p):
	'''command : frac '''
	p[0] = p[1]
#------------------------------------------------------------------------------------------------------


#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels; tal vez con una función.
def p_scripted(p):
	'''scripted : content SUP content
				| content SUB content '''
	if(p[2] == '^'):
		p[0] = p[1] + '<span aria-label=\"sup índice\"></span>' + p[3] + '<span aria-label=\"fin sup índice\"></span>'
	else:
		p[0] = p[1] + '<span aria-label=\"sub índice\"></span>' + p[3] + '<span aria-label=\"fin sub índice\"></span>'
	
def p_frac(p):
	'''frac : FRAC content content '''
	p[0] = '<span aria-label=\"comienza fracción\"></span>' + p[2] + '<span aria-label=\"sobre\"></span>' + p[3] + '<span aria-label=\"fin fracción\"></span>'


def p_error(p):
	print "Syntaxes Error."
	return p

parser = yacc.yacc()

def convert(String):
	return parser.parse(String)

