import argparse
from blindtex.latex2ast import converter
from blindtex.interpreter import reader

def read_equation(latex_equation,mode='lineal'):
    if mode == 'lineal':
        cv_s = converter.latex2list(latex_equation)
        lineal_lineal_eq = reader.lineal_read_formula(cv_s)
        return(lineal_lineal_eq)


def read_equation_list(latex_equation,mode='lineal'):
    if mode == 'lineal':
        cv_s = converter.latex2list(latex_equation)
        lineal_lineal_eq = reader.lineal_read_formula_list(cv_s)
        return(lineal_lineal_eq)

def main():
    parser = argparse.ArgumentParser(description="Tool for LaTeX's equations convertion")

    parser.add_argument('-e','--equation', dest='equation',
                                            help = 'Latex format equation to convert',
                                            default="")
    args = parser.parse_args()

    if args.equation:
        print(read_equation(args.equation))