#-*-:coding:utf-8-*-

import ply.lex
import ply.yacc
from blindtex.latex2ast import lexer
from blindtex.latex2ast.math_object import MathObject

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

def p_lnbrk(p):
    '''lnbrk : LINEBREAK '''
    p[0] = MathObject(content = r'\\')

def p_col(p):
    '''col : COL '''
    p[0] = MathObject(content = '&')
    
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
            | label
            | array
            | lnbrk
            | col'''
    p[0] = [p[1]]#It returns a list of one object.

def p_block(p):
    """
    block : BEGINBLOCK formula ENDBLOCK
    """
    p[0] = MathObject(content = 'block')
    p[0].append_child(p[2])

def p_accent(p):
    '''
    math_object : ACCENT block
                    | ACCENT symbol
    '''
    p[2].accent = p[1]
    p[0] = [p[2]]#Are you sure this does not create a conflict if the MathObject is complex?

def p_overset(p):
    '''math_object : OVERSET argument argument '''
    p[3].above = p[2]
    p[0] = [p[3]]#Are you sure this does not create a conflict if the MathObject is complex?

def p_underset(p):
    '''math_object : UNDERSET argument argument '''
    p[3].under = p[2]
    p[0] = [p[3]]#Are you sure this does not create a conflict if the MathObject is complex?

def p_style(p):
    '''
    math_object : STYLE block
                    | STYLE symbol
    '''
    p[2].style = p[1]
    p[0] = [p[2]]#Are you sure this does not create a conflict if the MathObject is complex?

def p_formula_scripted(p):
    '''
    math_object : math_object simple_scripted
                    | math_object compound_scripted
    '''
    p[0] = p[1]

#All the possible things an argument could be.
def p_argument(p):
    '''argument : symbol
                            | block'''
    p[0] = [p[1]]

#All the possible things a scripty may be.
def p_script(p):
    '''script : symbol
                    | block
                    | fraction
                    | root
                    | binom
                    | pmod
                    | text'''
    p[0] = [p[1]]

def p_simple_scripted(p):
    '''
    simple_scripted : SUP script
                                    | SUB script
    '''
    if(p[1] == '^'):
        #This distintion is made for formulas like a^2 ^3 (double scripted)
        #LaTeX accepts them and we have to.
        #Here we create a new Node with content 'nothing_scripted' that will be processed later. 
        if(p[-1][0].superscript == None):
            p[-1][0].superscript = p[2]#Adds the script to the previous element.
        else:
            p[-1].append(MathObject(content = 'nothing_scripted', superscript = p[2]))#What a duct tape fix.
    else:
        if(p[-1][0].subscript == None):
            p[-1][0].subscript = p[2]
        else:
            p[-1].append(MathObject(content = 'nothing_scripted', subscript = p[2]))

def p_compound_scripted(p):
    '''
    compound_scripted : SUP script SUB script
                                    | SUB script SUP script
    '''
    if(p[1] == '^'):
        #See p_simple_scripted
        if(p[-1][0].superscript == None and p[-1][0].subscript == None):
            #If some is not and the parser reached here, something funny is happening.
            p[-1][0].superscript = p[2]
            p[-1][0].subscript = p[4]
        else:
            p[-1].append(Node(content = 'nothing_scripted', superscript = p[2], subscript = p[4]))
    else:
        if(p[-1][0].superscript == None and p[-1][0].subscript == None):
            p[-1][0].subscript = p[2]
            p[-1][0].superscript = p[4]
        else:
            p[-1].append(Node(content = 'nothing_scripted', superscript = p[4], subscript = p[2]))

def p_symbol(p):
    """
    symbol : LIM
            | UNKNOWN
            | MOD
            | "!"
            | NOT
                        | KNOT
                        | USER
    """
    p[0] = MathObject(content = p[1])

def p_ord(p):
    ''' symbol :  ORD '''
    p[0] = MathObject(content = p[1], kind = 'Ordinary')#Beware to distinguish if is in the dictionary or not.

def p_noKind_ord(p):
    '''symbol : NUM
               | CHAR '''
    p[0] = MathObject(content = p[1])

def p_largeOp(p):
    ''' symbol : LARGEOP '''
    p[0] = MathObject(content = p[1], kind = 'LargeOperators')

def p_binop(p):
    ''' symbol : BINOP
                       | KBINOP '''
    p[0] = MathObject(content = p[1], kind = 'BinaryOperators')#Beware to distinguish if is in the dictionary or not.

def p_binrel(p):
    ''' symbol : KBINREL
                            | BINREL'''
    p[0] = MathObject(content = p[1], kind = 'BinaryRelations')#Beware to distinguish if is in the dictionary or not.

def p_func(p):
    ''' symbol : FUNC '''
    p[0] = MathObject(content = p[1], kind = 'MathFunctions')

def p_arrow(p):
    ''' symbol : ARROW '''
    p[0] = MathObject(content = p[1], kind = 'Arrows')

def p_delimiter(p):
    ''' symbol : DELIMITER
                            | kdelimiter '''
    p[0] = MathObject(content = p[1], kind = 'Delimiters')

def p_dots(p):
    ''' symbol : DOTS '''
    p[0] = MathObject(content = p[1], kind = 'Dots')

#We count [ and ] apart because the \sqrt structure uses them.
def p_kdelimiter(p):
    '''kdelimiter : KDELIMITER
                    | "["
                    | "]" '''
    p[0] = p[1]

def p_fraction(p):
    '''fraction : FRAC argument argument '''
    p[0] = MathObject(content = 'fraction')
    p[0].append_child(p[2])
    p[0].append_child(p[3][0]) #This is because p[3] is a list, as index returns that, but we want to append the MathObject, not the list.

def p_root(p):
    '''root : sqr_root
            | indexed_root '''
    p[0] = p[1]

def p_sqr_root(p):
    '''sqr_root : ROOT argument '''
    p[0] = MathObject(content = 'root')
    p[0].append_child(p[2])

def p_indexed_root(p):
    '''indexed_root : ROOT root_index argument '''
    p[0] = MathObject(content = 'root')
    p[0].append_child(p[2])#The first child will be the index.
    p[0].append_child(p[3][0])#This is because p[5] is a list, as index returns that, but we want to append the MathObject, not the list.

#TODO:Here argument must be changed by formula, but this change generates lots of problems.
def p_root_index(p):
    'root_index : "[" argument "]" '
    p[0] = p[2]

def p_choose(p):
    ''' choose : formula CHOOSE formula '''
    p[0] = MathObject(content = 'choose')
    p[0].append_child(p[1])
    p[0].append_child(p[3][0])

#Something funny here. See test_binom
def p_binom(p):
    '''binom : BINOM argument argument '''
    p[0] = MathObject(content = 'binom')
    p[0].append_child(p[2])
    p[0].append_child(p[3][0])

def p_pmod(p):
    ''' pmod : PMOD argument '''
    p[0] = MathObject(content = 'pmod')
    p[0].append_child(p[2])

def p_text(p):
    ''' text : TEXT TCHAR
            | TEXT ANYTHING'''
    p[0] = MathObject(content = 'text')
    p[0].append_child(p[2])

def p_label(p):
    '''label : LABEL '''
    p[0] = MathObject(content = 'label')
    p[0].append_child(p[1])

def p_array(p):
    '''array : BEGARRAY start ENDARRAY '''
    p[0] = MathObject(content = 'array')
    p[0].append_child(p[2])

#Here we have a delay of the problem. If  LINEBREAK is included as the
# row separator there is a conflict with LINEBREAK as symbol in any 
# formula, so, I decided to postpone the row and column finding in the later processes.
#By the moment it creates a large list with all the rows in one.


def get_parser():
    return ply.yacc.yacc()

if __name__ == "__main__":
    parser = get_parser()
    lexer = lexer.get_lexer()
    #cv = parser.parse(latex_string,custom_lexer)#,debug=1)
    while True:
        try:
            try:
                s = raw_input()
            except NameError: # Python3
                s = input('spi> ')

            cv_s = parser.parse(s,lexer)
            print(cv_s)
        except EOFError:
            break
