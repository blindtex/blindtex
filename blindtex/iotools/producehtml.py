#-*-:coding:utf-8-*-
import parser as parser

def produceHtml(input):
	inputSplit = input.split('\n')
	convertedFormula = '''<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title> Pruebas</title>
        </head>
        <body>
        <p>Fórmula generada:</p>'''
        for line in inputSplit:
            convertedFormula = convertedFormula + "<div>" + parser.convert(line) + "</div><br>" + "\n"
        convertedFormula = convertedFormula + '''</body>
        </html>'''
		