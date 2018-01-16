#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
from dictionary import *
from lexer import tokens
import formulate
import os
#--------------------------------------------------------------------------
#Variables dirección del los json


#Lista de objetos diccionario:
dOrdinary = dictionary(os.path.join('dicts','Ordinary.json'))
dLargeOperators = dictionary(os.path.join('dicts','LargeOperators.json'))
dBinaryOperators = dictionary(os.path.join('dicts','BinaryOperators.json'))
dBinaryRelations = dictionary(os.path.join('dicts','BinaryRelations.json'))
dMathFunctions = dictionary(os.path.join('dicts','MathFunctions.json'))
dArrows = dictionary(os.path.join('dicts','Arrows.json'))
dDelimiters = dictionary(os.path.join('dicts','Delimiters.json'))
dAccents = dictionary(os.path.join('dicts','Accents.json'))
dStyles = dictionary(os.path.join('dicts','Styles.json'))
dDots = dictionary(os.path.join('dicts','Dots.json'))
#-------------------------------------------------------------------------------
#TODO Find a way to avoid global variables.
OPTION = 0 #This option are for the formulate function. 0 is for span and &nbsp , 1 is for literal translation and 2 is for math and nbsp.

def getOption():
	'''Function to get the current value of OPTION.
		return(int): The value of OPTION'''
	return OPTION
	
def setOption(intOption):
	'''Function to change the value of OPTION.
		Args:
			intOption(int): The value the user wants for OPTION.'''
	global OPTION
	OPTION = intOption

	
#The grammar.
precedence = (
	
	('left', 'LARGEOP'),
	('left','SUP','SUB', 'FRAC','ROOT'),	
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
				| content content
				| larop'''
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
	p[0] =  formulate.formulate(dOrdinary.showReading(p[1]),OPTION)#--->Los operadores son la llave y el valor por defecto que esté en la lectura


def p_command(p):
	'''command : frac
				| char
				| root
				| array
				| col
				| factorial
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
				| lnbrk
				| phantom'''
	p[0] = p[1]

#------------------------------------------------------------------------------------------------------


#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels; tal vez que p[0] = "una función que depende de los otros p[i]".

#TODO Que se pueda poner ^2 o _b sin una base. Quitar el command o block antes, solo dejar SUP algo.
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

#TODO Poder poner LargeOP en esta regla.
def p_simpleFrac(p):
	'''frac : FRAC command command '''
	p[0] = p[2] + formulate.formulate('sobre',OPTION) + p[3]
		
def p_frac(p):
	'''frac : FRAC command block
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
	p[0] = formulate.formulate(dBinaryOperators.showReading(p[1]),OPTION)


def p_binRel(p):
	'''binrel : BINREL
				| KBINREL'''
	p[0] = formulate.formulate(dBinaryRelations.showReading(p[1]),OPTION)

def p_not(p):
	'''not : NOT '''
	p[0]= formulate.formulate('no',OPTION)	

def p_function(p):
	'''function : FUNC '''
	p[0] = formulate.formulate(dMathFunctions.showReading(p[1]),OPTION)

#TODO: Large operator is mocking again, by the moment it can not be used as a normal symbol.
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
		p[0] = formulate.formulate(dLargeOperators.showReading(p[1]) + ' desde',OPTION) + p[3] + formulate.formulate('hasta',OPTION) + p[5] + formulate.formulate('de',OPTION)
	else:
		p[0] = formulate.formulate(dLargeOperators.showReading(p[1]) + ' desde',OPTION) + p[5] + formulate.formulate('hasta',OPTION) + p[3] + formulate.formulate('de',OPTION)

def p_largeOp(p):
	'''larop : LARGEOP
				| LARGEOP SUB command
				| LARGEOP SUB block'''
	if(len(p)==2):
		p[0]= formulate.formulate(dLargeOperators.showReading(p[1]),OPTION)
	elif(len(p)==4):
		p[0] = formulate.formulate(dLargeOperators.showReading(p[1]) +' sobre',OPTION) + p[3] + formulate.formulate('de',OPTION)

def p_arrow(p):
	'''arrow : ARROW'''
	p[0] = formulate.formulate(dArrows.showReading(p[1]),OPTION)

def p_delimiter(p):
	'''delimiter : DELIMITER
					| KDELIMITER '''
	p[0] = formulate.formulate(dDelimiters.showReading(p[1]),OPTION)

def p_simpleAccent(p):
	'''accent : ACCENT command'''
	p[0] = p[2] + formulate.formulate(dAccents.showReading(p[1]),OPTION)

def p_complexAccent(p):
	'''accent : ACCENT block'''
	if(len(p[2]) > 3):
		p[0] = formulate.formulate(dAccents.showReading(p[1]),OPTION) + p[2] + formulate.formulate('fin ' + dAccents.showReading(p[1]),OPTION,)
	else:
		p[0] = p[2] + formulate.formulate(dAccents.showReading(p[1]),OPTION)

def p_style(p):
	'''style : STYLE command
				| STYLE block '''
	p[0] = formulate.formulate(dStyles.showReading(p[1]),OPTION) + p[2] + formulate.formulate('fin ' + dStyles.showReading(p[1]),OPTION)

def p_dots(p):
	'''dots : DOTS '''
	p[0] = formulate.formulate(dDots.showReading(p[1]),OPTION)

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

def p_phantom(p):
	'''phantom : PHANTOM command
				| PHANTOM block'''
	p[0] = ''


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

