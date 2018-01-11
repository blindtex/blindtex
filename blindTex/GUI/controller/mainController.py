#!/usr/bin/env python
#-*-:coding:utf-8-*-
import  wx
import os
import sys
if os.name == "nt":
    import converter.parser as parser
elif os.name == "posix":
    import parser as parser

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
