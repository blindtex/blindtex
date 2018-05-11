#-*-:coding:utf-8-*-
#Parser

import ply.yacc as yacc
from dictionary import *
#from lexer import tokens
#import lexer
import blindtex_lexer
#from blindtex_lexer import tokens
import ply.lex
import formulate
import os
import sys
import re
import copy
#TODO: Avoid this.
try:
    sys.path.insert(0, 'blindtex')
    from iotools.stringtools import reportProblem
except ValueError:
    from iotools.stringtools import reportProblem

#--------------------------------------------------------------------------
#Variables dirección del los json

tokens = blindtex_lexer.tokens
#Lista de objetos diccionario:
dOrdinary = json.loads("{\"sharp\": [0, [\"sostenido\"]], \"tau\": [0, [\"tau\"]], \"xi\": [0, [\"xi\"]], \"partial\": [0, [\"parcial\"]], \"exists\": [0, [\"existe\"]], \"flat\": [0, [\"bemol\"]], \"diamondsuit\": [0, [\"diamante\"]], \"clubsuit\": [0, [\"trebol\"]], \"surd\": [0, [\"ra&iacute;z\"]], \"vp\": [0, [\"p caligr&aacute;fica\"]], \"Re\": [0, [\"parte real\"]], \"lnot\": [0, [\"negaci&oacute;n\"]], \"emptyset\": [0, [\"conjunto vac&iacute;o\"]], \"upsilon\": [0, [\"ipsilon\"]], \"Theta\": [0, [\"teta may&uacute;scula\"]], \"zeta\": [0, [\"zeta\"]], \"Pi\": [0, [\"pi may&uacute;scula\"]], \"spadsuit\": [0, [\"picas\"]], \"Phi\": [0, [\"fi may&uacute;scula\"]], \"Psi\": [0, [\"psi may&uacute;scula\"]], \"Sigma\": [0, [\"sigma may&uacute;scula\"]], \"ell\": [0, [\"ele caligr&aacute;fica\"]], \"chi\": [0, [\"ji\"]], \"top\": [0, [\"transpuesto\"]], \"varphi\": [0, [\"var fi\"]], \"varpi\": [0, [\"var pi\"]], \"natural\": [0, [\"becuadro\"]], \"Delta\": [0, [\"delta may&uacute;scula\"]], \"theta\": [0, [\"teta\"]], \"imath\": [0, [\"i caligr&aacute;fica, sin punto\"]], \"pi\": [0, [\"pi\"]], \"Omega\": [0, [\"omega may&uacute;scula\"]], \"iota\": [0, [\"iota\"]], \"infty\": [0, [\"infinito\"]], \"phi\": [0, [\"fi\"]], \"psi\": [0, [\"psi\"]], \"triangle\": [0, [\"tri&aacute;ngulo\"]], \"Upsilon\": [0, [\"ipsilon may&uacute;scula\"]], \"epsilon\": [0, [\"epsilon\"]], \"varrho\": [0, [\"var ro\"]], \"heartsuit\": [0, [\"coraz&oacute;n\"]], \"backslash\": [0, [\"barra invertida\"]], \"varsigma\": [0, [\"var sigma\"]], \"beta\": [0, [\"beta\"]], \"aleph\": [0, [\"alef\"]], \"rho\": [0, [\"ro\"]], \"delta\": [0, [\"delta\"]], \"alpha\": [0, [\"alfa\"]], \"omega\": [0, [\"omega\"]], \"Gamma\": [0, [\"gama may&uacute;scula\"]], \"Lambda\": [0, [\"lambda may&uacute;scula\"]], \"prime\": [0, [\"prima\"]], \"varepsilon\": [0, [\"var epsilon\"]], \"jmath\": [0, [\"j caligr&aacute;fica, sin punto\"]], \"Xi\": [0, [\"xi may&uacute;scula\"]], \"kappa\": [0, [\"kappa\"]], \"vartheta\": [0, [\"var teta\"]], \"angle\": [0, [\"&aacute;ngulo\"]], \"nabla\": [0, [\"nabla\"]], \"bot\": [0, [\"perpendicular\"]], \"nu\": [0, [\"ni\"]], \"mu\": [0, [\"mi\"]], \"eta\": [0, [\"eta\"]], \"Im\": [0, [\"parte imaginaria\"]], \"neg\": [0, [\"negaci&oacute;n\"]], \"forall\": [0, [\"para todo\"]], \"hbar\": [0, [\"hache barra\"]], \"sigma\": [0, [\"sigma\"]], \"|\": [0, [\"norma\", \"paralelo\"]], \"gamma\": [0, [\"gamma\"]], \"lambda\": [0, [\"lambda\"]]}")
dLargeOperators = json.loads("{\"bigotimes\": [0, [\"prducto tensorial\"]], \"coprod\": [0, [\"coproducto\"]], \"iiiint\": [0, [\"cuadruple integral\"]], \"idotsint\": [0, [\"multiples integrales\"]], \"limits\": [0, [\"\"]], \"int\": [0, [\"integral\"]], \"sum\": [0, [\"suma\"]], \"bigodot\": [0, [\"circumpunto\"]], \"bigcup\": [0, [\"uni&oacute;n\"]], \"iiint\": [0, [\"triple integral\"]], \"biguplus\": [0, [\"uni&oacute;n con suma\"]], \"bigcap\": [0, [\"intersecci&oacute;n\"]], \"bigoplus\": [0, [\"circumsuma\"]], \"oint\": [0, [\"integral de contorno\"]], \"iint\": [0, [\"doble integral\"]], \"bigvee\": [0, [\"disyunci&oacute;n\"]], \"bigsqcup\": [0, [\"Uni&oacute;n rect&aacute;ngular\"]], \"prod\": [0, [\"producto\"]], \"bigwedge\": [0, [\"conjunci&oacute;n\"]]}")
dBinaryOperators = json.loads("{\"wedge\": [0, [\"conjunci&oacute;n\"]], \"diamond\": [0, [\"operaci&oacute;n diamante\"]], \"star\": [0, [\"estrella\"]], \"amalg\": [0, [\"amalgamaci&oacute;n\"]], \"ast\": [0, [\"asterisco\"]], \"odot\": [0, [\"circunpunto\"]], \"bmod\": [0, [\"m&oacute;dulo\"]], \"triangleleft\": [0, [\"tri&aacute;angulo a la izquierda\"]], \"bigtriangleup\": [0, [\"tri&aacute;ngulo grande hacia arriba\"]], \"ominus\": [0, [\"circunresta\"]], \"ddagger\": [0, [\"doble daga\"]], \"wr\": [0, [\"producto corona\"]], \"otimes\": [0, [\"circuncruz\"]], \"sqcup\": [0, [\"uni&oacute;n rect&aacute;ngular\"]], \"oplus\": [0, [\"circunsuma\"]], \"cap\": [0, [\"intersecci&oacute;n\"]], \"bigcirc\": [0, [\"c\u00edrculo grande\"]], \"oslash\": [0, [\"circunbarra\"]], \"lor\": [0, [\"disyunci&oacute;n\"]], \"land\": [0, [\"conjunci&oacute;n\"]], \"sqcap\": [0, [\"intersecci&oacute;n rect&aacute;ngular\"]], \"bullet\": [0, [\"c&iacute;rculo relleno\"]], \"cup\": [0, [\"uni&oacute;n\"]], \"cdot\": [0, [\"punto\"]], \"+\": [0, [\"m&aacute;s\"]], \"*\": [0, [\"por\"]], \"-\": [0, [\"menos\"]], \"bigtriangledown\": [0, [\"tri&aacute;ngulo grande hacia abajo\"]], \"/\": [0, [\"dividido entre\"]], \"times\": [0, [\"producto\"]], \"setminus\": [0, [\"diferencia conjuntos\"]], \"circ\": [0, [\"c&iacute;rculo\"]], \"vee\": [0, [\"disyunci&oacute;n\"]], \"uplus\": [0, [\"uni&oacute;n con suma\"]], \"mp\": [0, [\"menos m&aacute;s\"]], \"dagger\": [0, [\"daga\"]], \"triangleright\": [0, [\"tri&aacute;ngulo a la derecha\"]], \"div\": [0, [\"dividido entre\"]], \"pm\": [0, [\"m&aacute;s menos\"]]}")
dBinaryRelations = json.loads("{\"subset\": [0, [\"subconjunto\"]], \"geq\": [0, [\"mayor igual\"]], \"notin\": [0, [\"no est&aacute; en\"]], \"propto\": [0, [\"proporcional\"]], \"bowtie\": [0, [\"junta\"]], \"ne\": [0, [\"no igual\"]], \"supset\": [0, [\"superconjunto\"]], \"cong\": [0, [\"congruente\"]], \"succeq\": [0, [\"sucede igual\"]], \"frown\": [0, [\"fruncido\"]], \"dashv\": [0, [\"deducido\"]], \"gg\": [0, [\"mucho mayor\"]], \"leq\": [0, [\"menor igual\"]], \"succ\": [0, [\"sucede\"]], \"vdash\": [0, [\"deduce\"]], \"asymp\": [0, [\"asint&oacute;tico\"]], \"simeq\": [0, [\"similar igual\"]], \"subseteq\": [0, [\"subconjunto igual\"]], \"parallel\": [0, [\"paralelo\"]], \"equiv\": [0, [\"equivalente\"]], \"ni\": [0, [\"contiene a\"]], \"ge\": [0, [\"mayor igula\"]], \"le\": [0, [\"menor igual\"]], \"in\": [0, [\"est&aacute; en\"]], \"approx\": [0, [\"aproximado\"]], \"preceq\": [0, [\"precede igual\"]], \"ll\": [0, [\"mucho menor\"]], \"mid\": [0, [\"medio\"]], \"prec\": [0, [\"precede\"]], \"sqsupseteq\": [0, [\"superconjunto rect&aacute;ngular\"]], \"models\": [0, [\"modela\"]], \"perp\": [0, [\"perpendicular\"]], \"doteq\": [0, [\"igual puntuado\"]], \"sqsubseteq\": [0, [\"subconjunto rect&aacute;ngular\"]], \"owns\": [0, [\"contiene\"]], \"smile\": [0, [\"sonrisa\"]], \"supseteq\": [0, [\"super conjunto igual\"]], \"neq\": [0, [\"no igual\"]], \"=\": [0, [\"igual\"]], \"<\": [0, [\"menor\"]], \"sim\": [0, [\"similar\"]], \">\": [0, [\"mayor\"]]}")
dMathFunctions = json.loads("{\"Pr\": [0, [\"probabilidad\"]], \"cosh\": [0, [\"coseno hiperb&oacute;lico\"]], \"sec\": [0, [\"secante\"]], \"arg\": [0, [\"argumento\"]], \"inf\": [0, [\"infimo\"]], \"tan\": [0, [\"tangente\"]], \"lg\": [0, [\"logaritmo binario\"]], \"gcd\": [0, [\"mayor com&uacute;n divisor\"]], \"min\": [0, [\"mi&iacute;nimo\"]], \"ln\": [0, [\"logaritmo natural\"]], \"hom\": [0, [\"homomorfismo\"]], \"csc\": [0, [\"cosecante\"]], \"arctan\": [0, [\"arco tangente\"]], \"sup\": [0, [\"supremo\"]], \"sin\": [0, [\"seno\"]], \"limsup\": [0, [\"lim sup\"]], \"liminf\": [0, [\"lim inf\"]], \"arcsin\": [0, [\"arco seno\"]], \"max\": [0, [\"m&aacute;ximo\"]], \"sinh\": [0, [\"seno hiperb&oacute;lico\"]], \"ker\": [0, [\"n&uacute;cleo\"]], \"coth\": [0, [\"cotangente hiperb&oacute;lico\"]], \"log\": [0, [\"logaritmo\"]], \"dim\": [0, [\"dimenci&oacute;n\"]], \"cos\": [0, [\"coseno\"]], \"cot\": [0, [\"cotangente\"]], \"tanh\": [0, [\"tangente hiperb&oacute;lico\"]], \"det\": [0, [\"determinante\"]], \"exp\": [0, [\"exponencial\"]], \"arccos\": [0, [\"arco coseno\"]], \"deg\": [0, [\"grado\"]]}")
dArrows = json.loads("{\"searrow\": [0, [\"flecha diagonal abajo derecha\"]], \"updownarrow\": [0, [\"flecha arriba abajo\"]], \"Uparrow\": [0, [\"flecha arriba doble\"]], \"longleftrightarrow\": [0, [\"flecha izquierda derecha larga\"]], \"Leftarrow\": [0, [\"flecha izquierda doble\"]], \"longmapsto\": [0, [\"env&iacute;a largo\"]], \"nearrow\": [0, [\"flecha diagonal arriba derecha\"]], \"longleftarrow\": [0, [\"flecha izquierda larga\"]], \"uparrow\": [0, [\"flecha arriba\"]], \"hookleftarrow\": [0, [\"flecha  garfio izquierda\"]], \"downarrow\": [0, [\"flecha abajo\"]], \"Leftrightarrow\": [0, [\"flecha izquierda derecha doble\"]], \"longrightarrow\": [0, [\"flecha derecha larga\"]], \"rightharpoondown\": [0, [\"arp&acute;n abajo derecho\"]], \"rightarrow\": [0, [\"flecha derecha\"]], \"Updownarrow\": [0, [\"flecha arriba abajo doble\"]], \"rightharpoonup\": [0, [\"arp&oacute;n arriba derecho\"]], \"Longleftrightarrow\": [0, [\"flecha izquierda derecha doble larga\"]], \"leftarrow\": [0, [\"flecha izquierda\"]], \"mapsto\": [0, [\"env&iacute;a\"]], \"nwarrow\": [0, [\"flecha diagonal arriba izquierda\"]], \"Longleftarrow\": [0, [\"flecha izquierda doble larga\"]], \"leftharpoonup\": [0, [\"arp&oacute;n arriba izquierdo\"]], \"leftharpoondown\": [0, [\"arp&oacute;n abajo izquierda\"]], \"to\": [0, [\"hacia\"]], \"iff\": [0, [\"si y solo si\"]], \"Downarrow\": [0, [\"flecha abajo doble\"]], \"leftrightarrow\": [0, [\"flecha izquierda derecha\"]], \"Longrightarrow\": [0, [\"flecha derecha doble larga\"]], \"swarrow\": [0, [\"flecha diagonal abajo izquierda\"]], \"gets\": [0, [\"obtiene\"]], \"rightleftharpoons\": [0, [\"arp&oacute;n izquierda derecha\"]], \"hookrightarrow\": [0, [\"flecha garfio derecha\"]], \"Rightarrow\": [0, [\"flecha derecha doble\"]]}")
dDelimiters = json.loads("{\"lfloor\": [0, [\"abre piso\"]], \"backslash\": [0, [\"barra invertida\"]], \"rfloor\": [0, [\"cierra piso\"]], \"rangle\": [0, [\"cierra &aacute;ngulo\"]], \"[\": [0, [\"abre corchete\"]], \"]\": [0, [\"cierra corchete\"]], \"lceil\": [0, [\"abre techo\"]], \"langle\": [0, [\" abre &aacute;ngulo\"]], \")\": [0, [\"cierra par&eacute;ntesis\"]], \"rceil\": [0, [\"cierra techo\"]], \"(\": [0, [\"abre par&eacute;ntesis\"]], \"{\": [0, [\"abre llave\"]], \"}\": [0, [\"cierra llave\"]], \"vert\" : [0,[\"barra vertical\"]]}")
dAccents = json.loads("{\"tilde\": [0, [\"virgulilla\"]], \"widetilde\": [0, [\"virgulilla\"]], \"ddot\": [0, [\"doble punto\"]], \"breve\": [0, [\"breve\"]], \"check\": [0, [\"anticircunflejo\"]], \"grave\": [0, [\"grave\"]], \"acute\": [0, [\"agudo\"]], \"bar\": [0, [\"barra\"]], \"widehat\": [0, [\"gorro\"]], \"vec\": [0, [\"vecctor\"]], \"hat\": [0, [\"gorro\"]], \"dot\": [0, [\"punto\"]]}")
dStyles = json.loads("{\"mathbf\": [0, [\"negrilla\"]], \"mathit\": [0, [\"it&aacute;lica\"]], \"mathsf\": [0, [\"sans serif\"]], \"mathcal\": [0, [\"caligr&aacute;fica\"]], \"boldmath\": [0, [\"negrilla\"]], \"mathtt\": [0, [\"m&aacute;quina escribir\"]], \"mathrm\": [0, [\"roman\"]]}")
dDots = json.loads("{\"dots\": [0, [\"puntos\"]], \"cdots\": [0, [\"puntos centrados\"]], \"ddots\": [0, [\"puntos diagonales\"]], \"ldots\": [0, [\"puntos bajos\"]], \"vdots\": [0, [\"puntos verticales\"]]}")
dUser = json.loads("{}")
###########
dictOfDicts = json.loads("{\"Dots\": \"dots|ldots|cdots|vdots|ddots\", \
 \"Styles\": \"mathit|mathrm|mathbf|mathsf|mathtt|mathcal|boldmath\", \
 \"LargeOperators\": \"sum|prod|coprod|int|oint|bigcap|bigcup|bigsqcup|bigvee|bigwedge|bigodot|bigotimes|bigoplus|biguplus|limits\", \
 \"Delimiters\": \"{|}|lfloor|rfloor|lceil|rceil|langle|rangle|backslash|vert\", \
 \"Arrows\": \"leftarrow|Leftarrow|rightarrow|Rightarrow|leftrightarrow|Leftrightarrow|mapsto|hookleftarrow|leftharpoonup|leftharpoondown|rightleftharpoons|longleftarrow|Longleftarrow|longrightarrow|Longrightarrow|longleftrightarrow|Longleftrightarrow|longmapsto|hookrightarrow|rightharpoonup|rightharpoondown|uparrow|Uparrow|downarrow|Downarrow|updownarrow|Updownarrow|nearrow|searrow|swarrow|nwarrow|to|gets|iff\", \
 \"Accents\": \"hat|check|breve|acute|grave|tilde|bar|vec|dot|ddot|widehat|widetilde\", \
 \"MathFunctions\": \"arccos|arcsin|arctan|arg|cos|cosh|cot|coth|csc|deg|det|dim|exp|gcd|hom|inf|ker|lg|liminf|limsup|ln|log|max|min|Pr|sec|sin|sinh|sup|tan|tanh\", \
 \"BinaryOperators\": \"pm|mp|setminus|cdot|times|ast|star|diamond|circ|bullet|div|cap|cup|uplus|sqcap|sqcup|triangleleft|triangleright|wr|bigcirc|bigtriangleup|bigtriangledown|vee|wedge|oplus|ominus|otimes|oslash|odot|dagger|ddagger|amalg|lor|land|bmod\", \
 \"UserDict\": \"SafetyPorpouses\", \
 \"Ordinary\": \"(alpha)|(beta)|gamma|delta|epsilon|varepsilon|zeta|eta|theta|vartheta|iota|kappa|lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|aleph|hbar|imath|jmath|ell|vp|Re|Im|partial|infty|prime|emptyset|nabla|surd|top|bot|\\\\|angle|triangle|backslash|forall|exists|neg|flat|natural|sharp|clubsuit|diamondsuit|heartsuit|spadsuit|lnot|prime\", \
 \"BinaryRelations\": \"leq|geq|equiv|prec|succ|sim|preceq|succeq|simeq|ll|gg|asymp|subset|supset|approx|subseteq|supseteq|cong|sqsubseteq|sqsupseteq|bowtie|in|ni|propto|vdash|dashv|models|smile|mid|doteq|frown|parallel|perp|neq|notin|ne|(le)|ge|owns\"}")
##########

#-------------------------------------------------------------------------------
#TODO Find a way to avoid global variables.
OPTION = 1 #This option are for the formulate function. 0 is for span and &nbsp , 1 is for literal translation and 2 is for math and nbsp.

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


def p_textBlock(p):
    '''textBlock : TEXT any '''
    p[0] = 'texto ' + p[2] + ' fin texto'

def p_label(p):
    '''label : LABEL any '''
    p[0] = p[2]

def p_ARRAYTEXT(p):
    '''textBlock : ARRAYTEXT any'''
    p[0] = p[2] + ' '

def p_any(p):
    '''any : ANYTHING
            | ANYTHING any'''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]



def p_content(p):
    '''content : block
                | scripted
                | command
                | content content
                | larop
                | label'''
    if(len(p) == 3):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_char(p):
    '''char : CHAR
            | ord'''
    p[0] = p[1] + ' '

def p_num(p):
    '''num : NUM '''
    p[0] =p[1]

def p_ord(p):
    '''ord : ORD '''
    p[0] =  p[1]#--->Los operadores son la llave y el valor por defecto que esté en la lectura


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
                | phantom
                | textBlock
                | user
                | num'''
    p[0] = p[1]

#------------------------------------------------------------------------------------------------------


#TODO Que se pueda cambiar de lenguaje o lecturar en los aria-labels; tal vez que p[0] = "una función que depende de los otros p[i]".

#TODO: Que se pueda poner script si algo antes.
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
        p[0] = p[1] + 's&uacute;per' + p[3] + 'fin s&uacute;per'
    else:
        p[0] = p[1] + 'sub' + p[3] + 'fin sub'
#All this pain in the arse is for the Large operator issue. Remember, remember the largeoperator.
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
        p[0] =  p[1] + 's&uacute;per' + p[3] + 'fin s&uacute;per' + 'sub' + p[5] + 'fin sub'
    else:
        p[0] = p[1] + 'sub' + p[3] + 'fin sub' + 's&uacute;per' + p[5] + 'fin s&uacute;per'

#TODO Poder poner LargeOP en esta regla.
def p_simpleFrac(p):
    '''frac : FRAC command command '''
    p[0] = p[2] + 'sobre' + p[3]

def p_frac(p):
    '''frac : FRAC command block
                | FRAC block command
                | FRAC block block'''
    p[0] = 'comienza fracci&oacute;n' + p[2] + 'sobre' + p[3] + 'fin fracci&oacute;n'

def p_root(p):
    '''root : ROOT command
            | ROOT block
            | ROOT KDELIMITER content KDELIMITER command
            | ROOT KDELIMITER content KDELIMITER block '''
    if(len(p) == 3):
        p[0] = 'ra&iacute;z cuadrada de' + p[2] + 'termina ra&iacute;z'
    else:
        p[0] = 'ra&iacute;z' + p[3] + 'de' + p[5] + 'termina ra&iacute;z'


def p_binOp(p):
    '''binop : BINOP
                | KBINOP '''
    p[0] = p[1]


def p_binRel(p):
    '''binrel : BINREL
                | KBINREL'''
    p[0] = p[1]

def p_not(p):
    '''not : NOT '''
    p[0]= 'no'

def p_function(p):
    '''function : FUNC '''
    p[0] = p[1]

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
        p[0] = p[1] + ' desde' + p[3] + 'hasta' + p[5] + 'de'
    else:
        p[0] = p[1] + ' desde' + p[5] + 'hasta' + p[3] + 'de'

def p_largeOp(p):
    '''larop : LARGEOP
                | LARGEOP SUB command
                | LARGEOP SUB block'''
    if(len(p)==2):
        p[0]= p[1]
    elif(len(p)==4):
        p[0] = p[1] +' sobre' + p[3] + 'de'

def p_arrow(p):
    '''arrow : ARROW'''
    p[0] = p[1]

def p_delimiter(p):
    '''delimiter : DELIMITER
                    | KDELIMITER '''
    p[0] = p[1]

def p_simpleAccent(p):
    '''accent : ACCENT command'''
    p[0] = p[2] + p[1]

def p_complexAccent(p):
    '''accent : ACCENT block'''
    if(len(p[2]) > 3):
        p[0] = p[1] + p[2] + 'fin ' + p[1]
    else:
        p[0] = p[2] + p[1]

def p_style(p):
    '''style : STYLE command
                | STYLE block '''
    p[0] = p[1] + p[2] + 'fin ' + p[1]

def p_dots(p):
    '''dots : DOTS '''
    p[0] = p[1]

def p_lim(p):
    '''lim : LIM
            | LIM SUB command
            | LIM SUB block '''
    if(len(p) == 4):
        p[0] = 'l&iacute;mite cuando' + p[3] + 'de'
    else:
        p[0] = 'l&iacute;mite de'

def p_unknown(p):
    '''unknown : UNKNOWN'''
    p[0] = p[1]

def p_userCommand(p):
    '''user : USER'''
    p[0] = p[1]
#
def p_array(p):
    '''array : BEGARRAY arrayContent ENDARRAY '''
    p[0] = 'Arreglo\n' + p[2] + 'Fin Arreglo\n'



def p_arrayContent(p):
    '''arrayContent : content'''
    p[0] = p[1]

#
def p_col(p):
    '''col : COL'''
    p[0] = ''

def p_factorial(p):
    '''factorial : '!' '''
    p[0] = 'factorial'

def p_prime(p):
    '''prime : "'" '''
    p[0] = 'prima'

def p_combi(p):
    '''combi : choose
            | binom '''
    p[0] = p[1]

def p_choose(p):
    '''choose : command CHOOSE command
                | command CHOOSE block
                | block CHOOSE command
                | block CHOOSE block'''
    p[0] = 'combinaciones de' + p[1] + 'en' + p[3]

def p_binom(p):
    '''binom : BINOM command command
            | BINOM command block
            | BINOM block command
            | BINOM block block '''
    p[0] = 'combinaciones de' + p[2] + 'en' + p[3]

def p_pmod(p):
    '''pmod : PMOD command'''
    p[0] = 'm&oacute;dulo' + p[2]

def p_blockpmod(p):
    '''pmod : PMOD block'''
    p[0] = 'm&oacute;dulo' + p[2] + 'fin mod'

def p_linebreak(p):
    '''lnbrk : LINEBREAK'''
    p[0] = 'salto de l&iacute;nea'

def p_phantom(p):
    '''phantom : PHANTOM command
                | PHANTOM block'''
    p[0] = ''

#----------------------------Error Handling------------------------------------
class syntaxError(Exception):
        def __init__(self):
                pass

def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        raise syntaxError
        parser.errok()
    else:
        print("Syntax error at EOF")
        raise syntaxError

#-------------------------------------------------------------------------------

parser = yacc.yacc()
arrayRegex = re.compile(r'''((?<!\\)((\\begin\{array\}(\{.*?\})?)))
(.*?)
(?<!\\)(\\end\{array\})|
((?<!\\)\\begin\{[pbBvV]?matrix(\*)?\}(\[.*?\])?(\{.*?\})?)
(.*?)
((?<!\\)\\end\{[pbBvV]?matrix(\*)?\})''',re.DOTALL|re.UNICODE|re.X)
#Be careful with these constants, if you change the arrayRegex they could change.
ARRAY_CONTENT_GROUP = 5
MATRIX_CONTENT_GROUP = 11
def convert(String):
    latex_lexer = blindtex_lexer.get_latex_equation_lexer(dictOfDicts)
    newString = seekAndReplaceMatrices(String)
    try:
        return parser.parse(newString,latex_lexer)
    except ply.lex.LexError:
        reportProblem('LexError in:\n'+newString)
        return('Bad Formula')
    except syntaxError:
        reportProblem('Syntax Error in:\n' + newString)
        return('Bad Formula')
    except blindtex_lexer.illegalCharacter:
        reportProblem('illegal character in:\n' +newString)
        return('Bad Formula')
#EndOfFunction

def seekAndReplaceMatrices(String):

    otherString = copy.deepcopy(String)
    iterator = arrayRegex.finditer(otherString)
    while(True):
        try:
            currentMatch = iterator.next()
            if(currentMatch.group(ARRAY_CONTENT_GROUP) != None):
                GROUP = ARRAY_CONTENT_GROUP
            elif(currentMatch.group(MATRIX_CONTENT_GROUP) != None):
                GROUP = MATRIX_CONTENT_GROUP
            #Else, why are you here?
            arrayStringContent = currentMatch.group(GROUP)
            arrayRows = arrayStringContent.split(r'\\')
            myArray =[]
            for row in arrayRows:
                myArray.append(row.split('&'))
            curRow = 1
            curCol = 1
            newContent = ''
            for row in myArray:
                for col in row:
                    newContent = newContent + r'~text{Elemento %d %d;}'%(curRow, curCol) + col + ';'
                    curCol = curCol + 1
                curCol = 1
                curRow = curRow +1

            otherString = otherString.replace(currentMatch.group(GROUP), newContent)

        except StopIteration:
            break
    return otherString
#EndOFunction
