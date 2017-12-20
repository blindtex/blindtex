'#--:coding:utf-8--'
import pytest
import collections
from blindtex.iotools import stringtools

def test_extractContent():
	latex_document = "\documentclass[preview]{standalone}\\begin{document}\\begin{equation}F(V, T) = E(V) + D(T)\end{equation}\end{document}" 
	dict_document = stringtools.extractContent(latex_document) 
	assert ['preamble', r'\begin{document}content\end{document}','epilogue'] == stringtools.extractContent(r'preamble\begin{document}content\end{document}epilogue')
	assert [r'preamble\n', r'\begin{document}\ncontent\n\end{document}',r'\nepilogue'] == stringtools.extractContent(r'preamble\n\begin{document}\ncontent\n\end{document}\nepilogue')
	assert dict_document[0] == "\documentclass[preview]{standalone}"
	assert dict_document[1] == "\\begin{document}\\begin{equation}F(V, T) = E(V) + D(T)\\end{equation}\\end{document}"

def test_cleanDelimiters():
	assert 'a=b' == stringtools.cleanDelimiters('$a=b$')
	assert 'a=b' == stringtools.cleanDelimiters('$$a=b$$')
	assert 'a=b' == stringtools.cleanDelimiters(r'\(a=b\)')
	assert 'a=b' == stringtools.cleanDelimiters(r'\[a=b\]')
	assert 'a=b' == stringtools.cleanDelimiters(r'\begin{equation}a=b\end{equation}')
	assert 'a=b' == stringtools.cleanDelimiters(r'\begin{equation*}a=b\end{equation*}')
	assert 'a=b' == stringtools.cleanDelimiters(r'\begin{align}a=b\end{align}')
	assert 'a=b' == stringtools.cleanDelimiters(r'\begin{align*}a=b\end{align*}')
	assert 'a=b' == stringtools.cleanDelimiters(r'\begin{eqnarray}a=b\end{eqnarray}')
	assert 'a=b' == stringtools.cleanDelimiters(r'\begin{eqnarray*}a=b\end{eqnarray*}')

def test_seekAndReplaceFormulas():
	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], [])== stringtools.seekAndReplaceFormulas('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (inlineLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', ['a=b'], [])== stringtools.seekAndReplaceFormulas('Lorem ipsum dolor sit amet, consectetur $a=b$ adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (inlineLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', ['a=b'], [])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \(a=b\) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur $$a=b$$ adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \[a=b\] adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \begin{equation}a=b\end{equation} adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \begin{equation*}a=b\end{equation*} adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \begin{align}a=b\end{align} adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \begin{align*}a=b\end{align*} adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \begin{eqnarray}a=b\end{eqnarray} adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Duis fermentum dolor venenatis aliquet varius.', [], ['a=b'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum dolor sit amet, consectetur \begin{eqnarray*}a=b\end{eqnarray*} adipiscing elit. Duis fermentum dolor venenatis aliquet varius.')

	assert collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')('Lorem ipsum (inlineLaTeXStringNumber0) dolor (inlineLaTeXStringNumber1) sit amet, consectetur (displayLaTeXStringNumber0) adipiscing (displayLaTeXStringNumber1) elit (displayLaTeXStringNumber2). Duis (displayLaTeXStringNumber3) fermentum (displayLaTeXStringNumber4) dolor (displayLaTeXStringNumber5) venenatis (displayLaTeXStringNumber6) aliquet (displayLaTeXStringNumber7) varius.', ['i=0', 'i=1'], ['d=0', 'd=1', 'd=2', 'd=3', 'd=4', 'd=5', 'd=6', 'd=7'])== stringtools.seekAndReplaceFormulas(r'Lorem ipsum $i=0$ dolor \(i=1\) sit amet, consectetur $$d=0$$ adipiscing \[d=1\] elit \begin{equation}d=2\end{equation}. Duis \begin{equation*}d=3\end{equation*} fermentum \begin{align}d=4\end{align} dolor \begin{align*}d=5\end{align*} venenatis \begin{eqnarray}d=6\end{eqnarray} aliquet \begin{eqnarray*}d=7\end{eqnarray*} varius.')

def test_insertConvertedFormulas():
	assert 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a lectus nec turpis feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.' == stringtools.insertConvertedFormulas(r'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a lectus nec turpis feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.',[],[])

	assert 'Lorem ipsum dolor sit amet, consectetur <span>iequation0</span> adipiscing elit. Nam a lectus nec turpis feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.' == stringtools.insertConvertedFormulas('Lorem ipsum dolor sit amet, consectetur (inlineLaTeXStringNumber0) adipiscing elit. Nam a lectus nec turpis feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.', ['iequation0'], [])

	assert 'Lorem ipsum dolor sit amet, consectetur <div>dequation0</div> adipiscing elit. Nam a lectus nec turpis feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.' == stringtools.insertConvertedFormulas('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Nam a lectus nec turpis feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.', [],['dequation0'])

	assert 'Lorem ipsum dolor sit amet, consectetur <span>iequation0</span> adipiscing elit. Nam a lectus nec turpis <div>dequation0</div> feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.' == stringtools.insertConvertedFormulas('Lorem ipsum dolor sit amet, consectetur (inlineLaTeXStringNumber0) adipiscing elit. Nam a lectus nec turpis (displayLaTeXStringNumber0) feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.', ['iequation0'], ['dequation0'])

	assert 'Lorem ipsum dolor sit amet, consectetur <div>dequation0</div> adipiscing elit. Nam a lectus nec turpis <span>iequation0</span> feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.' == stringtools.insertConvertedFormulas('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Nam a lectus nec turpis (inlineLaTeXStringNumber0) feugiat eleifend. Integer convallis, nisi a porta porttitor, felis ante cursus velit, vel pulvinar risus tellus sodales ligula.', ['iequation0'], ['dequation0'])

	assert 'Lorem ipsum dolor sit amet, consectetur <div>dequation0</div> adipiscing elit. Nam a lectus nec turpis <span>iequation0</span> feugiat eleifend. Integer <span>iequation1</span> convallis, nisi a porta porttitor, felis ante cursus <div>dequation1</div> velit, vel pulvinar risus tellus sodales ligula.' == stringtools.insertConvertedFormulas('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Nam a lectus nec turpis (inlineLaTeXStringNumber0) feugiat eleifend. Integer (inlineLaTeXStringNumber1) convallis, nisi a porta porttitor, felis ante cursus (displayLaTeXStringNumber1) velit, vel pulvinar risus tellus sodales ligula.', ['iequation0', 'iequation1'], ['dequation0', 'dequation1'])

	assert 'Lorem ipsum dolor sit amet, consectetur <div>dequation0</div> adipiscing elit. Nam a lectus nec turpis <span>iequation0</span> feugiat eleifend. Integer <span>iequation1</span> convallis, nisi a porta porttitor, felis ante cursus <div>dequation1</div> velit, vel pulvinar risus tellus sodales ligula. Vestibulum et scelerisque <div>dequation2</div> augue. Cras dui dui, sodales sit amet odio <span>iequation2</span> consectetur, tristique placerat orci. Donec id lorem et eros cursus venenatis rhoncus sit amet urna. Integer magna neque, rutrum in odio non, sagittis finibus mi.' == stringtools.insertConvertedFormulas('Lorem ipsum dolor sit amet, consectetur (displayLaTeXStringNumber0) adipiscing elit. Nam a lectus nec turpis (inlineLaTeXStringNumber0) feugiat eleifend. Integer (inlineLaTeXStringNumber1) convallis, nisi a porta porttitor, felis ante cursus (displayLaTeXStringNumber1) velit, vel pulvinar risus tellus sodales ligula. Vestibulum et scelerisque (displayLaTeXStringNumber2) augue. Cras dui dui, sodales sit amet odio (inlineLaTeXStringNumber2) consectetur, tristique placerat orci. Donec id lorem et eros cursus venenatis rhoncus sit amet urna. Integer magna neque, rutrum in odio non, sagittis finibus mi.',['iequation0','iequation1','iequation2'],['dequation0','dequation1','dequation2'])
