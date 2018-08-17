from blindtex.latex2ast import lexer
from blindtex.latex2ast import parser

def latex2list(latex_srt):
    par = parser.get_parser()
    lex = lexer.get_lexer()

    return par.parse(latex_srt,lex)
