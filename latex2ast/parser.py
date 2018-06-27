#-*-:coding:utf-8-*-

import ply.lex
import ply.yacc
import lexer

from ast import Node

tokens = lexer.tokens

precedence = (
	('right', 'SUP', 'SUB'),
)
# In this parser the end result will be a python list with math_objects as elements.
# Each math object will have some characteristics.
def p_start(p):
    """
    start : formula
    """
    p[0] = p[1]
#If formula is nothing, the list does not exist, so it is oppened; if not,
# to the list we add the new math object.
def p_formula(p):
    """
    formula : math_object
			| concat
    """
    if(p[0] == None):
        p[0] = p[1]
    else:
        p[0] = p[0] + p[1]

#Rule to deal with concatenation of math objects.
def p_formulas(p):  
	'''concat :  math_object formula'''
	if(p[0] == None):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[0] + p[1] +p[2]
	
def p_math_object(p):
	'''math_object : symbol
				| block
                | fraction 
                | root
                | choose
                | binom
                | pmod
                | text
                | label'''
	p[0] = [p[1]]#It returns a list of one object.

def p_block(p):
    """
    block : BEGINBLOCK formula ENDBLOCK
    """
    p[0] = Node(content = 'block')
    p[0].append_child(p[2])


def p_accent(p):
	'''
	math_object : ACCENT block
			| ACCENT symbol
	'''
	p[2].accent = p[1]
	p[0] = [p[2]]

def p_style(p):
	'''
	math_object : STYLE block
			| STYLE symbol
	'''
	p[2].style = p[1]
	p[0] = [p[2]]


def p_formula_scripted(p):
	'''
	math_object : math_object simple_scripted
			| math_object compound_scripted
	'''
	p[0] = p[1]

def p_index(p):
	'''index : symbol
			| block '''
	p[0] = [p[1]]

#TODO: What if p[-1] is nothing? "_3^2 A" is a valid LaTeX formula.
def p_simple_scripted(p):
	'''
	simple_scripted : SUP index
					| SUB index
	'''
	if(p[1] == '^'):
		p[-1][0].superscript = p[2]#Adds the script to the previous element.
	else:
		p[-1][0].subscript = p[2]

def p_compound_scripted(p):
	'''
	compound_scripted : SUP index SUB index
					| SUB index SUP index
	'''
	if(p[1] == '^'):
		p[-1][0].superscript = p[2]
		p[-1][0].subscript = p[4]
	else:
		p[-1][0].subscript = p[2]
		p[-1][0].superscript = p[4]




def p_symbol(p):
    """
    symbol : NUM
            | CHAR
			| ORD
            | LARGEOP
            | BINOP
            | KBINOP
            | KBINREL
            | BINREL
            | FUNC
            | ARROW
            | kdelimiter
            | DELIMITER
            | DOTS
            | LIM
            | UNKNOWN
            | MOD
            | "!"
            | NOT
            | LINEBREAK
			| KNOT
			| USER
    """
    p[0] = Node(content = p[1])
#We count [ and ] apart because the \sqrt structure uses them.
def p_kdelimiter(p):
    '''kdelimiter : KDELIMITER
                    | "["
                    | "]" '''
    p[0] = p[1]

def p_fraction(p):
    '''fraction : FRAC index index '''
    p[0] = Node(content = 'fraction')
    p[0].append_child(p[2])
    p[0].append_child(p[3][0]) #This is because p[3] is a list, as index returns that, but we want to append the node, not the list.


def p_root(p):
    '''root : sqr_root
            | index_root '''
    p[0] = p[1]

def p_sqr_root(p):
    '''sqr_root : ROOT index '''
    p[0] = Node(content = 'root')
    p[0].append_child(p[2])


def p_index_root(p):
    '''index_root : ROOT "[" index "]" index '''
    p[0] = Node(content = 'root')
    p[0].append_child(p[3])#The first child will be the index.
    p[0].append_child(p[5][0])#This is because p[5] is a list, as index returns that, but we want to append the node, not the list.

def p_choose(p):
    ''' choose : formula CHOOSE formula '''
    p[0] = Node(content = 'choose')
    p[0].append_child(p[1])
    p[0].append_child(p[3][0])

#Something funny here. See test_binom
def p_binom(p):
    '''binom : BINOM index index '''
    p[0] = Node(content = 'binom')
    p[0].append_child(p[2])
    p[0].append_child(p[3][0])

def p_pmod(p):
    ''' pmod : PMOD index '''
    p[0] = Node(content = 'pmod')
    p[0].append_child(p[2])

def p_text(p):
    ''' text : TEXT TCHAR
            | TEXT ANYTHING'''
    p[0] = Node(content = 'text')
    p[0].append_child(p[2])

def p_label(p):
    '''label : LABEL '''
    p[0] = Node(content = 'label')
    p[0].append_child(p[1])




def get_parser():
    return ply.yacc.yacc()

if __name__ == "__main__":
    parser = get_parser()
    latex_string = "\sqrt{2+3}"
    custom_lexer = lexer.get_lexer()
    cv = parser.parse(latex_string,custom_lexer)#,debug=1)
    print(interpreter(cv))
    while True:
        try:
            try:
                s = raw_input()
            except NameError: # Python3
                s = input('spi> ')

            cv_s = parser.parse(s,custom_lexer)
            print(interpreter(cv_s))
        except EOFError:
            break
