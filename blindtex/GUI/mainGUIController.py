#!/usr/bin/env python
#-*-:coding:utf-8-*-
import sys
import blindtex.converter.parser as parser
from blindtex.mainBlindtex import convertDocument


def convert(str):
    convertedFormula = u''
    input = str
    inputSplit = input.split("\n")
    if parser.OPTION != 1:
        reload(sys)
        sys.setdefaultencoding('utf8')
        convertedFormula = '''<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title> Pruebas</title>
        </head>
        <body>
        <p>Fórmula generada:</p>'''
        for line in inputSplit:
            convertedFormula = convertedFormula + "<div>" + parser.convert(line) + "</div>" + "\n"
        convertedFormula = convertedFormula + '''</body>
        </html>'''
    if parser.OPTION == 1:
        for line in inputSplit:
            convertedFormula = convertedFormula + parser.convert(line) + "\n"
    return convertedFormula

def onSaveController(pathname, text):
    try:
        f = open(pathname, 'w')
        f.write(text)
        f.close()
        return True
    except IOError:
        return False

def onClickConvertFileController(pathName):
    try:
        convertDocument(pathName)
        return True
    except:
        return False
