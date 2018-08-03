from blindtex.latex2ast import converter
from blindtex.interpreter import reader
from blindtex.lang import translator

def read_equation(latex_equation,mode='lineal'):
    if mode == 'lineal':
        cv_s = converter.latex2list(latex_equation)
        literal_lineal_eq = reader.lineal_read_formula(cv_s)
        return(literal_lineal_eq)

def to_list(latex_equation):
    list_object_math = converter.latex2list(latex_equation)
    list_lineal_reading = reader.lineal_read_formula_list(list_object_math)
    list_lineal_reading_translated_to_spanish = translator.translate_lineal_read(list_lineal_reading, lang='es')
    return list_lineal_reading_translated_to_spanish

def read_equation_list(latex_equation,mode='lineal'):
    if mode == 'lineal':
        cv_s = converter.latex2list(latex_equation)
        literal_lineal_eq = reader.lineal_read_formula_list(cv_s)
        return(literal_lineal_eq)

def main():
    parser = argparse.ArgumentParser(description="Tool for LaTeX's equations convertion")

    parser.add_argument('-e','--equation', dest='equation',
                                            help = 'Latex format equation to convert',
                                            default="")
    args = parser.parse_args()

    if args.equation:
        print(read_equation(args.equation))
