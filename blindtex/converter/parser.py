#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
#from blindtex.converter.MathDictionary import *
from MathDictionary import *
from PyLexer import tokens

#Funciones: en esta sección, dejaremos todas las funciones que se requieran


def formulate(label):
	'''
	Function to put in a span tag with the desired label.

	Args:
		label(str): The label that is needed in a span tag, 
						if the label has accents it is recomended put them as html asks.

	Returns:
		str: The string with the aria-label already put.

	Examples:
		>>>print(formulate('integral'))
		'<span aria-label=\"integral\">&nbsp;</span>'
	'''
	return '<span aria-label=\"'+ label + '\"></span>'
#EndOfFunction
#--------------------------------------------------------------------------




#TODO Que esto sea una estructura de datos, con funciones para cambiar la lectura(value) con mayor facilidad.



#TODO: Acordar los nombres de algunos operadores.
LargeOperators ={'sum': ['suma'],'prod':['producto'], 'coprod':['coproducto'],'int': ['integral'], 'oint': ['integral de contorno'], 'bigcap': ['intersecci&oacute;n'],'bigcup': ['uni&oacute;n'], 'bigsqcup':['Uni&oacute;n rect&aacute;ngular'], 'bigvee' :['disyunci&oacute;n'],'bigwedge' : ['conjunci&oacute;n'], 'bigodot': ['circumpunto'],'bigotimes': ['prducto tensorial'],'bigoplus': ['circumsuma'], 'biguplus': ['uni&oacute;n con suma']}


BinaryOperators ={'+':['m&aacute;s'], '-':['menos'], '*':['por'], '/':['dividido entre'], 'pm':['m&aacute;s menos'], 'mp':['menos m&aacute;s'],'setminus':['diferencia conjuntos'], 'cdot':['punto'],'times':['producto'], 'ast':['asterisco'], 'star':['estrella'], 'diamond':['operaci&oacute;n diamante'],'circ':['c&iacute;rculo'],'bullet':['c&iacute;rculo relleno'],'div':['dividido entre'],'cap': ['intersecci&oacute;n'],'cup':['uni&oacute;n'],'uplus':['uni&oacute;n con suma'],'sqcap':['intersecci&oacute;n rect&aacute;ngular'],'sqcup':['uni&oacute;n rect&aacute;ngular'],'triangleleft':['tri&aacute;angulo a la izquierda'],'triangleright':['tri&aacute;ngulo a la derecha'],'wr':['producto corona'],'bigcirc':['círculo grande'],'bigtriangleup':['tri&aacute;ngulo grande hacia arriba'],'bigtriangledown':['tri&aacute;ngulo grande hacia abajo'],'vee':['disyunci&oacute;n'],'wedge':['conjunci&oacute;n'],'oplus':['circunsuma'],'ominus':['circunresta'],'otimes':['circuncruz'],'oslash':['circunbarra'],'odot':['circunpunto'], 'dagger': ['daga'],'ddagger': ['doble daga'],'amalg':['amalgamaci&oacute;n']}

BinaryRelations ={'=':['igual'],'<':['menor'],'>':['mayor'],'leq':['menor igual'], 'geq':['mayor igual'], 'equiv':['equivalente'], 'prec':['precede'], 'succ':['sucede'], 'sim':['similar'], 'preceq':['precede igual'], 'succeq':['sucede igual'], 'simeq':['similar igual'], 'll':['mucho menor'], 'gg':['mucho mayor'], 'asymp':['asint&oacute;tico'], 'subset':['subconjunto'], 'supset':['superconjunto'], 'approx':['aproximado'], 'subseteq':['subconjunto igual'], 'supseteq':['super conjunto igual'], 'cong':['congruente'], 'sqsubseteq':['subconjunto rect&aacute;ngular'], 'sqsupseteq':['superconjunto rect&aacute;ngular'], 'bowtie':['junta'], 'in':['est&aacute; en'], 'ni':['contiene a'], 'propto':['proporcional'], 'vdash':['deduce'], 'dashv':['deducido'], 'models':['modela'],'smile':['sonrisa'], 'mid':['medio'], 'doteq':['igual puntuado'],'frown':['fruncido'], 'parallel':['paralelo'],'perp':['perpendicular'], 'neq':['no igual'], 'notin':['no est&aacute; en']}
#Función para agregar al diccionario elementos
key = ''
value = ''#Estas variables de entrada se reconocer&aacute;n posteriormente las dejo así por el momento, para probar con la GUI
#addWord(key,value) Descomentar la línea cuando la funci&oacute;n vaya a ser utulizada

#-------------------------------------------------------------------------------
#The grammar.

precedence = (	
	('left','SUP','SUB', 'FRAC','ROOT'),
)

def p_start(p):
	'''start : content
				| start content'''
	if(len(p) == 3):
		p[0] =  p[1] +p[2]
	else:
		p[0] = p[1]

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
				| command
				| content content'''
	if(len(p) == 3):
		p[0] =p[1]+p[2]
	else:
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
	p[0] =  formulate(showReading[p[1][0]])#--->Cambios importantes en las referencias


def p_command(p):
	'''command : frac
				| root
				| binop
				| binrel
				| not'''
	p[0] = p[1]

#------------------------------------------------------------------------------------------------------


#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels; tal vez que p[0] = "una función que depende de los otros p[i]".

def p_scripted(p):
	'''scripted : content SUP content
				| content SUB content '''
	if(p[2] == '^'):
		p[0] = p[1] + formulate('s&uacute;per') + p[3] + formulate('fin s&uacute;per')
	else:
		p[0] = p[1] + formulate('sub') + p[3] + formulate('fin sub')
	
def p_frac(p):
	'''frac : FRAC content content'''
	p[0] = formulate('comienza fracci&oacute;n') + p[2] + formulate('sobre') + p[3] + formulate('fin fracci&oacute;n')

def p_root(p):
	'''root : ROOT content
			| ROOT sblock content '''
	if(len(p) == 3):
		p[0] = formulate('ra&iacute;z cuadrada de') + p[2] + formulate('termina ra&iacute;z')
	else:
		p[0] = formulate('ra&iacute;z') + p[2] + formulate('de') + p[3] + formulate('termina ra&iacute;z')

def p_binOp(p):
	'''binop : BINOP
				| KBINOP '''
	p[0] = formulate(BinaryOperators[p[1][0]])

def p_binRel(p):
	'''binrel : BINREL
				| KBINREL'''
	p[0] = formulate(BinaryRelations[p[1][0]])

def p_not(p):
	'''not : NOT '''
	p[0]= formulate('no')	


def p_error(p):
	if p:
		print("Syntax error at token", p.type)
		# Just discard the token and tell the parser it's okay.
		parser.errok()
	else:
		print("Syntax error at EOF")

#-------------------------------------------------------------------------------	

parser = yacc.yacc()

def convert(String):
	return parser.parse(String)

