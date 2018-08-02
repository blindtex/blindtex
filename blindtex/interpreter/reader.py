#-*-:coding:utf-8-*-
from blindtex.latex2ast import converter
#from latex2ast import ast
from blindtex.interpreter import dictionary
import os
import os.path

DICTSPATH = os.path.join('blindtex', 'lang', 'dicts')

DICTS = {'Accents' : dictionary.dictionary(os.path.join(DICTSPATH,'Accents.json')),
             'Arrows' : dictionary.dictionary(os.path.join(DICTSPATH,'Arrows.json')),
             'BinaryOperators' : dictionary.dictionary(os.path.join(DICTSPATH,'BinaryOperators.json')),
             'BinaryRelations' : dictionary.dictionary(os.path.join(DICTSPATH,'BinaryRelations.json')),
             'Delimiters' : dictionary.dictionary(os.path.join(DICTSPATH,'Delimiters.json')),
             'Dots' : dictionary.dictionary(os.path.join(DICTSPATH,'Dots.json')),
             'LargeOperators' : dictionary.dictionary(os.path.join(DICTSPATH,'LargeOperators.json')),
             'MathFunctions' : dictionary.dictionary(os.path.join(DICTSPATH,'MathFunctions.json')),
             'Ordinary' : dictionary.dictionary(os.path.join(DICTSPATH,'Ordinary.json')),
             'Styles' : dictionary.dictionary(os.path.join(DICTSPATH,'Styles.json')),
             'UserDict' : dictionary.dictionary(os.path.join(DICTSPATH,'UserDict.json')),}



to_read = {'simple_superscript' : 'super %s ',
                'comp_superscript' : 'super %s endsuper ',
                'simple_subscript' : 'sub %s ',
                'comp_subscript' : 'sub %s endsub ',
                'simple_frac' : '%s over %s ',
                'comp_frac' : 'fraction %s over %s endfraction ',
                'simple_sqrt' : 'squarerootof %s ',
                'comp_sqrt' : 'squarerootof %s endroot ',
                'simple_root' : 'root %s of %s ',
                'comp_root' : 'root %s of %s endroot ',
                'simple_choose' : 'from %s choose %s ',
                'comp_choose' : 'from %s choose %s end ',
                'simple_modulo' : 'modulo %s ',
                'comp_modulo' : 'modulo %s end ',
                'simple_text' : 'text %s ',
                'comp_text' : 'text %s endtext ',
                'from_to' : 'from %s to %s of ',
                'over' : 'over %s of ',
                'to' : 'to %s of ',
                'end' : 'end%s '}

def lineal_read(Node):
    #Dictionary with the possible nodes with children and the functions each case call.
    with_children = {'block' : lineal_read_block,
                     'fraction' : lineal_read_fraction,
                     'root' : lineal_read_root,
                     'choose' : lineal_read_choose_binom,
                     'binom' : lineal_read_choose_binom,
                     'pmod' : lineal_read_pmod,
                     'text' : lineal_read_text,
                     'label' : lineal_read_label}

    str_lineal_read = ''

    #The attributes will be readed in this order:
    # accent -> content-> children* -> style -> superscript -> subscript
    #TODO: Add the option for the user to change this.
    #TODO: Add the option to ommit style or whatever.
    #TODO: Add the translation by dictionary.


    
    #I'll go for the easiest and less elegant way: A chain of ifs.
    if(Node.content in with_children):
        #Identify the type of children the node has and act accordingly
        str_lineal_read = str_lineal_read + with_children[Node.content](Node.children)
    else:
        str_lineal_read = str_lineal_read + lineal_read_content(Node)

    if(Node.style != None):
        str_lineal_read = lineal_read_style(Node, str_lineal_read)

    if(Node.accent != None):
        str_lineal_read = lineal_read_accent(Node, str_lineal_read)

    #This part is to read the limits of large Operators like integral or sum.
    if(Node.kind == 'LargeOperators'):
        if(Node.subscript != None and Node.superscript != None):
            str_lineal_read = str_lineal_read + to_read['from_to']%(lineal_read(Node.subscript[0]),
                                                                    lineal_read(Node.superscript[0]))
        elif(Node.subscript != None and Node.superscript == None):
            str_lineal_read = str_lineal_read + to_read['over']%lineal_read(Node.subscript[0])

        elif(Node.subscript == None and Node.superscript != None):
            str_lineal_read = str_lineal_read + to_read['to']%lineal_read(Node.superscript[0])
    else:
        if(Node.superscript != None):
            str_lineal_read = str_lineal_read + lineal_read_superscript(Node.superscript[0])

        if(Node.subscript != None):
            str_lineal_read = str_lineal_read + lineal_read_subscript(Node.subscript[0])

    return str_lineal_read
#EndOfFunction

def lineal_read_content(node):
    if(node.kind != None):
        return '%s '%DICTS[node.kind].showReading(node.content)
    else:
        return '%s '%node.content
#EOF

def lineal_read_accent(node, str_read):
    node_accent = DICTS['Accents'].showReading(node.accent)
    if(is_simple(node)):
        return str_read + '%s '%node_accent
    else:
        return '%s '%node_accent + str_read + to_read['end']%node_accent    
#EOF

def lineal_read_style(node, str_read):
    node_style = DICTS['Styles'].showReading(node.style)
    if(is_simple(node)):
        return str_read + '%s '%node_style
    else:
        return '%s '%node_style + str_read + to_read['end']%node_style
#EOF

def lineal_read_superscript(node_script):
    #Here if the script is a block it will be considered as a compound script.
    #This to avoid the following ambiguity: a^{b_c} and a^b_c
    #That, otherwise, would be read the same.
    if(is_simple(node_script) and node_script.content != 'block'):
        return to_read['simple_superscript']%lineal_read(node_script)
    else:
        return to_read['comp_superscript']%lineal_read(node_script)
#EndOfFunction

def lineal_read_subscript(node_script):
    #See lineal_read_superscript.
    if(is_simple(node_script) and node_script.content != 'block'):
        return to_read['simple_subscript']%lineal_read(node_script)
    else:
        return to_read['comp_subscript']%lineal_read(node_script)
#EndOfFunction


def is_simple(Node):
    if(Node.get_children() == None):
        return True
    elif(Node.content == 'block' and len(Node.get_children()) == 1 ):
        return(is_simple(Node.get_children()[0]))#This is for cases like {{a+b}} (not simple) or {{{\alpha}}}(simple).
    else:
        return False
#EndOfFunction

def lineal_read_block(list_children):
    # The child of a block is a formula, a formula is a list of nodes.
    str_result = ''
    for node in list_children:
        str_result = str_result + lineal_read(node)

    return str_result
#EndOfFunction

def lineal_read_fraction(list_children):
    #The list received here must be of lenght 2. The numerator and denominator.
    if(is_simple(list_children[0]) and is_simple(list_children[1])):
        return to_read['simple_frac']%(lineal_read(list_children[0]), lineal_read(list_children[1]))
    else:
        return to_read['comp_frac']%(lineal_read(list_children[0]), lineal_read(list_children[1]))
#EndOfFunction

def lineal_read_root(list_children):
    #There are two cases here: Either the root has an index \sqrt[i]{k} or not.
    if(len(list_children) == 1):#It has not index
        if(is_simple(list_children[0])):
            return to_read['simple_sqrt']%(lineal_read(list_children[0]))
        else:
            return to_read['comp_sqrt']%(lineal_read(list_children[0]))
    else:
        if(is_simple(list_children[1])):
            return to_read['simple_root']%(lineal_read(list_children[0]), lineal_read(list_children[1]))
        else:
            return to_read['comp_root']%(lineal_read(list_children[0]), lineal_read(list_children[1]))
#EndOfFunction

def lineal_read_choose_binom(list_children):
    if(is_simple(list_children[0]) and is_simple(list_children[1])):
        return to_read['simple_choose']%(lineal_read(list_children[0]), lineal_read(list_children[1]))
    else:
        return to_read['comp_choose']%(lineal_read(list_children[0]), lineal_read(list_children[1]))
#EndOfFunction

def lineal_read_pmod(list_children):
    if(is_simple(list_children[0])):
        return to_read['simple_modulo']%(lineal_read(list_children[0]))
    else:
        return to_read['comp_modulo']%(lineal_read(list_children[0]))
#EndOfFunction

def lineal_read_text(list_children):
    return 'text %s endtext'%(list_children)#Here the child is a string
#EndOfFunction

def lineal_read_label(list_children):
    return r'\%s'%(list_children)#The labels must be inaltered.
#EndOFFunction

def lineal_read_formula(list_formula):
    str_result = ''
    for node in list_formula:
        str_result = str_result + lineal_read(node)
    return str_result
#EndOfFunction

def lineal_read_formula_list(list_formula):
    str_result = ''
    for node in list_formula:
        str_result = str_result + lineal_read(node)
    return str_result.split()
#EndOfFunction


if __name__ == "__main__":
    while True:
        try:
            try:
                s = raw_input()
            except NameError: # Python3
                s = input('spi> ')

            cv_s = converter.latex2list(s)
            print(lineal_read_formula(cv_s))
        except EOFError:
            break