import pytest
from blindtex.lang import translator

def test_translate_lineal_read():
    lineal_read_list = ['iiint', 'from', '0', 'to', '2', 'of', 'x', 'super', '4', 'd', 'x']
    expected_lineal_read = ['tripleIntegral', 'desde', '0', 'hacia', '2', 'de', 'x', 'super', '4', 'd', 'x']
    lineal_read_translated = translator.translate_lineal_read(lineal_read_list)
    assert expected_lineal_read == lineal_read_translated
