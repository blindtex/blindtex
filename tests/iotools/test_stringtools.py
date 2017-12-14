'#--:coding:utf-8--'
import pytest
import collections
from blindtex.iotools import stringtools

def test_extractContent():
	assert ['preamble', r'\begin{document}content\end{document}','epilogue'] == stringtools.extractContent(r'preamble\begin{document}content\end{document}epilogue')
	assert [r'preamble\n', r'\begin{document}\ncontent\n\end{document}',r'\nepilogue'] == stringtools.extractContent(r'preamble\n\begin{document}\ncontent\n\end{document}\nepilogue')

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


