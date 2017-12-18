'#--:coding:utf-8--'
import iotools.iotools
import iotools.stringtools
import converter.parser
import argparse
import os
from sys import argv

def convertDocument(fileName):

	#Get the document in a string.
	documentString = iotools.iotools.openFile(fileName)
	#Get the content in a list with three elements.
	documentContent = iotools.stringtools.extractContent(documentString)
	#This generates a list(a named tuple) with the document content (all formulas replaced) named replacedDocument, inline formulas named inlineList and display formulas named displayList.
	documentAndLists = iotools.stringtools.seekAndReplaceFormulas(documentContent[1])
	newDocumentContent = documentAndLists.replacedDocument
	#Write another tex file without formulas.
	iotools.iotools.replaceAndWrite(documentContent,newDocumentContent,'noFormula_'+fileName)
	iotools.iotools.convertToHtml('noFormula_'+fileName)

	#Convert the formulas
	for index in range(len(documentAndLists.inlineList)):
		documentAndLists.inlineList[index] = converter.parser.convert(documentAndLists.inlineList[index])

	for index in range(len(documentAndLists.displayList)):
		documentAndLists.displayList[index] = converter.parser.convert(documentAndLists.displayList[index])

	#Get the html in a string
	htmlString = iotools.iotools.openFile('noFormula_'+fileName.replace('.tex','.xhtml'))
	#Insert converted formulas.
	htmlString = iotools.stringtools.insertConvertedFormulas(htmlString, documentAndLists.inlineList, documentAndLists.displayList)
	iotools.iotools.writeHtmlFile(htmlString, fileName.replace('.tex','.xhtml'))

	#Remove Residues
	os.remove('noFormula_'+fileName)
	os.remove('noFormula_'+fileName.replace('.tex','.xml'))
	os.remove('noFormula_'+fileName.replace('.tex','.xhtml'))
#EndOfFunction



parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")

parser.add_argument('-e','--equation', dest='equation',
					help = 'Latex format equation to convert',
					default="")

parser.add_argument('-o','--output', dest='document',
					help = '',
					default="")


args = parser.parse_args()

if args.equation:
	print("Equation: ", converter.parser.convert(args.equation))
	print("Equation: ", args.equation)
else:
	print('The name is %s'% args.document)
	convertDocument(args.document)


