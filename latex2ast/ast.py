#-*-:coding:utf-8-*-
class Expr: pass

class Node(Expr):
    def __init__(self,left,op,right,token):
        self.type = token
        self.left = left
        self.right = right
        self.op = op

class Child(Expr):
    def __init__(self,value,token):
        self.type = token
        self.value = value
