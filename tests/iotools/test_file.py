import pytest
from blindtex.iotools import file

def test_extractContent():
	contentFile = str(r'\begin{document} \title{Introduction to \LaTeX{}} \begin{abstract}\ The abstract text goes here. \end{abstract} \end{document}')

	array = file.extractContent(contentFile)
	assert array[1] == contentFile

def test_read():
    contentFile = file.read("/path/to/dummy")
    assert "\{begin}..." == contentFile
