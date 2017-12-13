#-*-:coding:utf-8-*-

import re
import string
import collections
import copy
#import blindtex.converter.parser

#Regular expression to match anything in math mode. Altough there are better regex to do the same, this allows add new options easily.
#If you want to proove it before,  you can do it in https://regex101.com/r/dSxw4f/2/
#TODO The repetition of code is a signal it can be made in a more elegant way.

inlineMath = re.compile(r'''(?<!\\)( #Exclude escaped symbols
								((\$)(.*?)(?<!\\)(\$))| #Single $ formulas
								((\\\()(.*?)(?<!\\)(\\\))) #\(
							)''', re.DOTALL|re.UNICODE|re.X)
displayMath = re.compile(r'''(?<!\\)( #Exclude escaped symbols
										((\${2})(.*?)(?<!\\)(\${2}))| #Identify double $ formulas
										((\\\[)(.*?)(?<!\\)(\\\]))| #\[
										((\\begin\{equation\})(.*?)(?<!\\)(\\end\{equation\}))|
										((\\begin\{equation\*\})(.*?)(?<!\\)(\\end\{equation\*\}))| #begin equation with and without *
										((\\begin\{align\})(.*?)(?<!\\)(\\end\{align\}))|
										((\\begin\{align\*\})(.*?)(?<!\\)(\\end\{align\*\})) # align and align*
									)''',re.DOTALL|re.UNICODE|re.X)

#Strings to replace the found formulas.
inlineMathString = "(inlineLaTeXStringNumber%d)"
displayMathString = "(displayLaTeXStringNumber%d)"


#Function to separate the document from the preamble(LaTeX formating) and the information after the document.
#It returns an array of strings with the parts.
def extractContent(completeDocument):
    '''The method takes a string representing a LaTeX document and separates its preamble (the portion before "\\begin{document}"), its content and its epilogue (after \\end{document}) and returns them in a list.
        Args:
            completeDocument(str): The LaTeX document as a string.
        Returns:
            list[str,str,str]: A list of three strings, the first one the portion before \\begin{document}(inclusive), the second one the document, the last one the part after \\end{document}.'''
    
    preamble = ""
    document = ""
    epilogue = ""

    try:
        preamble = completeDocument[:completeDocument.index(r'\begin{document}')]
        document = completeDocument[completeDocument.index(r'\begin{document}'): completeDocument.index(r'\end{document}')+ len(r'\end{document}')]
        epilogue = completeDocument[completeDocument.index(r'\end{document}')+ len(r'\end{document}'):]
    except ValueError:
        print "\\begin{document} or \end{document} not found.\n"
    return [preamble, document, epilogue]
#EndOfFunction

#HU2 HU8 HU3
#Function to find all the math in the document, copy then in a file and replace then by  markers.
#The input is a strign with the document content, and a string with a name of the file where all the math will be writen.
def seekAndReplaceFormulas(document):
	'''Search for all the math formulas in the document, when one is found first, the function copies the formula in a list; then the function replace the formula for a marker to future uses.
		Args:
			document(str): the LaTeX content.
		Returns:
			namedTuple:A named Tuple called documentAndLists where:
						replacedDocument is the string with all the formulas replaced by markers.
						inline/displayList  is the list with all the inline/display formulas found.'''
	
	otherDocument = copy.deepcopy(document)

	inlineIterator = inlineMath.finditer(otherDocument)
	inlineIndex = 0 #Index to keep track of which equation is being replaced.
	inlineList = []
	
	while(True):
		try:
			currentMatch = inlineIterator.next()
			otherDocument = otherDocument.replace(currentMatch.group(0), inlineMathString%(inlineIndex), 1)
			currentMatch = currentMatch.group(0)
			inlineList.append(currentMatch)
			inlineIndex += 1
		except StopIteration:
			break

	displayIterator = displayMath.finditer(otherDocument)
	displayIndex = 0
	displayList =[]

	while(True):
		try:
			currentMatch = displayIterator.next()
			otherDocument = otherDocument.replace(currentMatch.group(0), displayMathString%(displayIndex),1)
			currentMatch = currentMatch.group(0)
			displayList.append(currentMatch)
			displayIndex += 1
		except StopIteration:
			break

	print "seekAndReplaceFormulas completed."
	return collections.namedtuple('documentAndLists', 'replacedDocument, inlineList, displayList')(otherDocument, inlineList, displayList)
#EndOfFunction

#HU6
#Insert all the LaTeX formulas in the file formulaFile, already converted, the replacement is done in order of appearance with the marker put before.
def insertConvertedFormulas(htmlString, inlineList, displayList):
	'''Insert all the LaTeX formulas in the lists, already converted, the replacement is done in order of appearance with the marker put before.
		Args:
			htmlString(str): the html document, product of the conversion from LaTeX to html.
			inlineList(str): the list with all the inline formulas written in LaTeX.
			diplayList(str): the list with all the  display formulas written in LaTeX.
			
		Returns:
			str: the html document but with all the formulas inserted. '''

	output = ""	
	newString = copy.deepcopy(htmlString)
	inlineIndex = 0
	for line in inlineList:
		output = newString.replace(inlineMathString%(inlineIndex),'<span>' + converter.parser.convert(line) + '</span>')
		newString = output
		inlineIndex += 1
	
	output = ""
	displayIndex = 0
	for line in displayList:
		output = newString.replace(displayMathString%(displayIndex),'<div>' + converter.parser.convert(line) + '</div>')
		newString = output
		displayIndex += 1
	
	
	print "Succes!! %d inline math inserted and %d display math inserted.\n"%(inlineIndex, displayIndex)
	return newString
#EndOfFunction







