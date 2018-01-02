#-*-:coding:utf-8-*-
from sys import argv
import parser as parser
import argparse

myArgumentParser = argparse.ArgumentParser()
myArgumentParser.add_argument('formula', type=str, help ='The formula to be converted')
myArgumentParser.add_argument('-lit', '--literal', help="Display the formula in literal form.",action="store_true")
myArgumentParser.add_argument('-nvda','--nvda', help='Converts with the label math.', action = "store_true")

args = myArgumentParser.parse_args()

if(args.literal):
	parser.OPTION = 1
	print(parser.convert(args.formula))
elif(args.nvda):
	parser.OPTION = 2
	result = '''<!DOCTYPE html>
				<html>
				<head>
				<meta charset="UTF-8">
				<title> Pruebas</title>
				</head>
				<body>
				<p>Fórmula generada:</p>
				<div>''' + parser.convert(args.formula) + '''</div>
				</body>
				</html>'''

	page = open('Prueba.html', 'w')
	page.write(result)
	page.close()
else:
	parser.OPTION = 0
	result = '''<!DOCTYPE html>
				<html>
				<head>
				<meta charset="UTF-8">
				<title> Pruebas</title>
				</head>
				<body>
				<p>Fórmula generada:</p>
				<div>''' + parser.convert(args.formula) + '''</div>
				</body>
				</html>'''

	page = open('Prueba.html', 'w')
	page.write(result)
	page.close()


