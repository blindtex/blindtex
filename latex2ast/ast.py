#-*-:coding:utf-8-*-
class AST():

    # Attributes of Math Object proposed by Raman
    left_superscript = None
    left_subscript = None
    accent = None
    underbar = None
    superscript = None
    subscript = None
    left_delimiter = None
    right_delimiter = None
    content = None
    type_node = None

class Node(AST):
    def __init__(self,left,content,right,
                 left_superscript = None,
                 left_subscript = None,
                 accent = None,
                 underbar = None,
                 superscript = None,
                 subscript = None,
                 left_delimiter = None,
                 right_delimiter = None):
        self.left = left
        self.right = right
        self.content = content
        self.type_node = 'parent'

        # Math Objet's Attributes
        self.left_superscript = left_superscript
        self.left_subscript = left_subscript
        self.accent = accent
        self.underbar = underbar
        self.superscript = superscript
        self.subscript = subscript
        self.left_delimiter = left_delimiter
        self.right_delimiter = right_delimiter

class Child(AST):
    def __init__(self,content,
                 left_superscript = None,
                 left_subscript = None,
                 accent = None,
                 underbar = None,
                 superscript = None,
                 subscript = None,
                 left_delimiter = None,
                 right_delimiter = None):
        self.content = content
        self.type_node = 'leaf'

        # Math Objet's Attributes
        self.left_superscript = left_superscript
        self.left_subscript = left_subscript
        self.accent = accent
        self.underbar = underbar
        self.superscript = superscript
        self.subscript = subscript
        self.left_delimiter = left_delimiter
        self.right_delimiter = right_delimiter

def lineal_read(node):
    temp_string = ""
    if(node != None):
        if(node.type_node != 'leaf'):
            # Go into left child
            temp_string = temp_string + str(lineal_read(node.left))
            # Read parent node content
            temp_string = temp_string + str(node.content)
            # Read superscript
            if(node.superscript != None):
                temp_string = temp_string + str(lineal_read(node.superscript))
            # Go into left child
            temp_string = temp_string + str(lineal_read(node.right))
        else:
            temp_string = str(node.content)

    return temp_string

def interpreter(tree):
    #print(tree.type)
    return(lineal_read(tree))
