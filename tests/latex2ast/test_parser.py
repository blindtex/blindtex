#-*-:coding:utf-8-*-
import pytest
from blindtex.latex2ast import lexer
from blindtex.latex2ast import parser

def test_symbol():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string1 = 'a'
    cv1 = custom_parser.parse(latex_string1,custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'a'
    latex_string2 = '1'
    cv2 = custom_parser.parse(latex_string2,custom_lexer)
    assert type(cv2) is list
    assert cv2[0].content == '1'
    latex_string3 = r'\alpha'
    cv3 = custom_parser.parse(latex_string3,custom_lexer)
    assert type(cv2) is list
    assert cv3[0].content == 'alpha'
#EOF
def test_block():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = '{a}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'block'
    assert cv[0].get_children()[0].content == 'a'
#EOF

#EOF

def test_accent():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'\hat{a}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'block'
    assert cv[0].get_children()[0].content == 'a'
    assert cv[0].accent == 'hat'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'\acute a'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].accent == 'acute'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'\hat{ab}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'block'
    assert cv[0].accent == 'hat'
    assert cv[0].get_children()[0].content == 'a'
    assert cv[0].get_children()[1].content == 'b'

def test_style():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'\mathit{a}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'block'
    assert cv[0].style == 'mathit'
    assert cv[0].get_children()[0].content == 'a'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'\mathbf a'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].style == 'mathbf'
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'\mathrm{ab}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'block'
    assert cv[0].style == 'mathrm'
    assert cv[0].get_children()[0].content == 'a'
    assert cv[0].get_children()[1].content == 'b'

def test_simple_indexes():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = 'a^b'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].superscript[0].content == 'b'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'a^{b}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].superscript[0].content == 'block'
    assert cv[0].superscript[0].get_children()[0].content == 'b'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = 'a_b'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].subscript[0].content == 'b'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'a_{b}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].subscript[0].content == 'block'
    assert cv[0].subscript[0].get_children()[0].content == 'b'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'a_{b^c}'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].subscript[0].content == 'block'
    assert cv[0].subscript[0].get_children()[0].content == 'b'
    assert cv[0].subscript[0].get_children()[0].superscript[0].content == 'c'

def test_compound_indexes():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = 'a^b_c'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].superscript[0].content == 'b'
    assert cv[0].subscript[0].content == 'c'

    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()
    latex_string = r'a_c^b'
    cv = custom_parser.parse(latex_string,custom_lexer)
    assert type(cv) is list
    assert cv[0].content == 'a'
    assert cv[0].superscript[0].content == 'b'
    assert cv[0].subscript[0].content == 'c'

def test_frac():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'\frac 1 a'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'fraction'
    assert cv1[0].get_children()[0].content == '1'
    assert cv1[0].get_children()[1].content == 'a'

    latex_string2 = r'\frac \alpha {\bigcap}'
    cv2 = custom_parser.parse(latex_string2, custom_lexer)
    assert type(cv2) is list
    assert cv2[0].content == 'fraction'
    assert cv2[0].get_children()[0].content == 'alpha'
    assert cv2[0].get_children()[1].content == 'block'
    assert cv2[0].get_children()[1].get_children()[0].content == 'bigcap'

    latex_string3 = r'\frac {\sqcap} \ni '
    cv3 = custom_parser.parse(latex_string3, custom_lexer)
    assert type(cv3) is list
    assert cv3[0].content == 'fraction'
    assert cv3[0].get_children()[0].content == 'block'
    assert cv3[0].get_children()[0].get_children()[0].content == 'sqcap'
    assert cv3[0].get_children()[1].content == 'ni'

    latex_string4 = r'\frac {\leftarrow}{\rangle}'
    cv4 = custom_parser.parse(latex_string4, custom_lexer)
    assert type(cv4) is list
    assert cv4[0].content == 'fraction'
    assert cv4[0].get_children()[0].content == 'block'
    assert cv4[0].get_children()[0].get_children()[0].content == 'leftarrow'
    assert cv4[0].get_children()[1].content == 'block'
    assert cv4[0].get_children()[1].get_children()[0].content == 'rangle'


def test_root():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'\sqrt \wp'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'root'
    assert len(cv1[0].children) == 1
    assert cv1[0].get_children()[0].content == 'wp'

    latex_string2 = r'\sqrt{\clubsuit}'
    cv2 = custom_parser.parse(latex_string2, custom_lexer)
    assert type(cv2) is list
    assert cv2[0].content == 'root'
    assert len(cv2[0].get_children()) == 1
    assert cv2[0].get_children()[0].content == 'block'
    assert cv2[0].get_children()[0].get_children()[0].content == 'clubsuit'

    latex_string3  = r'\sqrt [\sum] \uplus'
    cv3 = custom_parser.parse(latex_string3, custom_lexer)
    assert type(cv3) is list
    assert cv3[0].content == 'root'
    assert len(cv3[0].get_children()) == 2
    assert cv3[0].get_children()[0].content == 'sum'
    assert cv3[0].get_children()[1].content == 'uplus'

    latex_string4  = r'\sqrt [\sum] {\uplus}'
    cv4 = custom_parser.parse(latex_string4, custom_lexer)
    assert type(cv4) is list
    assert cv4[0].content == 'root'
    assert len(cv4[0].get_children()) == 2
    assert cv4[0].get_children()[0].content == 'sum'
    assert cv4[0].get_children()[1].content == 'block'
    assert cv4[0].get_children()[1].get_children()[0].content == 'uplus'

    latex_string5 = r'\sqrt [[] ]'
    cv5 = custom_parser.parse(latex_string5, custom_lexer)
    assert type(cv5) is list
    assert cv5[0].content == 'root'
    assert len(cv5[0].get_children()) == 2
    assert cv5[0].get_children()[0].content == '['
    assert cv5[0].get_children()[1].content == ']'

def test_choose():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'a \choose b'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'choose'
    assert len(cv1[0].get_children()) == 2
    assert cv1[0].get_children()[0].content == 'a'
    assert cv1[0].get_children()[1].content == 'b'

    latex_string2 = r'{\oint \choose \leftrightarrow}'
    cv2 = custom_parser.parse(latex_string2, custom_lexer)
    assert type(cv2) is list
    assert cv2[0].content == 'block'
    assert cv2[0].get_children()[0].content == 'choose'
    assert len(cv2[0].get_children()) == 1
    assert len(cv2[0].get_children()[0].get_children()) == 2
    assert cv2[0].get_children()[0].get_children()[0].content == 'oint'
    assert cv2[0].get_children()[0].get_children()[1].content == 'leftrightarrow'

#TODO: It is not recognizing blocks (?)
def test_binom():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'\binom \Leftrightarrow \Gamma'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'binom'
    assert len(cv1[0].get_children()) == 2
    assert cv1[0].get_children()[0].content == 'Leftrightarrow'
    assert cv1[0].get_children()[1].content == 'Gamma'

    latex_string2 = r'\binom \Leftrightarrow {\Gamma}'
    cv2 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv2) is list
    assert cv2[0].content == 'binom'
    assert len(cv2[0].get_children()) == 2
    assert cv2[0].get_children()[0].content == 'Leftrightarrow'
    assert cv2[0].get_children()[1].content == 'Gamma'

    latex_string3 = r'\binom {\Leftrightarrow} \Gamma'
    cv3 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv3) is list
    assert cv3[0].content == 'binom'
    assert len(cv3[0].get_children()) == 2
    assert cv3[0].get_children()[0].content == 'Leftrightarrow'
    assert cv3[0].get_children()[1].content == 'Gamma'

    latex_string4 = r'\binom {\Leftrightarrow} {\Gamma}'
    cv4 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv4) is list
    assert cv4[0].content == 'binom'
    assert len(cv4[0].get_children()) == 2
    assert cv4[0].get_children()[0].content == 'Leftrightarrow'
    assert cv4[0].get_children()[1].content == 'Gamma'

def test_pmod():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'\pmod \epsilon'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'pmod'
    assert cv1[0].get_children()[0].content == 'epsilon'
    assert len(cv1[0].get_children()) == 1

    latex_string2 = r'\pmod {\oplus}'
    cv2 = custom_parser.parse(latex_string2, custom_lexer)
    assert type(cv2) is list
    assert cv2[0].content == 'pmod'
    assert cv2[0].get_children()[0].content == 'block'
    assert cv2[0].get_children()[0].get_children()[0].content == 'oplus'
    assert len(cv2[0].get_children()) == 1

def test_text():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'\text a'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'text'
    assert cv1[0].get_children() == 'a' #A text character it is not a math object.
    #assert len(cv1[0].get_children()) == 1

    latex_string2 = r'\textrm {zb c 1 2 34 (d5)}'
    cv2 = custom_parser.parse(latex_string2, custom_lexer)
    assert type(cv2) is list
    assert cv2[0].content == 'text'
    #assert len(cv2[0].get_children()) == 1
    assert cv2[0].get_children() == 'zb c 1 2 34 (d5)' #A text character it is not a math object.


def test_label():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'\label{my label}'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'label'
    assert cv1[0].get_children() == 'label{my label}' #A label it is not a math object.


def test_concatenation():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'ab'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert type(cv1) is list
    assert cv1[0].content == 'a'
    assert cv1[1].content == 'b'

    latex_string2 = r'a^2b_i^3'
    cv2 = custom_parser.parse(latex_string2, custom_lexer)
    assert cv2[0].content == 'a'
    assert cv2[0].superscript[0].content == '2'
    assert cv2[1].content == 'b'
    assert cv2[1].subscript[0].content == 'i'
    assert cv2[1].superscript[0].content == '3'

def test_array():
    custom_parser = parser.get_parser()
    custom_lexer = lexer.get_lexer()

    latex_string1 = r'\begin{array}a&b\\c&d\end{array}'
    cv1 = custom_parser.parse(latex_string1, custom_lexer)
    assert cv1[0].content == 'array'
    children = cv1[0].get_children()
    assert len(children) == 7 #Two Rows
    assert children[0].content == 'a'
    assert children[1].content == '&'
    assert children[2].content == 'b'
    assert children[3].content == r'\\'
    assert children[4].content == 'c'
    assert children[5].content == '&'
    assert children[6].content == 'd'

