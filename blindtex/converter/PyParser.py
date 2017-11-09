#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
from PyLexer import tokens
#Funciones: en esta sección, dejaremos todas las funciones que se requieran
def addWord(key,value):
    global Ordinary
    if (Ordinary.get(key) is not None):
        print('Key is alredy exist')
    else:
        Ordinary[str(key)] = value

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
	return '<span aria-label=\"'+ label + '\">&nbsp;</span>'
#EndOfFunction
#--------------------------------------------------------------------------

#TODO Que esto sea una estructura de datos, con funciones para cambiar la lectura(value) con mayor facilidad.
Ordinary = {'alpha': 'alfa', 'beta': 'beta', 'gamma' : 'gamma', 'delta' : 'delta' ,'epsilon' : 'epsilon', 'varepsilon':'var epsilon' , 'zeta' : 'zeta', 'eta':'eta', 'theta' : 'teta','vartheta':'var teta', 'iota' : 'iota', 'kappa':'kappa', 'lambda':'lambda', 'mu':'mi', 'nu':'ni', 'xi':'xi', 'pi':'pi', 'varpi': 'var pi', 'rho':'ro', 'varrho': 'var ro','sigma':'sigma', 'varsigma': 'var sigma', 'tau':'tau', 'upsilon':'ipsilon', 'phi':'fi', 'varphi':'var fi', 'chi':'ji', 'psi':'psi', 'omega':'omega', 'Gamma': 'gama may&uacute;scula', 'Delta':'delta may&uacute;scula', 'Theta': 'teta may&uacute;scula', 'Lambda': 'lambda may&uacute;scula', 'Xi': 'xi may&uacute;scula', 'Pi': 'pi may&uacute;scula', 'Sigma': 'sigma may&uacute;scula', 'Upsilon': 'ipsilon may&uacute;scula', 'Phi': 'fi may&uacute;scula', 'Psi': 'psi may&uacute;scula', 'Omega': 'omega may&uacute;scula', 
			'aleph': 'alef', 'hbar': 'hache barra', 'imath': 'i caligr&aacute;fica, sin punto', 'jmath': 'j caligr&aacute;fica, sin punto', 'ell' : 'ele caligr&aacute;fica','vp': 'p caligr&aacute;fica', 'Re': 'parte real','Im': 'parte imaginaria', 'partial': 'parcial', 'infty': 'infinito','prime': 'prima','emptyset':'conjunto vac&iacute;o','nabla':'nabla','surd':'ra&iacute;z','top': 'transpuesto', 'bot': 'perpendicular','|': 'paralelo, norma', 'angle': '&aacute;ngulo', 'triangle': 'tri&aacute;ngulo','backslash': 'barra invertida', 'forall':'para todo','exists':'existe','neg': 'negaci&oacute;n', 'flat': 'bemol', 'natural':'becuadro','sharp':'sostenido','clubsuit':'trebol','diamondsuit': 'diamante','heartsuit': 'corazón','spadsuit': 'picas'}

#TODO: Acordar los nombres de algunos operadores.
LargeOperators ={'sum': 'suma','prod':'producto', 'coprod':'coproducto','int': 'integral', 'oint': 'integral de contorno', 'bigcap': 'intersecci&oacute;n','bigcup': 'uni&oacute;n', 'bigsqcup':'Uni&oacute;n rect&aacute;ngular', 'bigvee' :'disyunci&oacute;n','bigwedge' : 'conjunci&oacute;n', 'bigodot': 'circumpunto','bigotimes': 'prducto tensorial','bigoplus': 'circumsuma', 'biguplus': 'uni&oacute;n con suma'}

#Función para agregar al diccionario elementos
key = ''
value = ''#Estas variables de entrada se reconocerán posteriormente las dejo así por el momento, para probar con la GUI
#addWord(key,value) Descomentar la línea cuando la función vaya a ser utulizada


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
		p[0] = p[1] + formulate('sup &iacute;ndice') + p[3] + formulate('fin sup &iacute;ndice')
	else:
		p[0] = p[1] + formulate('sub &iacute;ndice') + p[3] + formulate('fin sub &iacute;ndice')
	
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

