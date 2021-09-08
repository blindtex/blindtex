#-*-:coding:utf-8-*-
class MathObject():

    def __init__(self,
                 content = None,
                 children = None,
                 left_superscript = None,
                 left_subscript = None,
                 accent = None,
                 above = None,
                 under = None,
                 superscript = None,
                 subscript = None,
                 left_delimiter = None,
                 right_delimiter = None,
                 style = None,
                 kind = None,):

        self.children = children #These are the children of the node in a list.
        self.content = content

        #Attributes of Math Object proposed by Raman
        self.left_superscript = left_superscript
        self.left_subscript = left_subscript
        self.accent = accent
        self.above = above
        self.under = under
        self.superscript = superscript
        self.subscript = subscript
        self.left_delimiter = left_delimiter
        self.right_delimiter = right_delimiter
        self.style = style
        self.kind = kind
        #The kind is the use of the math_object Ord, binary operator, arrow...etc. Just the symbols will have it.
        #This will serve to know beforehand in what dictionary look for and if it has some special behaviour.
        #It is not convenient to put kind in block, fraction, root...etc for the further exploration of the formula.

    def append_child(self, node_new_child):
        if(self.children == None):
            self.children = node_new_child
        else:
            self.children.append(node_new_child)

    #TODO: Verify if the list has de capacity for the index and so.
    def add_child(self, index, node_new_child):
        if(self.children == None):
            self.children = node_new_child
        else:
            self.children.insert(index, node_new_child)

    def get_children(self):
        return self.children
#EndOfClass
