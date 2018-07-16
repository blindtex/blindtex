from blindtex.latex2ast import converter
from blindtex.interpreter import reader

def read_equation(latex_equation,mode='lineal'):
    if mode == 'lineal':
        cv_s = converter.latex2list(latex_equation)
        literal_lineal_eq = reader.literal_read_formula(cv_s)
        return(literal_lineal_eq)


def read_equation_list(latex_equation,mode='lineal'):
    if mode == 'lineal':
        cv_s = converter.latex2list(latex_equation)
        literal_lineal_eq = reader.literal_read_formula_list(cv_s)
        return(literal_lineal_eq)
