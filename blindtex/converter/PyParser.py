#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
from blindtex.converter.MathDictionary import *
from PyLexer import tokens


#TODO Que esto sea una estructura de datos, con funciones para cambiar la lectura(value) con mayor facilidad.


#TODO: Acordar los nombres de algunos operadores.
LargeOperators ={'sum': 'suma','prod':'producto', 'coprod':'coproducto','int': 'integral', 'oint': 'integral de contorno', 'bigcap': 'intersecci&oacute;n','bigcup': 'uni&oacute;n', 'bigsqcup':'Uni&oacute;n rect&aacute;ngular', 'bigvee' :'disyunci&oacute;n','bigwedge' : 'conjunci&oacute;n', 'bigodot': 'circumpunto','bigotimes': 'prducto tensorial','bigoplus': 'circumsuma', 'biguplus': 'uni&oacute;n con suma'}

precedence = (	
	('left','SUP','SUB', 'FRAC','ROOT'),
)

def p_start(p):
	'''start : content'''
	p[0] =  p[1] 

def p_sblock(p):
	'''sblock : BEGINSBLOCK content ENDSBLOCK'''
	p[0] = p[2]

def p_block(p):
	'''block : BEGINBLOCK content ENDBLOCK'''
	p[0] = p[2]

def p_content(p):
	'''content : chars
				| block
				| scripted
				| command'''
	p[0]=p[1]

def p_chars(p):
	'''chars : CHAR
				| ord
				| chars chars '''
	if(len(p) == 3):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1]

def p_ord(p):
	'''ord : ORD '''
	p[0] =  '<span aria-label=\"' + Ordinary[p[1]] + '\">&nbsp;</span>'


def p_command(p):
	'''command : frac
				| root '''
	p[0] = p[1]

#------------------------------------------------------------------------------------------------------


#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels; tal vez que p[0] = "una función que depende de los otros p[i]".

def p_scripted(p):
	'''scripted : content SUP content
				| content SUB content '''
	if(p[2] == '^'):
		p[0] = p[1] + '<span aria-label=\"sup &iacute;ndice\">&nbsp;</span>' + p[3] + '<span aria-label=\"fin sup &iacute;ndice\">&nbsp;</span>'
	else:
		p[0] = p[1] + '<span aria-label=\"sub &iacute;ndice\">&nbsp;</span>' + p[3] + '<span aria-label=\"fin sub &iacute;ndice\">&nbsp;</span>'
	
def p_frac(p):
	'''frac : FRAC content content'''
	p[0] = '<span aria-label=\"comienza fracción\">&nbsp;</span>' + p[2] + '<span aria-label=\"sobre\">&nbsp;</span>' + p[3] + '<span aria-label=\"fin fracción\">&nbsp;</span>'

def p_root(p):
	'''root : ROOT content
			| ROOT sblock content '''
	if(len(p) == 3):
		p[0] = '<span aria-label=\"ra&iacute;z cuadrada de\">&nbsp;</span>' + p[2] + '<span aria-label=\"termina ra&iacute;z\">&nbsp;</span>'
	else:
		p[0] = '<span aria-label=\"ra&iacute;z\">&nbsp;</span>' + p[2] + '<span aria-label=\"de\" >&nbsp;</span>' + p[3] + '<span aria-label=\"termina ra&iacute;z\">&nbsp;</span>'




def p_error(p):
	if p:
		print("Syntax error at token", p.type)
		# Just discard the token and tell the parser it's okay.
		parser.errok()
	else:
		print("Syntax error at EOF")

parser = yacc.yacc()

def convert(String):
	return parser.parse(String)

