#--:coding:utf-8--
import iotools.iotools
import iotools.stringtools
import converter.parser
import argparse
import os
import os.path
from sys import argv

def convertDocument(fileName):

	#Get the document in a string.
	documentString = iotools.iotools.openFile(fileName)
	#Get the content in a list with three elements.
	documentContent = iotools.stringtools.extractContent(documentString)
	#This generates a list(a named tuple) with the document content (all formulas replaced) named replacedDocument, inline formulas named inlineList and display formulas named displayList.
	documentAndLists = iotools.stringtools.seekAndReplaceFormulas(documentContent[1])
	newDocumentContent = documentAndLists.replacedDocument
	#Let's deal with path and fileNames, actually fileName is the path of the file.
	(filePath,name) = os.path.split(fileName)
	#Write another tex file without formulas.
	iotools.iotools.replaceAndWrite(documentContent,newDocumentContent,os.path.join(filePath,'noFormula_'+name))
	iotools.iotools.convertToHtml(os.path.join(filePath,'noFormula_'+name))

	#Convert the formulas
	for index in range(len(documentAndLists.inlineList)):
		documentAndLists.inlineList[index] = converter.parser.convert(documentAndLists.inlineList[index])

	for index in range(len(documentAndLists.displayList)):
		documentAndLists.displayList[index] = converter.parser.convert(documentAndLists.displayList[index])

	#Get the html in a string
	htmlString = iotools.iotools.openFile(os.path.join(filePath,'noFormula_'+name.replace('.tex','.xhtml')))
	#Insert converted formulas.
	htmlString = iotools.stringtools.insertConvertedFormulas(htmlString, documentAndLists.inlineList, documentAndLists.displayList)
	iotools.iotools.writeHtmlFile(htmlString, os.path.join(filePath,name.replace('.tex','.xhtml')))

	#Remove Residues
	os.remove(os.path.join(filePath,'noFormula_'+name))
	os.remove(os.path.join(filePath,'noFormula_'+name.replace('.tex','.xml')))
	os.remove(os.path.join(filePath,'noFormula_'+name.replace('.tex','.xhtml')))
#EndOfFunction


def convertFormula(strFormula,intOption = 1):

        converter.parser.setOption(intOption)
        return converter.parser.convert(strFormula)
#EndOfFunction


if __name__=='__main__':
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
#EndOfMain

