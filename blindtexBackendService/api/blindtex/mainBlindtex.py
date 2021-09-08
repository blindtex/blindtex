#-*-:coding:utf-8-*-
import blindtex.iotools.iotools
import blindtex.iotools.stringtools
from blindtex.iotools.stringtools import troubleFormulas
from blindtex.converter import parser
import argparse
import os
import os.path
from sys import argv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def convertDocument(fileName):

    #Get the document in a string.
    documentString = iotools.iotools.openFile(fileName)
    #Get the content in a list with three elements.
    documentContent = iotools.stringtools.extractContent(documentString)
    #This generates a list(a named tuple) with the document content (all formulas replaced) named replacedDocument, inline formulas named inlineList and display formulas named displayList.
    documentAndLists = iotools.stringtools.seekAndReplaceFormulas(documentContent[1])
    newDocumentContent = documentAndLists.replacedDocument
    #Generate the labels list
    labelsList = iotools.stringtools.generateListOfLabels(documentAndLists.displayList)
    #Replace the references.
    newDocumentContent = iotools.stringtools.replaceRefs(newDocumentContent, labelsList)
    #Let's deal with path and fileNames, actually fileName is the path of the file.
    (filePath,name) = os.path.split(fileName)
    #Write another tex file without formulas.
    iotools.iotools.replaceAndWrite(documentContent,newDocumentContent,os.path.join(filePath,'noFormula_'+name))
    iotools.iotools.convertToHtml(os.path.join(filePath,'noFormula_'+name))

    #converter.parser.setOption(0)
    #Convert the formulas
    for index in range(len(documentAndLists.inlineList)):
        documentAndLists.inlineList[index] = converter.parser.convert(documentAndLists.inlineList[index])

    for index in range(len(documentAndLists.displayList)):
        documentAndLists.displayList[index] = converter.parser.convert(documentAndLists.displayList[index])

    #Get the html in a string
    htmlString = iotools.iotools.openFile(os.path.join(filePath,'noFormula_'+name.replace('.tex','.xhtml')))
    #Insert converted formulas.
    htmlString = iotools.stringtools.insertConvertedFormulas(htmlString, documentAndLists.inlineList, documentAndLists.displayList)
    #Insert References
    htmlString = iotools.stringtools.insertReferences(htmlString,labelsList)
    iotools.iotools.writeHtmlFile(htmlString, os.path.join(filePath,name.replace('.tex','.xhtml')))

    #Remove Residues
    os.remove(os.path.join(filePath,'noFormula_'+name))
    os.remove(os.path.join(filePath,'noFormula_'+name.replace('.tex','.xml')))
    os.remove(os.path.join(filePath,'noFormula_'+name.replace('.tex','.xhtml')))

    #Write the trouble formulas
    iotools.iotools.writeTroubles(fileName, troubleFormulas)

#EndOfFunction

def convertToPdf(fileName):
    #Get the document in a string.
    documentString = iotools.iotools.openFile(fileName)
    #Get the content in a list with three elements.
    documentContent = iotools.stringtools.extractContent(documentString)
    #This generates a list(a named tuple) with the document content (all formulas replaced) named replacedDocument, inline formulas named inlineList and display formulas named displayList.
    documentAndLists = iotools.stringtools.seekAndReplaceFormulas(documentContent[1])
    newDocumentContent = documentAndLists.replacedDocument
    #Generate the labels list
    labelsList = iotools.stringtools.generateListOfLabels(documentAndLists.displayList)

    #Let's deal with path and fileNames, actually fileName is the path of the file.
    (filePath,name) = os.path.split(fileName)

    converter.parser.setOption(3)#For the LaTeX Accents
    #Convert the formulas
    for index in range(len(documentAndLists.inlineList)):
        #Here we take the risk of the sign ~ being used in the formula.
        documentAndLists.inlineList[index] = "\# %s \#"%converter.parser.convert(documentAndLists.inlineList[index])

    for index in range(len(documentAndLists.displayList)):
        documentAndLists.displayList[index] = "Ecuaci\\'on\\\\%s\\\\ Fin Ecuaci\\'on\\\\"%converter.parser.convert(documentAndLists.displayList[index])
    #insert converted formulas
    newDocumentContent = iotools.stringtools.insertConvertedFormulas( newDocumentContent, documentAndLists.inlineList, documentAndLists.displayList)

    #Write the .tex file with the modified formulas
    iotools.iotools.replaceAndWrite(documentContent,newDocumentContent,os.path.join(filePath,'Accessible_'+name))

    iotools.iotools.convertToPdf(filePath ,os.path.join(filePath,'Accessible_'+name))

    #Write the trouble formulas
    iotools.iotools.writeTroubles(fileName, troubleFormulas)
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
