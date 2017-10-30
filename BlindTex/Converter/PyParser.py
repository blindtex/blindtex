#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
from PyLexer import tokens
#TODO Insertar la lectura lineal!!!
def p_start(p):
	'''start : content'''
	#TODO: Insert the appropiate id.
	p[0] = '<ul id=\"tree\" class=\"tree root-level\" role=\"tree\" tabindex=\"0\">\n' + p[1] + '</ul>\n'

def p_block(p):
	'''block : BEGINBLOCK content ENDBLOCK'''
	p[0] = p[2]

def p_content(p):
	'''content :  block'''
	p[0] =  p[1] 

def p_contentOrd(p):
	'''content : CHAR
				| ord '''
	p[0] = '<li tabindex=\"-1\" role=\"treeitem\">' + p[1] + '</li>\n'

def p_ord(p):
	'''ord : ORD '''
	#TODO write function to convert
	p[0] =  p[1]

def p_contentCon(p):
	'''content : block content
				  | content block
				  | ord content
				  | content ord'''
	p[0] = p[1] + p[2]

def p_tree(p):
	'''content : scripted
					| command '''
	p[0] = '<li class=\"tree-parent\" role=\"treeitem\" tabindex=\"0\" aria-expanded=\"false\">\n' + p[1] + '</li>\n'

def p_command(p):
	'''command : frac '''
	p[0] = p[1]
#------------------------------------------------------------------------------------------------------

#TODO Ojo que la base no siempre es ord.
#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels.
def p_scriptedSup(p):
	'''scripted : content SUP block
			| content SUP content
			| content SUP block SUB block
			| content SUP content SUB content'''
	if(len(p) == 4):
		p[0] = '<span aria-label=\"Con índices\"></span>\n<ul role=\"group\">\n<span aria-label=\"Base\"></span>' + p[1] + '<span aria-label=\"Super índice\"></span>' + p[3] +'</ul>'
	else:
		p[0] =  '<span aria-label=\"Con índices\"></span>\n<ul role=\"group\">\n<span aria-label=\"Base\"></span>' + p[1] + '<span aria-label=\"Super índice\"></span>' + p[3] +'<span aria-label=\"Sub índice\"></span>' + p[5] + '</ul>'

def p_scriptedSub(p):
	'''scripted : content SUB block
			| content SUB content
			| content SUB block SUP block
			| content SUB content SUP content'''
	if(len(p) == 4):
		p[0] = '<span aria-label=\"Con índices\"></span>\n<ul role=\"group\">\n<span aria-label=\"Base\"></span>' + p[1] + '<span aria-label=\"Sub índice\"></span>' +  p[3] +'</ul>'
	else:
		p[0] = '<span aria-label=\"Con índices\"></span>\n<ul role=\"group\">\n<span aria-label=\"Base\"></span>' + p[1] + '<span aria-label=\"Sub índice\"></span>' + p[3] +'<span aria-label=\"Super índice\"></span>' + p[5] + '</ul>'

def p_frac(p):
	'''frac : FRAC block block
				| FRAC content content '''
	p[0] = '<span aria-label=\"Fracción\"></span><ul role=\"group\">\n<span aria-label=\"Numerador\"></span>' + p[2] + '<span aria-label=\"Denominador\"></span>' +   p[3] + '</ul>'
	


def p_error(p):
	print "Syntaxes Error."
	return p

parser = yacc.yacc()

def convert(String):
	return parser.parse(String)

