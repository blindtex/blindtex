import pytest
from blindtex.io import file

def test_read():
    contentFile = file.read("/path/to/dummy")
    assert "\{begin}..." == contentFile
