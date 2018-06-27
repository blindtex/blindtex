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

class Node(AST):
    def __init__(self,
                 content = None,
                 children = None,
                 left_superscript = None,
                 left_subscript = None,
                 accent = None,
                 underbar = None,
                 superscript = None,
                 subscript = None,
                 left_delimiter = None,
                 right_delimiter = None,
		 style = None):
        self.children = None #These are the children of the node in a list.
        self.content = content

        # Math Objet's Attributes
        self.left_superscript = left_superscript
        self.left_subscript = left_subscript
        self.accent = accent
        self.underbar = underbar
        self.superscript = superscript
        self.subscript = subscript
        self.left_delimiter = left_delimiter
        self.right_delimiter = right_delimiter
        self.style = style
    
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


#def inoder_read(node):
#    temp_string = ""
#    if(node is not None):
#        if(node.type_node == 'parent'):
#            # Go into left child
#            temp_string = temp_string + str(inoder_read(node.left))
#            # Read parent node content
#            temp_string = temp_string + ',' + str(node.content) + ','
#            # Read superscript
#            if(node.superscript != None):
#                temp_string = temp_string + '^' + str(inoder_read(node.superscript))
#            # Go into left child
#            temp_string = temp_string + str(inoder_read(node.right))
#        else:
#            temp_string = str(node.content)
#
#    return temp_string
#
#def interpreter(tree):
#    return(inoder_read(tree))
