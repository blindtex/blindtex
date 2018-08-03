import pytest
from blindtex import tex2all

# TODO: Correct test

#def test_read_equation_list():
#    equation = "1+2"
#    expected_reading = ['1','más','2']
#    reading = tex2all.read_equation_list(equation)
#    assert expected_reading == reading
#
#    equation = "\\frac{1}{2}"
#    expected_reading = ['1','over','2']
#    reading = tex2all.read_equation_list(equation)
#    assert expected_reading == reading
#
#    equation = "\\int_0^2 x^4 dx"
#    expected_reading = ['integral', 'from', '0', 'to', '2', 'of', 'x', 'super', '4', 'd', 'x']
#    reading = tex2all.read_equation_list(equation)
#    assert expected_reading == reading
#
#    equation = "\\sqrt[5]{x+b}"
#    expected_reading = ['root','5','of','x','más','b','endroot']
#    reading = tex2all.read_equation_list(equation)
#    assert expected_reading == reading
#
#    equation = "\\sqrt{x+b}"
#    expected_reading = ['squarerootof','x','más','b','endroot']
#    reading = tex2all.read_equation_list(equation)
#    assert expected_reading == reading
