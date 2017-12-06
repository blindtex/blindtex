#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
#from ply import yacc
#from blindtex.converter.dictionary import *
from dictionary import *
#from blindtex.converter.lexer import *
from lexer import tokens
import formulate

#Funciones: en esta sección, dejaremos todas las funciones que se requieran



#--------------------------------------------------------------------------





Ordinary = {'alpha': [0,['alfa']], 'beta': [0,['beta']], 'gamma' : [0,['gamma']], 'delta' : [0,['delta']] ,'epsilon' : [0,['epsilon']], 'varepsilon':[0,['var epsilon']] , 'zeta' : [0,['zeta']],
            'eta':[0,['eta']], 'theta' : [0,['teta']],'vartheta':[0,['var teta']], 'iota' : [0,['iota']], 'kappa':[0,['kappa']], 'lambda':[0,['lambda']], 'mu':[0,['mi']], 'nu':[0,['ni']], 'xi':[0,['xi']],
            'pi':[0,['pi']], 'varpi': [0,['var pi']], 'rho':[0,['ro']], 'varrho': [0,['var ro']],'sigma':[0,['sigma']], 'varsigma': [0,['var sigma']], 'tau':[0,['tau']], 'upsilon':[0,['ipsilon']],
            'phi':[0,['fi']], 'varphi':[0,['var fi']], 'chi':[0,['ji']], 'psi':[0,['psi']], 'omega':[0,['omega']], 'Gamma': [0,['gama may&uacute;scula']], 'Delta':[0,['delta may&uacute;scula']],
            'Theta': [0,['teta may&uacute;scula']], 'Lambda': [0,['lambda may&uacute;scula']], 'Xi': [0,['xi may&uacute;scula']], 'Pi': [0,['pi may&uacute;scula']],
            'Sigma': [0,['sigma may&uacute;scula']], 'Upsilon': [0,['ipsilon may&uacute;scula']], 'Phi': [0,['fi may&uacute;scula']], 'Psi': [0,['psi may&uacute;scula']],
            'Omega': [0,['omega may&uacute;scula']],'aleph': [0,['alef']], 'hbar': [0,['hache barra']], 'imath': [0,['i caligr&aacute;fica, sin punto']],
            'jmath': [0,['j caligr&aacute;fica, sin punto']], 'ell' : [0,['ele caligr&aacute;fica']],'vp': [0,['p caligr&aacute;fica']], 'Re': [0,['parte real']],
            'Im': [0,['parte imaginaria']], 'partial': [0,['parcial']], 'infty': [0,['infinito']],'prime': [0,['prima']],'emptyset':[0,['conjunto vac&iacute;o']],'nabla':[0,['nabla']],
            'surd':[0,['ra&iacute;z']],'top': [0,['transpuesto']], 'bot': [0,['perpendicular']],'|': [0,['paralelo, norma']], 'angle': [0,['&aacute;ngulo']],
            'triangle': [0,['tri&aacute;ngulo']],'backslash': [0,['barra invertida']], 'forall':[0,['para todo']],'exists':[0,['existe']],'neg': [0,['negaci&oacute;n']],
            'flat': [0,['bemol']], 'natural':[0,['becuadro']],'sharp':[0,['sostenido']],'clubsuit':[0,['trebol']],'diamondsuit': [0,['diamante']],'heartsuit': [0,['coraz&oacute;n']],'spadsuit': [0,['picas']], 'lnot':[0,['negaci&oacute;n']], 'prime':[0,['prima']]}

LargeOperators ={'sum': [0,['suma']],'prod':[0,['producto']], 'coprod':[0,['coproducto']],'int': [0,['integral']], 'oint': [0,['integral de contorno']], 'bigcap': [0,['intersecci&oacute;n']],'bigcup': [0,['uni&oacute;n']], 'bigsqcup':[0,['Uni&oacute;n rect&aacute;ngular']], 'bigvee' :[0,['disyunci&oacute;n']],'bigwedge' : [0,['conjunci&oacute;n']], 'bigodot': [0,['circumpunto']],'bigotimes': [0,['prducto tensorial']],'bigoplus': [0,['circumsuma']], 'biguplus': [0,['uni&oacute;n con suma']], 'iint': [0,['doble integral']], 'iiint': [0,['triple integral']], 'iiiint': [0,['cuadruple integral']], 'idotsint': [0,['multiples integrales']], 'limits':[0,['']]}


BinaryOperators ={'+':[0,['m&aacute;s']], '-':[0,['menos']], '*':[0,['por']], '/':[0,['dividido entre']], 'pm':[0,['m&aacute;s menos']], 'mp':[0,['menos m&aacute;s']],'setminus':[0,['diferencia conjuntos']], 'cdot':[0,['punto']],'times':[0,['producto']], 'ast':[0,['asterisco']], 'star':[0,['estrella']], 'diamond':[0,['operaci&oacute;n diamante']],'circ':[0,['c&iacute;rculo']],'bullet':[0,['c&iacute;rculo relleno']],'div':[0,['dividido entre']],'cap': [0,['intersecci&oacute;n']],'cup':[0,['uni&oacute;n']],'uplus':[0,['uni&oacute;n con suma']],'sqcap':[0,['intersecci&oacute;n rect&aacute;ngular']],'sqcup':[0,['uni&oacute;n rect&aacute;ngular']],'triangleleft':[0,['tri&aacute;angulo a la izquierda']],'triangleright':[0,['tri&aacute;ngulo a la derecha']],'wr':[0,['producto corona']],'bigcirc':[0,['círculo grande']],'bigtriangleup':[0,['tri&aacute;ngulo grande hacia arriba']],'bigtriangledown':[0,['tri&aacute;ngulo grande hacia abajo']],'vee':[0,['disyunci&oacute;n']],'wedge':[0,['conjunci&oacute;n']],'oplus':[0,['circunsuma']],'ominus':[0,['circunresta']],'otimes':[0,['circuncruz']],'oslash':[0,['circunbarra']],'odot':[0,['circunpunto']], 'dagger': [0,['daga']],'ddagger': [0,['doble daga']],'amalg':[0,['amalgamaci&oacute;n']],'lor':[0,['disyunci&oacute;n']],'land':[0,['conjunci&oacute;n']], 'bmod':[0,['m&oacute;dulo']]}

BinaryRelations ={'=':[0,['igual']],'<':[0,['menor']],'>':[0,['mayor']],'leq':[0,['menor igual']], 'geq':[0,['mayor igual']], 'equiv':[0,['equivalente']], 'prec':[0,['precede']], 'succ':[0,['sucede']], 'sim':[0,['similar']], 'preceq':[0,['precede igual']], 'succeq':[0,['sucede igual']], 'simeq':[0,['similar igual']], 'll':[0,['mucho menor']], 'gg':[0,['mucho mayor']], 'asymp':[0,['asint&oacute;tico']], 'subset':[0,['subconjunto']], 'supset':[0,['superconjunto']], 'approx':[0,['aproximado']], 'subseteq':[0,['subconjunto igual']], 'supseteq':[0,['super conjunto igual']], 'cong':[0,['congruente']], 'sqsubseteq':[0,['subconjunto rect&aacute;ngular']], 'sqsupseteq':[0,['superconjunto rect&aacute;ngular']], 'bowtie':[0,['junta']], 'in':[0,['est&aacute; en']], 'ni':[0,['contiene a']], 'propto':[0,['proporcional']], 'vdash':[0,['deduce']], 'dashv':[0,['deducido']], 'models':[0,['modela']],'smile':[0,['sonrisa']], 'mid':[0,['medio']], 'doteq':[0,['igual puntuado']],'frown':[0,['fruncido']], 'parallel':[0,['paralelo']],'perp':[0,['perpendicular']], 'neq':[0,['no igual']], 'notin':[0,['no est&aacute; en']], 'ne':[0,['no igual']],'le':[0,['menor igual']],'ge':[0,['mayor igula']],'owns':[0,['contiene']]}

MathFunctions ={'arccos':[0,['arco coseno']], 'arcsin':[0,['arco seno']], 'arctan':[0,['arco tangente']], 'arg':[0,['argumento']], 'cos':[0,['coseno']], 'cosh':[0,['coseno hiperb&oacute;lico']], 'cot':[0,['cotangente']], 'coth':[0,['cotangente hiperb&oacute;lico']], 'csc':[0,['cosecante']], 'deg':[0,['grado']], 'det':[0,['determinante']], 'dim':[0,['dimenci&oacute;n']], 'exp':[0,['exponencial']], 'gcd':[0,['mayor com&uacute;n divisor']], 'hom':[0,['homomorfismo']], 'inf':[0,['infimo']], 'ker':[0,['n&uacute;cleo']], 'lg':[0,['logaritmo binario']], 'liminf':[0,['lim inf']], 'limsup':[0,['lim sup']], 'ln':[0,['logaritmo natural']], 'log':[0,['logaritmo']], 'max':[0,['m&aacute;ximo']], 'min':[0,['mi&iacute;nimo']], 'Pr':[0,['probabilidad']], 'sec':[0,['secante']], 'sin':[0,['seno']], 'sinh':[0,['seno hiperb&oacute;lico']], 'sup':[0,['supremo']], 'tan':[0,['tangente']], 'tanh':[0,['tangente hiperb&oacute;lico']]}

Arrows ={'leftarrow':[0,['flecha izquierda']], 'Leftarrow':[0,['flecha izquierda doble']], 'rightarrow':[0,['flecha derecha']], 'Rightarrow':[0,['flecha derecha doble']], 'leftrightarrow':[0,['flecha izquierda derecha']], 'Leftrightarrow':[0,['flecha izquierda derecha doble']], 'mapsto':[0,['env&iacute;a']], 'hookleftarrow':[0,['flecha  garfio izquierda']], 'leftharpoonup':[0,['arp&oacute;n arriba izquierdo']], 'leftharpoondown':[0,['arp&oacute;n abajo izquierda']], 'rightleftharpoons':[0,['arp&oacute;n izquierda derecha']], 'longleftarrow':[0,['flecha izquierda larga']], 'Longleftarrow':[0,['flecha izquierda doble larga']], 'longrightarrow':[0,['flecha derecha larga']], 'Longrightarrow':[0,['flecha derecha doble larga']], 'longleftrightarrow':[0,['flecha izquierda derecha larga']], 'Longleftrightarrow':[0,['flecha izquierda derecha doble larga']], 'longmapsto':[0,['env&iacute;a largo']], 'hookrightarrow':[0,['flecha garfio derecha']], 'rightharpoonup':[0,['arp&oacute;n arriba derecho']], 'rightharpoondown':[0,['arp&acute;n abajo derecho']], 'uparrow':[0,['flecha arriba']], 'Uparrow':[0,['flecha arriba doble']], 'downarrow':[0,['flecha abajo']], 'Downarrow':[0,['flecha abajo doble']], 'updownarrow':[0,['flecha arriba abajo']], 'Updownarrow':[0,['flecha arriba abajo doble']], 'nearrow':[0,['flecha diagonal arriba derecha']], 'searrow':[0,['flecha diagonal abajo derecha']], 'swarrow':[0,['flecha diagonal abajo izquierda']], 'nwarrow':[0,['flecha diagonal arriba izquierda']],'to':[0,['hacia']],'gets':[0,['obtiene']],'iff':[0,['si y solo si']]}

Delimiters ={'(':[0,['abre par&eacute;ntesis']],')':[0,['cierra par&eacute;ntesis']],'[':[0,['abre corchete']],']':[0,['cierra corchete']], '{':[0,['abre llave']],'}':[0,['cierra llave']], 'lfloor':[0,['abre piso']],'rfloor':[0,['cierra piso']], 'lceil':[0,['abre techo']], 'rceil':[0,['cierra techo']],'langle':[0,[' abre &aacute;ngulo']],'rangle':[0,['cierra &aacute;ngulo']],'backslash':[0,['barra invertida']]}

Accents ={'hat':[0,['gorro']],'check':[0,['anticircunflejo']],'breve':[0,['breve']],'acute':[0,['agudo']],'grave':[0,['grave']],'tilde':[0,['virgulilla']],'bar':[0,['barra']], 'vec':[0,['vecctor']],'dot':[0,['punto']],'ddot':[0,['doble punto']],'widehat':[0,['gorro']],'widetilde':[0,['virgulilla']]}

Styles ={'mathit':[0,['it&aacute;lica']],'mathrm':[0,['roman']],'mathbf':[0,['negrilla']],'mathsf':[0,['sans serif']],'mathtt':[0,['m&aacute;quina escribir']], 'mathcal':[0,['caligr&aacute;fica']], 'boldmath':[0,['negrilla']]}

Dots ={'dots':[0,['puntos']],'ldots':[0,['puntos bajos']],'cdots':[0,['puntos centrados']],'vdots':[0,['puntos verticales']],'ddots':[0,['puntos diagonales']]}

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
#
OPTION = 0

#
precedence = (
	('left','SUP','SUB', 'FRAC','ROOT'),
	('right', 'LARGEOP')	
)


def p_start(p):
	'''start : content
				| start content'''
	if(len(p) == 3):
		p[0] =  p[1] + p[2] + ' '
	else:
		p[0] = p[1] + ' '


def p_block(p):
	'''block : BEGINBLOCK content ENDBLOCK'''
	p[0] = p[2]


def p_content(p):
	'''content : block
				| scripted
				| command
				| content content'''
	if(len(p) == 3):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1]
	

def p_char(p):
	'''char : CHAR
			| ord
'''
	p[0] = p[1] + ' '


def p_ord(p):
	'''ord : ORD '''
	p[0] =  formulate.formulate(dOrdinary.showReading(p[1],0),OPTION)#--->Los operadores son la llave y el valor por defecto que esté en la lectura


def p_command(p):
	'''command : frac
				| char
				| root
				| array
				| col
				| factorial
				| larop
				| prime
				| binop
				| binrel
				| not
				| function
				| arrow
				| delimiter
				| accent
				| style
				| dots
				| lim
				| combi
				| unknown
				| pmod
				| lnbrk'''
	p[0] = p[1]

#------------------------------------------------------------------------------------------------------


#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels; tal vez que p[0] = "una función que depende de los otros p[i]".

def p_scripted(p):
	'''scripted : command SUP command
					| command SUP block
					| block SUP command
					| block SUP block
					| command SUB command
					| command SUB block
					| block SUB command
					| block SUB block'''
	if(p[2] == '^'):
		p[0] = p[1] + formulate.formulate('s&uacute;per',OPTION) + p[3] + formulate.formulate('fin s&uacute;per',OPTION)
	else:
		p[0] = p[1] + formulate.formulate('sub',OPTION) + p[3] + formulate.formulate('fin sub',OPTION)
			
def p_compScripted(p):
	'''scripted : command SUP command SUB command
					| command SUP command SUB block
					| command SUP block SUB command
					| command SUP block SUB block
					| block SUP command SUB command
					| block SUP command SUB block
					| block SUP block SUB command
					| block SUP block SUB block
					| command SUB command SUP command
					| command SUB command SUP block
					| command SUB block SUP command
					| command SUB block SUP block
					| block SUB command SUP command
					| block SUB command SUP block
					| block SUB block SUP command
					| block SUB block SUP block'''
	if(p[2] =='^'):
		p[0] =  p[1] + formulate.formulate('s&uacute;per',OPTION) + p[3] + formulate.formulate('fin s&uacute;per',OPTION) + formulate.formulate('sub',OPTION) + p[5] + formulate.formulate('fin sub',OPTION)
	else:
		p[0] = p[1] + formulate.formulate('sub',OPTION) + p[3] + formulate.formulate('fin sub',OPTION) + formulate.formulate('s&uacute;per',OPTION) + p[5] + formulate.formulate('fin s&uacute;per',OPTION)
		
def p_frac(p):
	'''frac : FRAC command command
				| FRAC command block
				| FRAC block command
				| FRAC block block'''
	p[0] = formulate.formulate('comienza fracci&oacute;n',OPTION) + p[2] + formulate.formulate('sobre',OPTION) + p[3] + formulate.formulate('fin fracci&oacute;n',OPTION)

def p_root(p):
	'''root : ROOT command
			| ROOT block
			| ROOT KDELIMITER content KDELIMITER command
			| ROOT KDELIMITER content KDELIMITER block '''
	if(len(p) == 3):
		p[0] = formulate.formulate('ra&iacute;z cuadrada de',OPTION) + p[2] + formulate.formulate('termina ra&iacute;z',OPTION)
	else:
		p[0] = formulate.formulate('ra&iacute;z',OPTION) + p[3] + formulate.formulate('de',OPTION) + p[5] + formulate.formulate('termina ra&iacute;z',OPTION)


def p_binOp(p):
	'''binop : BINOP
				| KBINOP '''
	p[0] = formulate.formulate(dBinaryOperators.showReading(p[1],0),OPTION)


def p_binRel(p):
	'''binrel : BINREL
				| KBINREL'''
	p[0] = formulate.formulate(dBinaryRelations.showReading(p[1],0),OPTION)

def p_not(p):
	'''not : NOT '''
	p[0]= formulate.formulate('no',OPTION)	

def p_function(p):
	'''function : FUNC '''
	p[0] = formulate.formulate(dMathFunctions.showReading(p[1],0),OPTION)

def p_comLargeOp(p):
	'''larop : LARGEOP SUB command SUP command
				| LARGEOP SUB command SUP block
				| LARGEOP SUB block SUP command
				| LARGEOP SUB block SUP block
				| LARGEOP SUP command SUB command
				| LARGEOP SUP command SUB block
				| LARGEOP SUP block SUB command
				| LARGEOP SUP block SUB block'''
	if(p[2] =='_'):
		p[0] = formulate.formulate(dLargeOperators.showReading(p[1],0) + ' desde',OPTION) + p[3] + formulate.formulate('hasta',OPTION) + p[5] + formulate.formulate('de',OPTION)
	else:
		p[0] = formulate.formulate(dLargeOperators.showReading(p[1],0) + ' desde',OPTION) + p[5] + formulate.formulate('hasta',OPTION) + p[3] + formulate.formulate('de',OPTION)

def p_largeOp(p):
	'''larop : LARGEOP
				| LARGEOP SUB command
				| LARGEOP SUB block'''
	if(len(p)==2):
		p[0]= formulate.formulate(dLargeOperators.showReading(p[1],0),OPTION)
	elif(len(p)==4):
		p[0] = formulate.formulate(dLargeOperators.showReading(p[1],0) +' sobre',OPTION) + p[3] + formulate.formulate('de',OPTION)

def p_arrow(p):
	'''arrow : ARROW'''
	p[0] = formulate.formulate(dArrows.showReading(p[1],0),OPTION)

def p_delimiter(p):
	'''delimiter : DELIMITER
					| KDELIMITER '''
	p[0] = formulate.formulate(dDelimiters.showReading(p[1],0),OPTION)

def p_simpleAccent(p):
	'''accent : ACCENT command'''
	p[0] = p[2] + formulate.formulate(dAccents.showReading(p[1],0),OPTION)

def p_complexAccent(p):
	'''accent : ACCENT block'''
	if(len(p[2]) > 3):
		p[0] = formulate.formulate(dAccents.showReading(p[1],0),OPTION) + p[2] + formulate.formulate('fin ' + dAccents.showReading(p[1],0),OPTION,)
	else:
		p[0] = p[2] + formulate.formulate(dAccents.showReading(p[1],0),OPTION)

def p_style(p):
	'''style : STYLE command
				| STYLE block '''
	p[0] = formulate.formulate(dStyles.showReading(p[1],0),OPTION) + p[2] + formulate.formulate('fin ' + dStyles.showReading(p[1],0),OPTION)

def p_dots(p):
	'''dots : DOTS '''
	p[0] = formulate.formulate(dDots.showReading(p[1],0),OPTION)

def p_lim(p):
	'''lim : LIM
			| LIM SUB command
			| LIM SUB block '''
	if(len(p) == 4):
		p[0] = formulate.formulate('l&iacute;mite cuando',OPTION) + p[3] + formulate.formulate('de',OPTION)
	else:
		p[0] = formulate.formulate('l&iacute;mite de',OPTION)

def p_unknown(p):
	'''unknown : UNKNOWN'''
	p[0] = formulate.formulate(p[1],OPTION)
#
def p_array(p):
	'''array : BEGARRAY row ENDARRAY '''
	p[0] = '<table>\n' + p[2] + '</table>'

def p_rows(p):
	'''row : column LINEBREAK row
			| column'''
	if(len(p) == 4):
		p[0] = '<tr>' + p[1] + '</tr>\n' + p[3]
	else:	
		p[0] = '<tr>' + p[1] + '</tr>\n'

def p_columns(p):
	'''column : content col column
			| content'''
	if(len(p) == 4):
		p[0] = '<td>' + p[1] + '</td>' + p[3]
	else:
		p[0] = '<td>' + p[1] + '</td>'
#
def p_col(p):
	'''col : COL'''
	p[0] = ''

def p_factorial(p):
	'''factorial : '!' '''
	p[0] = formulate.formulate('factorial',OPTION)

def p_prime(p):
	'''prime : "'" '''
	p[0] = formulate.formulate('prima',OPTION)

def p_combi(p):
	'''combi : choose
			| binom '''
	p[0] = p[1]

def p_choose(p):
	'''choose : command CHOOSE command
				| command CHOOSE block
				| block CHOOSE command
				| block CHOOSE block'''
	p[0] = formulate.formulate('combinaciones de', OPTION) + p[1] + formulate.formulate('en',OPTION) + p[3]

def p_binom(p):
	'''binom : BINOM command command
			| BINOM command block
			| BINOM block command
			| BINOM block block ''' 
	p[0] = formulate.formulate('combinaciones de', OPTION) + p[2] + formulate.formulate('en',OPTION) + p[3]

def p_pmod(p):
	'''pmod : PMOD command'''
	p[0] = formulate.formulate('m&oacute;dulo',OPTION) + p[2]

def p_blockpmod(p):
	'''pmod : PMOD block'''
	p[0] = formulate.formulate('m&oacute;dulo', OPTION) + p[2] + formulate.formulate('fin mod', OPTION)

def p_linebreak(p):
	'''lnbrk : LINEBREAK'''
	p[0] = formulate.formulate('salto de l&iacute;nea',OPTION)

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

