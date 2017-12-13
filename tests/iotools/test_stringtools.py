import pytest
from blindtex.iotools import stringtools

latex_document = "\documentclass[preview]{standalone}\\begin{document}\\begin{equation}F(V, T) = E(V) + D(T)\end{equation}\end{document}" 

def test_extractContent():
    
    dict_document = stringtools.extractContent(latex_document)   
    assert dict_document[0] == "\documentclass[preview]{standalone}"
    assert dict_document[1] == "\\begin{document}\\begin{equation}F(V, T) = E(V) + D(T)\\end{equation}\\end{document}"

#def test_seekAndReplaceFormulas():
#	equation = stringtools.seekAndReplaceFormulas(latex_document)
#	print(equation)
#	assert 0
