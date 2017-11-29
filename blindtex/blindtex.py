import converter.parser
import argparse
from sys import argv


parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")

parser.add_argument('-e','--equation', dest='equation',
					help = 'Latex format equation to convert',
					default="")

parser.add_argument('-o','--output', dest='a.out',
					help = '',
					default="")


args = parser.parse_args()

if args.equation:
	print("Equation: ", converter.parser.convert(args.equation))
	print("Equation: ", args.equation)
