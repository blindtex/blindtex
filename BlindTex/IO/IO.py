#-*-:coding:utf-8-*-

#TODO Document the methods.

import os
import re
import copy
import string
import subprocess
from sys import argv

#Regular expression to match anything in math mode. Altough there are better regex to do the same, this allows add new options easily.
#If you want to proove it before,  you can do it in https://regex101.com/r/dSxw4f/2/
#TODO The repetition of code is a signal it can be made in a more elegant way.
mathMode = re.compile(r'''(?<!\\)( #Exclude escaped symbols
											((\${2})(.*?)(?<!\\)(\${2}))| #Identify double $ formulas
											((\$)(.*?)(?<!\\)(\$))| #Single $ formulas
											((\\\()(.*?)(?<!\\)(\\\)))| #\(
											((\\\[)(.*?)(?<!\\)(\\\]))| #\[
											((\\begin\{equation\})(.*?)(?<!\\)(\\end\{equation\}))|
											((\\begin\{equation\*\})(.*?)(?<!\\)(\\end\{equation\*\}))| #begin equation with and without *
											((\\begin\{align\})(.*?)(?<!\\)(\\end\{align\}))|
											((\\begin\{align\*\})(.*?)(?<!\\)(\\end\{align\*\})) # align and align*
											)''',re.DOTALL|re.UNICODE|re.X)
replaceString = "(LaTexStringNumber%d)"
#HU1
#Method to open a file and return its content as a string.
def openFile(fileName):
	try:
		myFile = open(fileName)
		stringDocument = myFile.read()
		myFile.close()
		return stringDocument
	except IOError:
		print "File %s could not be openned."%(fileName)
		return ""
#EndOfFunction

#Function to separate the document from the preamble(LaTeX formating) and the information after the document.
#It returns an array of strings with the parts.
def extractContent(completeDocument):
	try:
		preamble = completeDocument[:completeDocument.index(r'\begin{document}')]
		document = completeDocument[completeDocument.index(r'\begin{document}'): completeDocument.index(r'\end{document}')+ len(r'\end{document}')]
		epilogue = completeDocument[completeDocument.index(r'\end{document}')+ len(r'\end{document}'):]
	except ValueError:
		print "\\begin{document} or \end{document} not found.\n"
	return [preamble, document, epilogue]
#EndOfFunction

#HU2 HU8 HU3
#Function to find all the math in the document, copy it in a file and replace it by a marker.
#The input is a strign with the document content, and a string with a name of the file where all the math will be writen.
def seekAndReplace(document, formulaFileName):
	otherDocument = copy.deepcopy(document)
	myIterator = mathMode.finditer(otherDocument)
	index = 0 #Index to keep track of which equation is being replaced.
	
	try:
		myFile = open(formulaFileName, "w")#TODO Check if the file already exits, warn about that and decide if the user wants to replace it.
		while(True):
			try:
				currentMatch = myIterator.next()
				otherDocument = otherDocument.replace(currentMatch.group(0), replaceString%(index), 1)
				currentMatch = currentMatch.group(0)
				myFile.write(currentMatch +"\n")
				index += 1
			except StopIteration:
				myFile.close()
				break
	except IOError:
		print "File could not be oppened."
	
	print "seekAndReplace completed."
	return otherDocument
#EndOfFunction

#Replace the document with the LaTeX math with the output of the function seekAndReplace. Write the content in a new file.
def replaceAndWrite(contentList, replacedDocument, fileName):
	newContentList = copy.deepcopy(contentList)
	newContentList[1] = replacedDocument
	try:
		myFile = open(fileName, 'w')#TODO Check if the file already exits, warn about that and decide if the user wants to replace it.
		myFile.write(string.join(newContentList))
		myFile.close()
	except IOError:
		print "File could not be oppened."
	print "replaceAndWrite completed."
#EndOfFunction


#Insert all the LaTeX formulas in the file formulaFile, already converted, the replacement is done in order of appearance with the marker put before.
def insertConvertedFormulas(htmlString, formulaFile):
	try:
		myFile = open(formulaFile)
	except IOError:
		print "File could not be openned."
		return
	output = ""	
	newString = copy.deepcopy(htmlString)
	index = 0
	
	for line in myFile:
		output = newString.replace(replaceString%(index),line)
		newString = output
		index += 1

	myFile.close()
	print "%d math inserted.\n"%(index)
	return newString
#EndOfFunction

def main1(fileName):
	noExtensionName = fileName.replace(".tex","")

	myContent = extractContent(openFile(fileName))
	newDocument = seekAndReplace(myContent[1], noExtensionName + "_Formulae.txt")#Generates  txt file.
	replaceAndWrite(myContent, newDocument, "NoTex"+fileName)#Generates  tex File

	#HU7
	subprocess.call(["latexml","--dest=%s.xml"%(noExtensionName),"--quiet","NoTex"+fileName], shell= True)#Generates xml file.
	subprocess.call(["latexmlpost","-dest=%s.xhtml"%(noExtensionName),noExtensionName+".xml"], shell= True)#Generates xhtml file.

	htmlString = openFile(noExtensionName+".xhtml")
	#TODO Call the method to convert the formulas and generate a file with them.
	#HU6
	htmlString = insertConvertedFormulas(htmlString, noExtensionName+ "_ConvertedFormulae.txt") #TODO Insert the converted Formulas.

	try:
		newFile = open(noExtensionName+".xhtml", 'w')
		newFile.write(htmlString)
		newFile.close()
		os.remove(noExtensionName+"_Formulae.txt")#It could not generate this file.
		os.remove("NoTex"+fileName)
		os.remove(noExtensionName+".xml")
	except IOError:
		print "file could not be oppened."
		return
	print "Process Ended."
#EndOfFunction

#The same main but considering a bibliography.
def main2(fileName, biblioName):
	noExtensionName = fileName.replace(".tex","")
	noExtensionBiblio = biblioName.replace(".bib","")

	myContent = extractContent(openFile(fileName))
	newDocument = seekAndReplace(myContent[1], noExtensionName + "_Formulae.txt")
	replaceAndWrite(myContent, newDocument, "NoTex"+fileName)

	#HU7
	subprocess.call(["latexml","--dest=%s.xml"%(noExtensionName),"--quiet","NoTex"+fileName], shell=True)
	subprocess.call(["latexml", "--dest=%s.xml"%(noExtensionBiblio),"--bibtex", biblioName], shell= True)
	subprocess.call(["latexmlpost","-dest=%s.xhtml"%(noExtensionName),"--bibliography=%s.xml"%(noExtensionBiblio),noExtensionName+".xml"], shell=True)

	htmlString = openFile(noExtensionName+".xhtml")
	#TODO Call the method to convert the formulas and generate a file with them.
	#HU6
	htmlString = insertConvertedFormulas(htmlString, noExtensionName+ "_ConvertedFormulae.txt") #TODO Insert the converted Formulas.

	try:
		newFile = open(noExtensionName+".xhtml", 'w')
		newFile.write(htmlString)
		newFile.close()
		os.remove(noExtensionName+"_Formulae.txt")#It could not generate this file.
		os.remove("NoTex"+fileName)
		os.remove(noExtensionName + ".xml")
		os.remove(noExtensionBiblio + ".xml")
	except IOError:
		print "file could not be oppened."
		return
	print "Process Ended"
#EndOfFunction

#The execution of the program.
if(len(argv)==2):
	main1(argv[1])
	
elif(len(argv)==3):
	main2(argv[1],argv[2])
	
else:
	print"Wrong number of arguments, expected one or two (file name or filename + bibliography) and received %d."%(len(argv) -1)
#End of execution.

