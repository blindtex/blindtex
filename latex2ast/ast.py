#-*-:coding:utf-8-*-
class AST():
    left_superscript = None
    accent = None
    superscript = None
    left_subscript = None
    underbar = None
    subscript = None

class Node(AST):
    def __init__(self,left,operator,right,type_node):
        self.left = left
        self.right = right
        self.operator = operator
        self.type = type_node

class Child(AST):
    def __init__(self,value,type_node):
        self.value = value
        self.type = type_node

def lineal_read(child):
    temp_string = ""
    if(child.type!='ORDINARY'):
        temp_string = temp_string + str(lineal_read(child.left))
        temp_string = temp_string + str(child.operator)
        temp_string = temp_string + str(lineal_read(child.right))
    else:
        temp_string = str(child.value)

    return temp_string

def interpreter(tree):
    print(dir(tree))
    return(lineal_read(tree))
