'#--:coding:utf-8--'
import pytest
from blindtex.converter import blindtex_parser


def test_convert():
    assert ' ' == blindtex_parser.convert("\sqrt{a^{x-1}+3}")
