#Lexer of LaTeX math content

import ply.lex as lex
from ply.lex import TOKEN
import json
import re


fileName = 'regexes.json'
 
tokens = ('CHAR', 'SUP', 'SUB','BEGINBLOCK','ENDBLOCK', 'ORD', 'FRAC', 'ROOT', 'LARGEOP', 'BINOP','KBINOP','KBINREL', 'BINREL', 'NOT', 'FUNC', 'ARROW', 'KDELIMITER', 'DELIMITER', 'ACCENT','STYLE','DOTS','LIM', 'UNKNOWN', 'BEGARRAY', 'ENDARRAY', 'LINEBREAK', 'COL','CHOOSE', 'BINOM', 'PMOD','PHANTOM',)

dictOfDicts = json.loads('{"dots": "dots|ldots|cdots|vdots|ddots", "delimiter": "{|}|lfloor|rfloor|lceil|rceil|langle|rangle|backslash", "func": "arccos|arcsin|arctan|arg|cos|cosh|cot|coth|csc|deg|det|dim|exp|gcd|hom|inf|ker|lg|liminf|limsup|ln|log|max|min|Pr|sec|sin|sinh|sup|tan|tanh", "binRel": "leq|geq|equiv|prec|succ|sim|preceq|succeq|simeq|ll|gg|asymp|subset|supset|approx|subseteq|supseteq|cong|sqsubseteq|sqsupseteq|bowtie|in|ni|propto|vdash|dashv|models|smile|mid|doteq|frown|parallel|perp|neq|notin|ne|(le)|ge|owns", "binOp": "pm|mp|setminus|cdot|times|ast|star|diamond|circ|bullet|div|cap|cup|uplus|sqcap|sqcup|triangleleft|triangleright|wr|bigcirc|bigtriangleup|bigtriangledown|vee|wedge|oplus|ominus|otimes|oslash|odot|dagger|ddagger|amalg|lor|land|bmod", "largeOperator": "sum|prod|coprod|int|oint|bigcap|bigcup|bigsqcup|bigvee|bigwedge|bigodot|bigotimes|bigoplus|biguplus|limits", "arrow": "leftarrow|Leftarrow|rightarrow|Rightarrow|leftrightarrow|Leftrightarrow|mapsto|hookleftarrow|leftharpoonup|leftharpoondown|rightleftharpoons|longleftarrow|Longleftarrow|longrightarrow|Longrightarrow|longleftrightarrow|Longleftrightarrow|longmapsto|hookrightarrow|rightharpoonup|rightharpoondown|uparrow|Uparrow|downarrow|Downarrow|updownarrow|Updownarrow|nearrow|searrow|swarrow|nwarrow|to|gets|iff", "ordinary": "(alpha)|(beta)|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|kappa|lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|aleph|hbar|imath|jmath|ell|vp|Re|Im|partial|infty|prime|emptyset|nabla|surd|top|bot|\\\||angle|triangle|backslash|forall|exists|neg|flat|natural|sharp|clubsuit|diamondsuit|heartsuit|spadsuit|lnot|prime", "accent": "hat|check|breve|acute|grave|tilde|bar|vec|dot|ddot|widehat|widetilde", "style": "mathit|mathrm|mathbf|mathsf|mathtt|mathcal|boldmath"}')

states = (('command', 'exclusive'),)

#try:
#	myFile = open(fileName, 'r')
#	dictOfDicts = json.load(myFile)
#	myFile.close()
#except IOError:

literals = [':', '!',"'"]

def t_BEGINBLOCK(t):
	r'\{'
	return t

def t_ENDBLOCK(t):
	r'\}'
	return t

def t_SUP(t):
	r'\^'
	return t

def t_SUB(t):
	r'_'
	return t

def t_COMMAND(t):
	r'\\'
	t.lexer.begin('command')
	return

def t_command_PMOD(t):
	r'pmod'
	t.lexer.begin('INITIAL')
	return t

def t_command_PHANTOM(t):
	r'[hv]?phantom'
	t.lexer.begin('INITIAL')
	return t

def t_command_BEGARRAY(t):
	r'(begin\{array\}|begin\{[pbBvV]?matrix(\*)?\})(\[.*?\])?(\{.*?\})?'
	t.lexer.begin('INITIAL')
	return t

def t_command_ENDARRAY(t):
	r'end\{array\}|end\{[pbBvV]?matrix(\*)?\}'
	t.lexer.begin('INITIAL')
	return t

def t_command_LINEBREAK(t):
	r'\\'
	t.lexer.begin('INITIAL')
	return t

def t_COL(t):
	r'[&]'
	return t

@TOKEN(dictOfDicts['largeOperator'])
def t_command_LARGEOP(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['ordinary'])
def t_command_ORD(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_FRAC(t):
	r'frac|tfrac|dfrac'
	t.lexer.begin('INITIAL')
	return t

def t_command_ROOT(t):
	r'sqrt'
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['arrow'])
def t_command_ARROW(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_leftRight(t):
	r'(left)|(right)|left\.|right\.'
	t.lexer.begin('INITIAL')
	pass

def t_KBINOP(t):#Binary operators that can be made from the keyboard.
	r'\+|-|\*|/'
	return t

@TOKEN(dictOfDicts['dots'])
def t_command_DOTS(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['binOp'])	
def t_command_BINOP(t):
	
	t.lexer.begin('INITIAL')
	return t


def t_KBINREL(t):
	r'[=<>]'	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['binRel'])
def t_command_BINREL(t):
		
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['func'])
def t_command_FUNC(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_NOT(t):
	r'not'
	t.lexer.begin('INITIAL')
	return t

def t_KDELIMITER(t):
	r'\(|\)|\[|\]'
	return t

@TOKEN(dictOfDicts['delimiter'])
def t_command_DELIMITER(t):
	
	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['accent'])
def t_command_ACCENT(t):

	t.lexer.begin('INITIAL')
	return t

@TOKEN(dictOfDicts['style'])
def t_command_STYLE(t):
	
	t.lexer.begin('INITIAL')
	return t

def t_command_LIM(t):
	r'lim'
	t.lexer.begin('INITIAL')
	return t

def t_command_CHOOSE(t):
	r'choose'
	t.lexer.begin('INITIAL')
	return t

def t_command_BINOM(t):
	r'binom'
	t.lexer.begin('INITIAL')
	return t

def t_command_MATHSPACE(t):
	r'[,!:;]|quad|qquad'
	t.lexer.begin('INITIAL')
	pass

def t_CHAR(t):
	r'[A-Za-z0-9,.]+?'
	return t

def t_command_UNKNOWN(t):
	r'[A-Za-z]+'
	t.lexer.begin('INITIAL')
	return t

t_ignore_SPACE=r'[ \t\n]+'


def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)


lexer= lex.lex()
#while True:
#	s = raw_input()
#	lexer.input(s)
#	while True:
#		tok = lexer.token()
#		if not tok:
#			break
#		print tok
