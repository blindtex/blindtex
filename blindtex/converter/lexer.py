#Lexer of LaTeX math content

import ply.lex as lex

tokens = ('CHAR', 'SUP', 'SUB','BEGINBLOCK','ENDBLOCK', 'BEGINSBLOCK','ENDSBLOCK', 'ORD', 'FRAC', 'ROOT', 'LARGEOP', 'BINOP','KBINOP','KBINREL', 'BINREL', 'NOT', 'FUNC')

states = (('command', 'exclusive'),)



def t_BEGINBLOCK(t):
	r'\{'
	return t

def t_ENDBLOCK(t):
	r'\}'
	return t

def t_BEGINSBLOCK(t):
	r'\['
	return t

def t_ENDSBLOCK(t):
	r'\]'
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

def t_command_ORD(t):
	r'(alpha)|(beta)|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|kappa|lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|aleph|hbar|imath|jmath|ell|vp|Re|Im|partial|infty|prime|emptyset|nabla|surd|top|bot|\||angle|triangle|backslash|forall|exists|neg|flat|natural|sharp|clubsuit|diamondsuit|heartsuit|spadsuit'
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

def t_KBINOP(t):#Binary operators that can be made from the keyboard.
	r'\+|-|\*|/'
	return t
	
def t_command_BINOP(t):
	r'pm|mp|setminus|cdot|times|ast|star|diamond|circ|bullet|div|cap|cup|uplus|sqcap|sqcup|triangleleft|triangleright|wr|bigcirc|bigtriangleup|bigtriangledown|vee|wedge|oplus|ominus|otimes|oslash|odot|dagger|ddagger|amalg'
	t.lexer.begin('INITIAL')
	return t

def t_KBINREL(t):
	r'[=<>]'	
	t.lexer.begin('INITIAL')
	return t

def t_command_BINREL(t):
	r'leq|geq|equiv|prec|succ|sim|preceq|succeq|simeq|ll|gg|asymp|subset|supset|approx|subseteq|supseteq|cong|sqsubseteq|sqsupseteq|bowtie|in|ni|propto|vdash|dashv|models|smile|mid|doteq|frown|parallel|perp|neq|notin'	
	t.lexer.begin('INITIAL')
	return t

def t_command_FUNC(t):
	r'arccos|arcsin|arctan|arg|cos|cosh|cot|coth|csc|deg|det|dim|exp|gcd|hom|inf|ker|lg|lim|liminf|limsup|ln|log|max|min|Pr|sec|sin|sinh|sup|tan|tanh'
	t.lexer.begin('INITIAL')
	return t

def t_command_NOT(t):
	r'not'
	t.lexer.begin('INITIAL')
	return t

def t_command_LARGEOP(t):
	r'sum|prod|coprod|int|oint|bigcap|bigcup|bigsqcup|bigvee|bigwedge|bigodot|bigotimes|bigoplus|biguplus'
	t.lexer.begin('INITIAL')
	return t

def t_CHAR(t):
	r'[A-Za-z0-9]+?'
	return t

t_ignore_SPACE=r'[ \t]+'


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
