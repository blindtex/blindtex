#!/usr/bin/env python
#-*-:coding:utf-8-*-
import sys
import converter.parser as parser
from mainBlindtex import convertDocument
from mainBlindtex import convertToPdf

def convert(stringInput):
    convertedFormula = u''
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
        <p>Fórmula generada:</p>
        <div>''' + parser.convert(stringInput) + '''</div>
        </body>
        </html>'''
    if parser.OPTION == 1:
        convertedFormula = parser.convert(stringInput)
    print convertedFormula
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

def onClickConvertToPdfController(pathName):
    try:
        convertToPdf(pathName)
        return True
    except:
        return False
