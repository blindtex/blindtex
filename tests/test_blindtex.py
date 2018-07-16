import pytest
from blindtex import blindtex

def test_read_equation_list():
    equation = "1+2"
    expected_reading = ['1','+','2']
    reading = blindtex.read_equation_list(equation)
    assert expected_reading == reading

    equation = "\\frac{1}{2}"
    expected_reading = ['1','over','2']
    reading = blindtex.read_equation_list(equation)
    assert expected_reading == reading

    equation = "\\int_0^2 x^4 dx"
    expected_reading = ['int', 'from', '0', 'to', '2', 'of', 'x', 'super', '4', 'd', 'x']
    reading = blindtex.read_equation_list(equation)
    assert expected_reading == reading
