from blindtex.converter import parser
import pytest

def test_formulate():
    assert '<span aria-label="alpha"></span>' == parser.formulate('alpha')