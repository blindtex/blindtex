#-*-:coding:utf-8-*-

import json
import ply.lex as lex
from ply.lex import TOKEN
import json

tokens = ('CHAR', 'SUP', 'SUB',
          'BEGINBLOCK','ENDBLOCK','ORD',
          'FRAC', 'ROOT', 'LARGEOP',
          'BINOP','KBINOP','KBINREL',
          'BINREL', 'NOT', 'FUNC',
          'ARROW','KDELIMITER','DELIMITER',
          'ACCENT','STYLE','DOTS',
          'LIM','UNKNOWN','BEGARRAY',
          'ENDARRAY','LINEBREAK','COL',
          'CHOOSE','BINOM','PMOD',
          'PHANTOM','TEXT','LABEL',
          'ANYTHING','ARRAYTEXT','USER',
          'NUM')

dictOfDicts = json.loads("{\"Dots\": \"dots|ldots|cdots|vdots|ddots\", \
    \"Styles\": \"mathit|mathrm|mathbf|mathsf|mathtt|mathcal|boldmath\", \
    \"LargeOperators\": \"sum|prod|coprod|int|oint|bigcap|bigcup|bigsqcup|bigvee|bigwedge|bigodot|bigotimes|bigoplus|biguplus|limits\", \"Delimiters\": \"{|}|lfloor|rfloor|lceil|rceil|langle|rangle|backslash|vert\", \
    \"Arrows\": \"leftarrow|Leftarrow|rightarrow|Rightarrow|leftrightarrow|Leftrightarrow|mapsto|hookleftarrow|leftharpoonup|leftharpoondown|rightleftharpoons|longleftarrow|Longleftarrow|longrightarrow|Longrightarrow|longleftrightarrow|Longleftrightarrow|longmapsto|hookrightarrow|rightharpoonup|rightharpoondown|uparrow|Uparrow|downarrow|Downarrow|updownarrow|Updownarrow|nearrow|searrow|swarrow|nwarrow|to|gets|iff\", \
    \"Accents\": \"hat|check|breve|acute|grave|tilde|bar|vec|dot|ddot|widehat|widetilde\", \"MathFunctions\": \"arccos|arcsin|arctan|arg|cos|cosh|cot|coth|csc|deg|det|dim|exp|gcd|hom|inf|ker|lg|liminf|limsup|ln|log|max|min|Pr|sec|sin|sinh|sup|tan|tanh\", \
    \"BinaryOperators\": \"pm|mp|setminus|cdot|times|ast|star|diamond|circ|bullet|div|cap|cup|uplus|sqcap|sqcup|triangleleft|triangleright|wr|bigcirc|bigtriangleup|bigtriangledown|vee|wedge|oplus|ominus|otimes|oslash|odot|dagger|ddagger|amalg|lor|land|bmod\", \
    \"UserDict\": \"SafetyPorpouses\", \
    \"Ordinary\": \"(alpha)|(beta)|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|kappa|lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|aleph|hbar|imath|jmath|ell|vp|Re|Im|partial|infty|prime|emptyset|nabla|surd|top|bot|\\\\|angle|triangle|backslash|forall|exists|neg|flat|natural|sharp|clubsuit|diamondsuit|heartsuit|spadsuit|lnot|prime\", \
    \"BinaryRelations\": \"leq|geq|equiv|prec|succ|sim|preceq|succeq|simeq|ll|gg|asymp|subset|supset|approx|subseteq|supseteq|cong|sqsubseteq|sqsupseteq|bowtie|in|ni|propto|vdash|dashv|models|smile|mid|doteq|frown|parallel|perp|neq|notin|ne|(le)|ge|owns\"}")

def get_lexer():

    states = (('command', 'exclusive'),#)
              ('anything','exclusive'),)

    literals = [ '!',"'",]

    BEGINBLOCK = r'\{'
    ENDBLOCK = r'\}'
    SUP = r'\^'
    SUB = r'_'
    COMMAND = r'\\'
    command_PMOD = r'pmod'
    command_PHANTOM = r'[hv]?phantom'
    command_BEGARRAY = r'(begin\{array\}|begin\{[pbBvV]?matrix(\*)?\})(\[.*?\])?(\{.*?\})?'
    command_ENDARRAY = r'end\{array\}|end\{[pbBvV]?matrix(\*)?\}'
    command_LINEBREAK = r'\\'
    COL = r'[&]'
    #command_LARGEOP =
    #command_ORD =
    command_FRAC = r'frac|tfrac|dfrac'
    command_ROOT = r'sqrt'
    #command_ARROW =
    command_leftRight = r'(left)|(right)|left\.|right\.'
    KBINOP = r'\+|-|\*|/'
    #command_DOTS =
    #command_BINOP =
    KBINREL = r'[=<>]'
    #command_BINREL =
    #command_FUNC =
    command_NOT = r'not'
    KDELIMITER = r'\(|\)|\[|\]'
    #command_DELIMITER =
    #command_ACCENT =
    #command_STYLE =
    command_LIM = r'lim'
    command_CHOOSE = r'choose'
    command_BINOM = r'binom'
    command_MATHSPACE = r'[,!:;]|quad|qquad'
    command_TEXT = r'(text(rm)?|mbox)\{'
    command_LABEL = r'label\{'
    ARRAYTEXT = r'~text\{'
    anything_ANYTHING = r'[^}]'
    anything_ENDANY = r'(?<!\\)\}'
    CHAR = r'[A-Za-z"%\',.:;|]+?'
    #NUM = r'[0-9]?'
    NUM = r'[0-9]{1,}' # Extraer numeros de 1 o mas digitos
    #command_USER =
    command_UNKNOWN = r'[A-Za-z]+'
    t_ignore_SPACE=r'[ \t\n]+' #LaTeX does not care about spaces in math mode unless they are specified.

    #dictOfDicts = json.loads("{\"Dots\": \"dots|ldots|cdots|vdots|ddots\", \
    #\"Styles\": \"mathit|mathrm|mathbf|mathsf|mathtt|mathcal|boldmath\", \
    #\"LargeOperators\": \"sum|prod|coprod|int|oint|bigcap|bigcup|bigsqcup|bigvee|bigwedge|bigodot|bigotimes|bigoplus|biguplus|limits\", \"Delimiters\": \"{|}|lfloor|rfloor|lceil|rceil|langle|rangle|backslash|vert\", \
    #\"Arrows\": \"leftarrow|Leftarrow|rightarrow|Rightarrow|leftrightarrow|Leftrightarrow|mapsto|hookleftarrow|leftharpoonup|leftharpoondown|rightleftharpoons|longleftarrow|Longleftarrow|longrightarrow|Longrightarrow|longleftrightarrow|Longleftrightarrow|longmapsto|hookrightarrow|rightharpoonup|rightharpoondown|uparrow|Uparrow|downarrow|Downarrow|updownarrow|Updownarrow|nearrow|searrow|swarrow|nwarrow|to|gets|iff\", \
    #\"Accents\": \"hat|check|breve|acute|grave|tilde|bar|vec|dot|ddot|widehat|widetilde\", \"MathFunctions\": \"arccos|arcsin|arctan|arg|cos|cosh|cot|coth|csc|deg|det|dim|exp|gcd|hom|inf|ker|lg|liminf|limsup|ln|log|max|min|Pr|sec|sin|sinh|sup|tan|tanh\", \
    #\"BinaryOperators\": \"pm|mp|setminus|cdot|times|ast|star|diamond|circ|bullet|div|cap|cup|uplus|sqcap|sqcup|triangleleft|triangleright|wr|bigcirc|bigtriangleup|bigtriangledown|vee|wedge|oplus|ominus|otimes|oslash|odot|dagger|ddagger|amalg|lor|land|bmod\", \
    #\"UserDict\": \"SafetyPorpouses\", \
    #\"Ordinary\": \"(alpha)|(beta)|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|kappa|lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|aleph|hbar|imath|jmath|ell|vp|Re|Im|partial|infty|prime|emptyset|nabla|surd|top|bot|\\\\|angle|triangle|backslash|forall|exists|neg|flat|natural|sharp|clubsuit|diamondsuit|heartsuit|spadsuit|lnot|prime\", \
    #\"BinaryRelations\": \"leq|geq|equiv|prec|succ|sim|preceq|succeq|simeq|ll|gg|asymp|subset|supset|approx|subseteq|supseteq|cong|sqsubseteq|sqsupseteq|bowtie|in|ni|propto|vdash|dashv|models|smile|mid|doteq|frown|parallel|perp|neq|notin|ne|(le)|ge|owns\"}" )

    @TOKEN(BEGINBLOCK)
    def t_BEGINBLOCK(t):
    	return t

    @TOKEN(ENDBLOCK)
    def t_ENDBLOCK(t):
    	return t

    @TOKEN(SUP)
    def t_SUP(t):
    	return t

    @TOKEN(SUB)
    def t_SUB(t):
    	return t

    @TOKEN(COMMAND)
    def t_COMMAND(t):
    	t.lexer.begin('command')
    	return

    @TOKEN(command_PMOD)
    def t_command_PMOD(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_PHANTOM)
    def t_command_PHANTOM(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_BEGARRAY)
    def t_command_BEGARRAY(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_ENDARRAY)
    def t_command_ENDARRAY(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_LINEBREAK)
    def t_command_LINEBREAK(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(COL)
    def t_COL(t):
    	return t

    @TOKEN(dictOfDicts['LargeOperators'])
    def t_command_LARGEOP(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(dictOfDicts['Ordinary'])
    def t_command_ORD(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_FRAC)
    def t_command_FRAC(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_ROOT)
    def t_command_ROOT(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(dictOfDicts['Arrows'])
    def t_command_ARROW(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_leftRight)
    def t_command_leftRight(t):
    	t.lexer.begin('INITIAL')
    	pass

    @TOKEN(KBINOP)
    def t_KBINOP(t):#Binary operators that can be made from the keyboard.
    	return t

    @TOKEN(dictOfDicts['Dots'])
    def t_command_DOTS(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(dictOfDicts['BinaryOperators'])
    def t_command_BINOP(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(KBINREL)
    def t_KBINREL(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(dictOfDicts['BinaryRelations'])
    def t_command_BINREL(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(dictOfDicts['MathFunctions'])
    def t_command_FUNC(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_NOT)
    def t_command_NOT(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(KDELIMITER)
    def t_KDELIMITER(t):
    	return t

    @TOKEN(dictOfDicts['Delimiters'])
    def t_command_DELIMITER(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(dictOfDicts['Accents'])
    def t_command_ACCENT(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(dictOfDicts['Styles'])
    def t_command_STYLE(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_LIM)
    def t_command_LIM(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_CHOOSE)
    def t_command_CHOOSE(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_BINOM)
    def t_command_BINOM(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_MATHSPACE)
    def t_command_MATHSPACE(t):
    	t.lexer.begin('INITIAL')
    	pass

    @TOKEN(command_TEXT)
    def t_command_TEXT(t):
        t.lexer.begin('anything')
        return t

    @TOKEN(command_LABEL)
    def t_command_LABEL(t):
        t.lexer.begin('anything')
        return t

    @TOKEN(ARRAYTEXT)
    def t_ARRAYTEXT(t):
        t.lexer.begin('anything')
        return t

    @TOKEN(anything_ANYTHING)
    def t_anything_ANYTHING(t):
        return t

    @TOKEN(anything_ENDANY)
    def t_anything_ENDANY(t):
        t.lexer.begin('INITIAL')
        pass

    @TOKEN(CHAR)
    def t_CHAR(t):
    	return t

    @TOKEN(NUM)
    def t_NUM(t):
        return t

    @TOKEN(dictOfDicts['UserDict'])
    def t_command_USER(t):
    	t.lexer.begin('INITIAL')
    	return t

    @TOKEN(command_UNKNOWN)
    def t_command_UNKNOWN(t):
    	t.lexer.begin('INITIAL')
    	return t

    def t_command_error(t):
        print("Illegal character '%s'" % t.value[0])
        #t.lexer.skip(1)
        #raise illegalCharacter

    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        #t.lexer.skip(1)
        #raise illegalCharacter

    return lex.lex()

if __name__ =="__main__":
    lexer = get_lexer()
    while True:
        try:
            try:
                s = raw_input()
            except NameError: # Python3
                s = input('spi> ')
        except EOFError:
            break

        lexer.input(s)
        while True:
            tok = lexer.token()
            if not tok:
                break

            print(tok)
