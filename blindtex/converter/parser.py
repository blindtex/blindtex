#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
#from ply import yacc
from dictionary import *
#from dictionary import *
from lexer import tokens

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
	return '<span aria-label=\"'+ label + '\">&nbsp</span>'
#EndOfFunction
#--------------------------------------------------------------------------




#TODO Que esto sea una estructura de datos, con funciones para cambiar la lectura(value) con mayor facilidad.

#dictionary LargeOperators(LagrgeOperator) = new...
#LargeOperators.Fun...

#TODO: Acordar los nombres de algunos operadores.

Ordinary = {'alpha': ['alfa'], 'beta': ['beta'], 'gamma' : ['gamma'], 'delta' : ['delta'] ,'epsilon' : ['epsilon'], 'varepsilon':['var epsilon'] , 'zeta' : ['zeta'],
            'eta':['eta'], 'theta' : ['teta'],'vartheta':['var teta'], 'iota' : ['iota'], 'kappa':['kappa'], 'lambda':['lambda'], 'mu':['mi'], 'nu':['ni'], 'xi':['xi'],
            'pi':['pi'], 'varpi': ['var pi'], 'rho':['ro'], 'varrho': ['var ro'],'sigma':['sigma'], 'varsigma': ['var sigma'], 'tau':['tau'], 'upsilon':['ipsilon'],
            'phi':['fi'], 'varphi':['var fi'], 'chi':['ji'], 'psi':['psi'], 'omega':['omega'], 'Gamma': ['gama may&uacute;scula'], 'Delta':['delta may&uacute;scula'],
            'Theta': ['teta may&uacute;scula'], 'Lambda': ['lambda may&uacute;scula'], 'Xi': ['xi may&uacute;scula'], 'Pi': ['pi may&uacute;scula'],
            'Sigma': ['sigma may&uacute;scula'], 'Upsilon': ['ipsilon may&uacute;scula'], 'Phi': ['fi may&uacute;scula'], 'Psi': ['psi may&uacute;scula'],
            'Omega': ['omega may&uacute;scula'],'aleph': ['alef'], 'hbar': ['hache barra'], 'imath': ['i caligr&aacute;fica, sin punto'],
            'jmath': ['j caligr&aacute;fica, sin punto'], 'ell' : ['ele caligr&aacute;fica'],'vp': ['p caligr&aacute;fica'], 'Re': ['parte real'],
            'Im': ['parte imaginaria'], 'partial': ['parcial'], 'infty': ['infinito'],'prime': ['prima'],'emptyset':['conjunto vac&iacute;o'],'nabla':['nabla'],
            'surd':['ra&iacute;z'],'top': ['transpuesto'], 'bot': ['perpendicular'],'|': ['paralelo, norma'], 'angle': ['&aacute;ngulo'],
            'triangle': ['tri&aacute;ngulo'],'backslash': ['barra invertida'], 'forall':['para todo'],'exists':['existe'],'neg': ['negaci&oacute;n'],
            'flat': ['bemol'], 'natural':['becuadro'],'sharp':['sostenido'],'clubsuit':['trebol'],'diamondsuit': ['diamante'],'heartsuit': ['corazón'],'spadsuit': ['picas'], 'lnot':['negaci&oacute;n']}

LargeOperators ={'sum': ['suma'],'prod':['producto'], 'coprod':['coproducto'],'int': ['integral'], 'oint': ['integral de contorno'], 'bigcap': ['intersecci&oacute;n'],'bigcup': ['uni&oacute;n'], 'bigsqcup':['Uni&oacute;n rect&aacute;ngular'], 'bigvee' :['disyunci&oacute;n'],'bigwedge' : ['conjunci&oacute;n'], 'bigodot': ['circumpunto'],'bigotimes': ['prducto tensorial'],'bigoplus': ['circumsuma'], 'biguplus': ['uni&oacute;n con suma']}


BinaryOperators ={'+':['m&aacute;s'], '-':['menos'], '*':['por'], '/':['dividido entre'], 'pm':['m&aacute;s menos'], 'mp':['menos m&aacute;s'],'setminus':['diferencia conjuntos'], 'cdot':['punto'],'times':['producto'], 'ast':['asterisco'], 'star':['estrella'], 'diamond':['operaci&oacute;n diamante'],'circ':['c&iacute;rculo'],'bullet':['c&iacute;rculo relleno'],'div':['dividido entre'],'cap': ['intersecci&oacute;n'],'cup':['uni&oacute;n'],'uplus':['uni&oacute;n con suma'],'sqcap':['intersecci&oacute;n rect&aacute;ngular'],'sqcup':['uni&oacute;n rect&aacute;ngular'],'triangleleft':['tri&aacute;angulo a la izquierda'],'triangleright':['tri&aacute;ngulo a la derecha'],'wr':['producto corona'],'bigcirc':['círculo grande'],'bigtriangleup':['tri&aacute;ngulo grande hacia arriba'],'bigtriangledown':['tri&aacute;ngulo grande hacia abajo'],'vee':['disyunci&oacute;n'],'wedge':['conjunci&oacute;n'],'oplus':['circunsuma'],'ominus':['circunresta'],'otimes':['circuncruz'],'oslash':['circunbarra'],'odot':['circunpunto'], 'dagger': ['daga'],'ddagger': ['doble daga'],'amalg':['amalgamaci&oacute;n'],'lor':['disyunci&oacute;n'],'land':['conjunci&oacute;n']}

BinaryRelations ={'=':['igual'],'<':['menor'],'>':['mayor'],'leq':['menor igual'], 'geq':['mayor igual'], 'equiv':['equivalente'], 'prec':['precede'], 'succ':['sucede'], 'sim':['similar'], 'preceq':['precede igual'], 'succeq':['sucede igual'], 'simeq':['similar igual'], 'll':['mucho menor'], 'gg':['mucho mayor'], 'asymp':['asint&oacute;tico'], 'subset':['subconjunto'], 'supset':['superconjunto'], 'approx':['aproximado'], 'subseteq':['subconjunto igual'], 'supseteq':['super conjunto igual'], 'cong':['congruente'], 'sqsubseteq':['subconjunto rect&aacute;ngular'], 'sqsupseteq':['superconjunto rect&aacute;ngular'], 'bowtie':['junta'], 'in':['est&aacute; en'], 'ni':['contiene a'], 'propto':['proporcional'], 'vdash':['deduce'], 'dashv':['deducido'], 'models':['modela'],'smile':['sonrisa'], 'mid':['medio'], 'doteq':['igual puntuado'],'frown':['fruncido'], 'parallel':['paralelo'],'perp':['perpendicular'], 'neq':['no igual'], 'notin':['no est&aacute; en'], 'ne':['no igual'],'le':['menor igual'],'ge':['mayor igula'],'owns':['contiene']}

MathFunctions ={'arccos':['arco coseno'], 'arcsin':['arco seno'], 'arctan':['arco tangente'], 'arg':['argumento'], 'cos':['coseno'], 'cosh':['coseno hiperb&oacute;lico'], 'cot':['cotangente'], 'coth':['cotangente hiperb&oacute;lico'], 'csc':['cosecante'], 'deg':['grado'], 'det':['determinante'], 'dim':['dimenci&oacute;n'], 'exp':['exponencial'], 'gcd':['mayor com&uacute;n divisor'], 'hom':['homomorfismo'], 'inf':['infimo'], 'ker':['n&uacute;cleo'], 'lg':['logaritmo binario'], 'liminf':['lim inf'], 'limsup':['lim sup'], 'ln':['logaritmo natural'], 'log':['logaritmo'], 'max':['m&aacute;ximo'], 'min':['mi&iacute;nimo'], 'Pr':['probabilidad'], 'sec':['secante'], 'sin':['seno'], 'sinh':['seno hiperb&oacute;lico'], 'sup':['supremo'], 'tan':['tangente'], 'tanh':['tangente hiperb&oacute;lico']}

Arrows ={'leftarrow':['flecha izquierda'], 'Leftarrow':['flecha izquierda doble'], 'rightarrow':['flecha derecha'], 'Rightarrow':['flecha derecha doble'], 'leftrightarrow':['flecha izquierda derecha'], 'Leftrightarrow':['flecha izquierda derecha doble'], 'mapsto':['env&iacute;a'], 'hookleftarrow':['flecha  garfio izquierda'], 'leftharpoonup':['arp&oacute;n arriba izquierdo'], 'leftharpoondown':['arp&oacute;n abajo izquierda'], 'rightleftharpoons':['arp&oacute;n izquierda derecha'], 'longleftarrow':['flecha izquierda larga'], 'Longleftarrow':['flecha izquierda doble larga'], 'longrightarrow':['flecha derecha larga'], 'Longrightarrow':['flecha derecha doble larga'], 'longleftrightarrow':['flecha izquierda derecha larga'], 'Longleftrightarrow':['flecha izquierda derecha doble larga'], 'longmapsto':['env&iacute;a largo'], 'hookrightarrow':['flecha garfio derecha'], 'rightharpoonup':['arp&oacute;n arriba derecho'], 'rightharpoondown':['arp&acute;n abajo derecho'], 'uparrow':['flecha arriba'], 'Uparrow':['flecha arriba doble'], 'downarrow':['flecha abajo'], 'Downarrow':['flecha abajo doble'], 'updownarrow':['flecha arriba abajo'], 'Updownarrow':['flecha arriba abajo doble'], 'nearrow':['flecha diagonal arriba derecha'], 'searrow':['flecha diagonal abajo derecha'], 'swarrow':['flecha diagonal abajo izquierda'], 'nwarrow':['flecha diagonal arriba izquierda'],'to':['hacia'],'gets':['obtiene'],'iff':['si y solo si']}

Delimiters ={'(':['abre par&eacute;ntesis'],')':['cierra par&eacute;ntesis'],'[':['abre corchete'],']':['cierra corchete'], '{':['abre llave'],'}':['cierra llave'], 'lfloor':['abre piso'],'rfloor':['cierra piso'], 'lceil':['abre techo'], 'rceil':['cierra techo'],'langle':[' abre &aacute;ngulo'],'rangle':['cierra &aacute;ngulo'],'backslash':['barra invertida']}

Accents ={'hat':['gorro'],'check':['anticircunflejo'],'breve':['breve'],'acute':['agudo'],'grave':['grave'],'tilde':['virgulilla'],'bar':['barra'], 'vec':['vecctor'],'dot':['punto'],'ddot':['doble punto'],'widehat':['gorro'],'widetilde':['virgulilla']}

Styles ={'mathit':['it&aacute;lica'],'mathrm':['roman'],'mathbf':['negrilla'],'mathsf':['sans serif'],'mathtt':['m&aacute;quina escribir'], 'mathcal':['caligr&aacute;fica'], 'boldmath':['negrilla']}

Dots ={'dots':['puntos'],'ldots':['puntos bajos'],'cdots':['puntos centrados'],'vdots':['puntos verticales'],'ddots':['puntos diagonales']}
#Función para agregar al diccionario elementos
key = ''
value = ''#Estas variables de entrada se reconocer&aacute;n posteriormente las dejo así por el momento, para probar con la GUI
#addWord(key,value) Descomentar la línea cuando la funci&oacute;n vaya a ser utulizada

#-------------------------------------------------------------------------------
#The grammar.

precedence = (
	('left','SUP','SUB', 'FRAC','ROOT'),
	('right', 'LARGEOP')	
)

def p_start(p):
	'''start : content
				| start content'''
	if(len(p) == 3):
		p[0] =  p[1] +p[2]
	else:
		p[0] = p[1]

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
	'''chars : char
				| char chars '''
	if(len(p) == 3):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1]

def p_char(p):
	'''char : CHAR
			| ord '''
	p[0] = p[1]

def p_ord(p):
	'''ord : ORD '''
	p[0] =  formulate(Ordinary[p[1]][0])#--->Cambios importantes en las referencias


def p_command(p):
	'''command : frac
				| root
				| binop
				| binrel
				| not
				| function
				| larop
				| arrow
				| delimiter
				| accent
				| style
				| dots
				| lim
				| unknown'''
	p[0] = p[1]

#------------------------------------------------------------------------------------------------------


#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels; tal vez que p[0] = "una función que depende de los otros p[i]".

def p_scripted(p):
	'''scripted : char SUP char
					| char SUP block
					| block SUP char
					| block SUP block
					| char SUB char
					| char SUB block
					| block SUB char
					| block SUB block'''
	if(p[2] == '^'):
		p[0] = p[1] + formulate('s&uacute;per') + p[3] + formulate('fin s&uacute;per')
	else:
		p[0] = p[1] + formulate('sub') + p[3] + formulate('fin sub')
			
def p_compScripted(p):
	'''scripted : char SUP char SUB char
					| char SUP char SUB block
					| char SUP block SUB char
					| char SUP block SUB block
					| block SUP char SUB char
					| block SUP char SUB block
					| block SUP block SUB char
					| block SUP block SUB block
					| char SUB char SUP char
					| char SUB char SUP block
					| char SUB block SUP char
					| char SUB block SUP block
					| block SUB char SUP char
					| block SUB char SUP block
					| block SUB block SUP char
					| block SUB block SUP block'''
	if(p[2] =='^'):
		p[0] =  p[1] + formulate('s&uacute;per') + p[3] + formulate('fin s&uacute;per') + formulate('sub') + p[5] + formulate('fin sub')
	else:
		p[0] = p[1] + formulate('sub') + p[3] + formulate('fin sub') + formulate('s&uacute;per') + p[5] + formulate('fin s&uacute;per')
		
def p_frac(p):
	'''frac : FRAC char char
				| FRAC char block
				| FRAC block char
				| FRAC block block'''
	p[0] = formulate('comienza fracci&oacute;n') + p[2] + formulate('sobre') + p[3] + formulate('fin fracci&oacute;n')

def p_root(p):
	'''root : ROOT char
			| ROOT block
			| ROOT KDELIMITER content KDELIMITER char
			| ROOT KDELIMITER content KDELIMITER block '''
	if(len(p) == 3):
		p[0] = formulate('ra&iacute;z cuadrada de') + p[2] + formulate('termina ra&iacute;z')
	else:
		p[0] = formulate('ra&iacute;z') + p[3] + formulate('de') + p[5] + formulate('termina ra&iacute;z')

def p_binOp(p):
	'''binop : BINOP
				| KBINOP '''
	p[0] = formulate(BinaryOperators[p[1]][0])

def p_binRel(p):
	'''binrel : BINREL
				| KBINREL'''
	p[0] = formulate(BinaryRelations[p[1]][0])

def p_not(p):
	'''not : NOT '''
	p[0]= formulate('no')	

def p_function(p):
	'''function : FUNC '''
	p[0] = formulate(MathFunctions[p[1]][0])

def p_comLargeOp(p):
	'''larop : LARGEOP SUB char SUP char
				| LARGEOP SUB char SUP block
				| LARGEOP SUB block SUP char
				| LARGEOP SUB block SUP block
				| LARGEOP SUP char SUB char
				| LARGEOP SUP char SUB block
				| LARGEOP SUP block SUB char
				| LARGEOP SUP block SUB block'''
	if(p[2] =='_'):
		p[0] = formulate(LargeOperators[p[1]][0] + ' desde') + p[3] + formulate('hasta') + p[5] + formulate('de')
	else:
		p[0] = formulate(LargeOperators[p[1]][0] + ' desde') + p[5] + formulate('hasta') + p[3] + formulate('de')

def p_largeOp(p):
	'''larop : LARGEOP
				| LARGEOP SUB char
				| LARGEOP SUB block'''
	if(len(p)==2):
		p[0]= formulate(LargeOperators[p[1]][0] +' de')
	elif(len(p)==4):
		p[0] = formulate(LargeOperators[p[1]][0] +' sobre') + p[3] + formulate('de')

def p_arrow(p):
	'''arrow : ARROW'''
	p[0] = formulate(Arrows[p[1]][0])

def p_delimiter(p):
	'''delimiter : DELIMITER
					| KDELIMITER '''
	p[0] = formulate(Delimiters[p[1]][0])

def p_simpleAccent(p):
	'''accent : ACCENT char'''
	p[0] = p[2] + formulate(Accents[p[1]][0])

def p_complexAccent(p):
	'''accent : ACCENT block'''
	if(len(p[2]) > 3):
		p[0] = formulate(Accents[p[1]][0]) + p[2] + formulate('fin ' + Accents[p[1]][0])
	else:
		p[0] = p[2] + formulate(Accents[p[1]][0])

def p_style(p):
	'''style : STYLE char
				| STYLE block '''
	p[0] = formulate(Styles[p[1]][0]) + p[2] + formulate('fin ' + Styles[p[1]][0])

def p_dots(p):
	'''dots : DOTS '''
	p[0] = formulate(Dots[p[1]][0])

def p_lim(p):
	'''lim : LIM
			| LIM SUB char
			| LIM SUB block '''
	if(len(p) == 4):
		p[0] = formulate('l&iacute;mite cuando') + p[3] + formulate('de')
	else:
		p[0] = formulate('l&iacute;mite de')

def p_unknown(p):
	'''unknown : UNKNOWN'''
	p[0] = formulate(p[1])
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

