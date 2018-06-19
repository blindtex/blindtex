#-*-:coding:utf-8-*-

import ply.lex
import ply.yacc
import lexer

from ast import Node

tokens = lexer.tokens

def p_start(p):
    """
    start : formula
		| start formula
    """
    if(len(p) == 2):
    	p[0] = p[1]
    else:
		p[0] =Node(content = 'concatenation', left = p[1], right =p[2] )

def p_formula(p):
    """
    formula : symbol
            | block
    """
    p[0] = p[1]

def p_delimiters(p):
	'''
	formula : delimiter start delimiter
	'''
	p[2].left_delimiter = p[1]
	p[2].right_delimiter = p[3]
	p[0] = p[2]

def p_accent(p):
	'''
	formula : ACCENT block
			| ACCENT symbol
	'''
	p[2].accent = p[1]
	p[0] = p[2]

def p_style(p):
	'''
	formula : STYLE block
			| STYLE symbol
	'''
	p[2].style = p[1]
	p[0] = p[2]

def p_formula_scripted(p):
	'''
	formula : formula simple_scripted
			| formula compound_scripted
	'''
	p[0] = p[1]

def p_simple_scripted(p):
	'''
	simple_scripted : SUP symbol
			| SUP block
			| SUB symbol
			| SUB block
	'''
	if(p[1] == '^'):
		p[-1].superscript = p[2]
	else:
		p[-1].subscript = p[2]

def p_compound_scripted(p):
	'''
	compound_scripted : SUP symbol SUB symbol
					| SUP symbol SUB block
					| SUP block SUB symbol
					| SUP block SUB block
					| SUB symbol SUP symbol
					| SUB symbol SUP block
					| SUB block SUP symbol
					| SUB block SUP block
	'''
	if(p[1] == '^'):
		p[-1].superscript = p[2]
		p[-1].subscript = p[4]
	else:
		p[-1].subscript = p[2]
		p[-1].superscript = p[4]


def p_block(p):
    """
    block : BEGINBLOCK start ENDBLOCK
    """
    p[0] = p[2]

def p_ordinary(p):
    """
    symbol : NUM
            | CHAR
			| ORD
    """
    p[0] = Node(content=p[1])

def p_delimiter(p):
	'''
	delimiter : KDELIMITER
				| DELIMITER
	'''
	p[0] = p[1]

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
