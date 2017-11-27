#-*-:coding:utf-8-*-
#Parser
#This file is  just for user tests. It will  be not used in the final code. 

import ply.yacc as yacc
#from ply import yacc
#from blindtex.converter.dictionary import *
from dictionary import *
#from blindtex.converter.lexer import *
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
	return label + ' '
#EndOfFunction
#--------------------------------------------------------------------------




#TODO Que esto sea una estructura de datos, con funciones para cambiar la lectura(value) con mayor facilidad.

#dictionary LargeOperators(LagrgeOperator) = new...
#LargeOperators.Fun...

#TODO: Acordar los nombres de algunos operadores.

Ordinary = {'alpha': [0,['alfa']], 'beta': [0,['beta']], 'gamma' : [0,['gamma']], 'delta' : [0,['delta']] ,'epsilon' : [0,['epsilon']], 'varepsilon':[0,['var epsilon']] , 'zeta' : [0,['zeta']],
            'eta':[0,['eta']], 'theta' : [0,['teta']],'vartheta':[0,['var teta']], 'iota' : [0,['iota']], 'kappa':[0,['kappa']], 'lambda':[0,['lambda']], 'mu':[0,['mi']], 'nu':[0,['ni']], 'xi':[0,['xi']],
            'pi':[0,['pi']], 'varpi': [0,['var pi']], 'rho':[0,['ro']], 'varrho': [0,['var ro']],'sigma':[0,['sigma']], 'varsigma': [0,['var sigma']], 'tau':[0,['tau']], 'upsilon':[0,['ipsilon']],
            'phi':[0,['fi']], 'varphi':[0,['var fi']], 'chi':[0,['ji']], 'psi':[0,['psi']], 'omega':[0,['omega']], 'Gamma': [0,['gama mayúscula']], 'Delta':[0,['delta mayúscula']],
            'Theta': [0,['teta mayúscula']], 'Lambda': [0,['lambda mayúscula']], 'Xi': [0,['xi mayúscula']], 'Pi': [0,['pi mayúscula']],
            'Sigma': [0,['sigma mayúscula']], 'Upsilon': [0,['ipsilon mayúscula']], 'Phi': [0,['fi mayúscula']], 'Psi': [0,['psi mayúscula']],
            'Omega': [0,['omega mayúscula']],'aleph': [0,['alef']], 'hbar': [0,['hache barra']], 'imath': [0,['i caligráfica, sin punto']],
            'jmath': [0,['j caligráfica, sin punto']], 'ell' : [0,['ele caligráfica']],'vp': [0,['p caligráfica']], 'Re': [0,['parte real']],
            'Im': [0,['parte imaginaria']], 'partial': [0,['parcial']], 'infty': [0,['infinito']],'prime': [0,['prima']],'emptyset':[0,['conjunto vacío']],'nabla':[0,['nabla']],
            'surd':[0,['raíz']],'top': [0,['transpuesto']], 'bot': [0,['perpendicular']],'|': [0,['paralelo, norma']], 'angle': [0,['ángulo']],
            'triangle': [0,['triángulo']],'backslash': [0,['barra invertida']], 'forall':[0,['para todo']],'exists':[0,['existe']],'neg': [0,['negación']],
            'flat': [0,['bemol']], 'natural':[0,['becuadro']],'sharp':[0,['sostenido']],'clubsuit':[0,['trebol']],'diamondsuit': [0,['diamante']],'heartsuit': [0,['corazón']],'spadsuit': [0,['picas']], 'lnot':[0,['negación']]}

LargeOperators ={'sum': [0,['suma']],'prod':[0,['producto']], 'coprod':[0,['coproducto']],'int': [0,['integral']], 'oint': [0,['integral de contorno']], 'bigcap': [0,['intersección']],'bigcup': [0,['unión']], 'bigsqcup':[0,['Unión rectángular']], 'bigvee' :[0,['disyunción']],'bigwedge' : [0,['conjunción']], 'bigodot': [0,['circumpunto']],'bigotimes': [0,['prducto tensorial']],'bigoplus': [0,['circumsuma']], 'biguplus': [0,['unión con suma']]}


BinaryOperators ={'+':[0,['más']], '-':[0,['menos']], '*':[0,['por']], '/':[0,['dividido entre']], 'pm':[0,['más menos']], 'mp':[0,['menos más']],'setminus':[0,['diferencia conjuntos']], 'cdot':[0,['punto']],'times':[0,['producto']], 'ast':[0,['asterisco']], 'star':[0,['estrella']], 'diamond':[0,['operación diamante']],'circ':[0,['círculo']],'bullet':[0,['círculo relleno']],'div':[0,['dividido entre']],'cap': [0,['intersección']],'cup':[0,['unión']],'uplus':[0,['unión con suma']],'sqcap':[0,['intersección rectángular']],'sqcup':[0,['unión rectángular']],'triangleleft':[0,['triáangulo a la izquierda']],'triangleright':[0,['triángulo a la derecha']],'wr':[0,['producto corona']],'bigcirc':[0,['círculo grande']],'bigtriangleup':[0,['triángulo grande hacia arriba']],'bigtriangledown':[0,['triángulo grande hacia abajo']],'vee':[0,['disyunción']],'wedge':[0,['conjunción']],'oplus':[0,['circunsuma']],'ominus':[0,['circunresta']],'otimes':[0,['circuncruz']],'oslash':[0,['circunbarra']],'odot':[0,['circunpunto']], 'dagger': [0,['daga']],'ddagger': [0,['doble daga']],'amalg':[0,['amalgamación']],'lor':[0,['disyunción']],'land':[0,['conjunción']]}

BinaryRelations ={'=':[0,['igual']],'<':[0,['menor']],'>':[0,['mayor']],'leq':[0,['menor igual']], 'geq':[0,['mayor igual']], 'equiv':[0,['equivalente']], 'prec':[0,['precede']], 'succ':[0,['sucede']], 'sim':[0,['similar']], 'preceq':[0,['precede igual']], 'succeq':[0,['sucede igual']], 'simeq':[0,['similar igual']], 'll':[0,['mucho menor']], 'gg':[0,['mucho mayor']], 'asymp':[0,['asintótico']], 'subset':[0,['subconjunto']], 'supset':[0,['superconjunto']], 'approx':[0,['aproximado']], 'subseteq':[0,['subconjunto igual']], 'supseteq':[0,['super conjunto igual']], 'cong':[0,['congruente']], 'sqsubseteq':[0,['subconjunto rectángular']], 'sqsupseteq':[0,['superconjunto rectángular']], 'bowtie':[0,['junta']], 'in':[0,['está en']], 'ni':[0,['contiene a']], 'propto':[0,['proporcional']], 'vdash':[0,['deduce']], 'dashv':[0,['deducido']], 'models':[0,['modela']],'smile':[0,['sonrisa']], 'mid':[0,['medio']], 'doteq':[0,['igual puntuado']],'frown':[0,['fruncido']], 'parallel':[0,['paralelo']],'perp':[0,['perpendicular']], 'neq':[0,['no igual']], 'notin':[0,['no está en']], 'ne':[0,['no igual']],'le':[0,['menor igual']],'ge':[0,['mayor igula']],'owns':[0,['contiene']]}

MathFunctions ={'arccos':[0,['arco coseno']], 'arcsin':[0,['arco seno']], 'arctan':[0,['arco tangente']], 'arg':[0,['argumento']], 'cos':[0,['coseno']], 'cosh':[0,['coseno hiperbólico']], 'cot':[0,['cotangente']], 'coth':[0,['cotangente hiperbólico']], 'csc':[0,['cosecante']], 'deg':[0,['grado']], 'det':[0,['determinante']], 'dim':[0,['dimención']], 'exp':[0,['exponencial']], 'gcd':[0,['mayor común divisor']], 'hom':[0,['homomorfismo']], 'inf':[0,['infimo']], 'ker':[0,['núcleo']], 'lg':[0,['logaritmo binario']], 'liminf':[0,['lim inf']], 'limsup':[0,['lim sup']], 'ln':[0,['logaritmo natural']], 'log':[0,['logaritmo']], 'max':[0,['máximo']], 'min':[0,['miínimo']], 'Pr':[0,['probabilidad']], 'sec':[0,['secante']], 'sin':[0,['seno']], 'sinh':[0,['seno hiperbólico']], 'sup':[0,['supremo']], 'tan':[0,['tangente']], 'tanh':[0,['tangente hiperbólico']]}

Arrows ={'leftarrow':[0,['flecha izquierda']], 'Leftarrow':[0,['flecha izquierda doble']], 'rightarrow':[0,['flecha derecha']], 'Rightarrow':[0,['flecha derecha doble']], 'leftrightarrow':[0,['flecha izquierda derecha']], 'Leftrightarrow':[0,['flecha izquierda derecha doble']], 'mapsto':[0,['envía']], 'hookleftarrow':[0,['flecha  garfio izquierda']], 'leftharpoonup':[0,['arpón arriba izquierdo']], 'leftharpoondown':[0,['arpón abajo izquierda']], 'rightleftharpoons':[0,['arpón izquierda derecha']], 'longleftarrow':[0,['flecha izquierda larga']], 'Longleftarrow':[0,['flecha izquierda doble larga']], 'longrightarrow':[0,['flecha derecha larga']], 'Longrightarrow':[0,['flecha derecha doble larga']], 'longleftrightarrow':[0,['flecha izquierda derecha larga']], 'Longleftrightarrow':[0,['flecha izquierda derecha doble larga']], 'longmapsto':[0,['envía largo']], 'hookrightarrow':[0,['flecha garfio derecha']], 'rightharpoonup':[0,['arpón arriba derecho']], 'rightharpoondown':[0,['arp&acute;n abajo derecho']], 'uparrow':[0,['flecha arriba']], 'Uparrow':[0,['flecha arriba doble']], 'downarrow':[0,['flecha abajo']], 'Downarrow':[0,['flecha abajo doble']], 'updownarrow':[0,['flecha arriba abajo']], 'Updownarrow':[0,['flecha arriba abajo doble']], 'nearrow':[0,['flecha diagonal arriba derecha']], 'searrow':[0,['flecha diagonal abajo derecha']], 'swarrow':[0,['flecha diagonal abajo izquierda']], 'nwarrow':[0,['flecha diagonal arriba izquierda']],'to':[0,['hacia']],'gets':[0,['obtiene']],'iff':[0,['si y solo si']]}

Delimiters ={'(':[0,['abre paréntesis']],')':[0,['cierra paréntesis']],'[':[0,['abre corchete']],']':[0,['cierra corchete']], '{':[0,['abre llave']],'}':[0,['cierra llave']], 'lfloor':[0,['abre piso']],'rfloor':[0,['cierra piso']], 'lceil':[0,['abre techo']], 'rceil':[0,['cierra techo']],'langle':[0,[' abre ángulo']],'rangle':[0,['cierra ángulo']],'backslash':[0,['barra invertida']]}

Accents ={'hat':[0,['gorro']],'check':[0,['anticircunflejo']],'breve':[0,['breve']],'acute':[0,['agudo']],'grave':[0,['grave']],'tilde':[0,['virgulilla']],'bar':[0,['barra']], 'vec':[0,['vecctor']],'dot':[0,['punto']],'ddot':[0,['doble punto']],'widehat':[0,['gorro']],'widetilde':[0,['virgulilla']]}

Styles ={'mathit':[0,['itálica']],'mathrm':[0,['roman']],'mathbf':[0,['negrilla']],'mathsf':[0,['sans serif']],'mathtt':[0,['máquina escribir']], 'mathcal':[0,['caligráfica']], 'boldmath':[0,['negrilla']]}

Dots ={'dots':[0,['puntos']],'ldots':[0,['puntos bajos']],'cdots':[0,['puntos centrados']],'vdots':[0,['puntos verticales']],'ddots':[0,['puntos diagonales']]}
#Función para agregar al diccionario elementos
key = ''
value = ''#Estas variables de entrada se reconocerán posteriormente las dejo así por el momento, para probar con la GUI
#addWord(key,value) Descomentar la línea cuando la función vaya a ser utulizada
#TODO: Lista de objetos diccionario:
dOrdinary = dictionary(Ordinary)
dLargeOperators = dictionary(LargeOperators)
dBinaryOperators = dictionary(BinaryOperators)
dBinaryRelations = dictionary(BinaryRelations)
dMathFunctions = dictionary(MathFunctions)
dArrows = dictionary(Arrows)
dDelimiters = dictionary(Delimiters)
dAccents = dictionary(Accents)
dStyles = dictionary(Styles)
dDots = dictionary(Dots)
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
		p[0] =  p[1] + p[2]
	else:
		p[0] = p[1]

def p_block(p):
	'''block : BEGINBLOCK content ENDBLOCK'''
	p[0] = p[2]

def p_content(p):
	'''content : char
				| block
				| scripted
				| command
				| content content'''
	if(len(p) == 3):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1]
	

def p_char(p):
	'''char : CHAR
			| ord'''
	p[0] = p[1] + ' '

def p_ord(p):
	'''ord : ORD '''
	p[0] =  formulate(dOrdinary.showReading(p[1],0))#--->Los operadores son la llave y el valor por defecto que esté en la lectura


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
		p[0] = p[1] + formulate('súper') + p[3] + formulate('fin súper')
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
		p[0] =  p[1] + formulate('súper') + p[3] + formulate('fin súper') + formulate('sub') + p[5] + formulate('fin sub')
	else:
		p[0] = p[1] + formulate('sub') + p[3] + formulate('fin sub') + formulate('súper') + p[5] + formulate('fin súper')
		
def p_frac(p):
	'''frac : FRAC char char
				| FRAC char block
				| FRAC block char
				| FRAC block block'''
	p[0] = formulate('comienza fracción') + p[2] + formulate('sobre') + p[3] + formulate('fin fracción')

def p_root(p):
	'''root : ROOT char
			| ROOT block
			| ROOT KDELIMITER content KDELIMITER char
			| ROOT KDELIMITER content KDELIMITER block '''
	if(len(p) == 3):
		p[0] = formulate('raíz cuadrada de') + p[2] + formulate('termina raíz')
	else:
		p[0] = formulate('raíz') + p[3] + formulate('de') + p[5] + formulate('termina raíz')

def p_binOp(p):
	'''binop : BINOP
				| KBINOP '''
	p[0] = formulate(dBinaryOperators.showReading(p[1],0))

def p_binRel(p):
	'''binrel : BINREL
				| KBINREL'''
	p[0] = formulate(dBinaryRelations.showReading(p[1],0))

def p_not(p):
	'''not : NOT '''
	p[0]= formulate('no')	

def p_function(p):
	'''function : FUNC '''
	p[0] = formulate(dMathFunctions.showReading(p[1],0))

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
		p[0] = formulate(dLargeOperators.showReading(p[1],0) + ' desde') + p[3] + formulate('hasta') + p[5] + formulate('de')
	else:
		p[0] = formulate(dLargeOperators.showReading(p[1],0) + ' desde') + p[5] + formulate('hasta') + p[3] + formulate('de')

def p_largeOp(p):
	'''larop : LARGEOP
				| LARGEOP SUB char
				| LARGEOP SUB block'''
	if(len(p)==2):
		p[0]= formulate(dLargeOperators.showReading(p[1],0) +' de')
	elif(len(p)==4):
		p[0] = formulate(dLargeOperators.showReading(p[1],0) +' sobre') + p[3] + formulate('de')

def p_arrow(p):
	'''arrow : ARROW'''
	p[0] = formulate(dArrows.showReading(p[1],0))

def p_delimiter(p):
	'''delimiter : DELIMITER
					| KDELIMITER '''
	p[0] = formulate(dDelimiters.showReading(p[1],0))

def p_simpleAccent(p):
	'''accent : ACCENT char'''
	p[0] = p[2] + formulate(dAccents.showReading(p[1],0))

def p_complexAccent(p):
	'''accent : ACCENT block'''
	if(len(p[2]) > 3):
		p[0] = formulate(dAccents.showReading(p[1],0)) + p[2] + formulate('fin ' + dAccents.showReading(p[1],0))
	else:
		p[0] = p[2] + formulate(dAccents.showReading(p[1],0))

def p_style(p):
	'''style : STYLE char
				| STYLE block '''
	p[0] = formulate(dStyles.showReading(p[1],0)) + p[2] + formulate('fin ' + dStyles.showReading(p[1],0))

def p_dots(p):
	'''dots : DOTS '''
	p[0] = formulate(dDots.showReading(p[1],0))

def p_lim(p):
	'''lim : LIM
			| LIM SUB char
			| LIM SUB block '''
	if(len(p) == 4):
		p[0] = formulate('límite cuando') + p[3] + formulate('de')
	else:
		p[0] = formulate('límite de')

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

