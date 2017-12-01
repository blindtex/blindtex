from sys import argv
import argparse
import parser as parser

myArgumentParser = argparse.ArgumentParser()
myArgumentParser.add_argument('formula', type=str, help ='The formula to be converted')
myArgumentParser.add_argument('-lit', '--literal', help="Display the formula in literal form.",action="store_true")

args = myArgumentParser.parse_args()

if(args.literal):
	parser.OPTION = 1
	print(parser.convert(args.formula))
else:
	parser.OPTION = 0
	print(parser.convert(args.formula))






