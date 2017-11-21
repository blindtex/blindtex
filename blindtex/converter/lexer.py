#Lexer of LaTeX math content

import ply.lex as lex
import re

tokens = ('CHAR', 'SUP', 'SUB','BEGINBLOCK','ENDBLOCK', 'ORD', 'FRAC', 'ROOT', 'LARGEOP', 'BINOP','KBINOP','KBINREL', 'BINREL', 'NOT', 'FUNC', 'ARROW', 'KDELIMITER', 'DELIMITER', 'ACCENT','STYLE','DOTS','LIM', 'UNKNOWN')

states = (('command', 'exclusive'),)

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
	pass

def t_command_LARGEOP(t):
	r'sum|prod|coprod|int|oint|bigcap|bigcup|bigsqcup|bigvee|bigwedge|bigodot|bigotimes|bigoplus|biguplus'
	t.lexer.begin('INITIAL')
	return t

def t_command_ORD(t):
	r'(alpha)|(beta)|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|kappa|lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|aleph|hbar|imath|jmath|ell|vp|Re|Im|partial|infty|prime|emptyset|nabla|surd|top|bot|\||angle|triangle|backslash|forall|exists|neg|flat|natural|sharp|clubsuit|diamondsuit|heartsuit|spadsuit|lnot'
	t.lexer.begin('INITIAL')
	return t

def t_command_FRAC(t):
	r'frac'
	t.lexer.begin('INITIAL')
	return t

def t_command_ROOT(t):
	r'sqrt'
	t.lexer.begin('INITIAL')
	return t

def t_command_ARROW(t):
	r'leftarrow|Leftarrow|rightarrow|Rightarrow|leftrightarrow|Leftrightarrow|mapsto|hookleftarrow|leftharpoonup|leftharpoondown|rightleftharpoons|longleftarrow|Longleftarrow|longrightarrow|Longrightarrow|longleftrightarrow|Longleftrightarrow|longmapsto|hookrightarrow|rightharpoonup|rightharpoondown|uparrow|Uparrow|downarrow|Downarrow|updownarrow|Updownarrow|nearrow|searrow|swarrow|nwarrow|to|gets|iff'
	t.lexer.begin('INITIAL')
	return t

def t_command_leftRight(t):
	r'(left)|(right)'
	t.lexer.begin('INITIAL')
	pass

def t_KBINOP(t):#Binary operators that can be made from the keyboard.
	r'\+|-|\*|/'
	return t

def t_command_DOTS(t):
	r'dots|ldots|cdots|vdots|ddots'
	t.lexer.begin('INITIAL')
	return t
	
def t_command_BINOP(t):
	r'pm|mp|setminus|cdot|times|ast|star|diamond|circ|bullet|div|cap|cup|uplus|sqcap|sqcup|triangleleft|triangleright|wr|bigcirc|bigtriangleup|bigtriangledown|vee|wedge|oplus|ominus|otimes|oslash|odot|dagger|ddagger|amalg|lor|land'
	t.lexer.begin('INITIAL')
	return t

def t_KBINREL(t):
	r'[=<>]'	
	t.lexer.begin('INITIAL')
	return t

def t_command_BINREL(t):
	r'leq|geq|equiv|prec|succ|sim|preceq|succeq|simeq|ll|gg|asymp|subset|supset|approx|subseteq|supseteq|cong|sqsubseteq|sqsupseteq|bowtie|in|ni|propto|vdash|dashv|models|smile|mid|doteq|frown|parallel|perp|neq|notin|ne|(le)|ge|owns'	
	t.lexer.begin('INITIAL')
	return t

def t_command_FUNC(t):
	r'arccos|arcsin|arctan|arg|cos|cosh|cot|coth|csc|deg|det|dim|exp|gcd|hom|inf|ker|lg|liminf|limsup|ln|log|max|min|Pr|sec|sin|sinh|sup|tan|tanh'
	t.lexer.begin('INITIAL')
	return t

def t_command_NOT(t):
	r'not'
	t.lexer.begin('INITIAL')
	return t

def t_KDELIMITER(t):
	r'\(|\)|\[|\]'
	return t

def t_command_DELIMITER(t):
	r'{|}|lfloor|rfloor|lceil|rceil|langle|rangle|backslash'
	t.lexer.begin('INITIAL')
	return t

def t_command_ACCENT(t):
	r'hat|check|breve|acute|grave|tilde|bar|vec|dot|ddot|widehat|widetilde'
	t.lexer.begin('INITIAL')
	return t

def t_command_STYLE(t):
	r'mathit|mathrm|mathbf|mathsf|mathtt|mathcal|boldmath'
	t.lexer.begin('INITIAL')
	return t

def t_command_LIM(t):
	r'lim'
	t.lexer.begin('INITIAL')
	return t

def t_CHAR(t):
	r'[A-Za-z0-9]+?'
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
while True:
	s = raw_input()
	lexer.input(s)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print tok
