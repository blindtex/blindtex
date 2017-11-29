import converter.parser
import argparse
from sys import argv


parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")

parser.add_argument('-e','--ecuation', dest='ecuation',
					help = 'Latex format ecuation to convert',
					default="")

parser.add_argument('-o','--output', dest='a.out',
					help = '',
					default="")


args = parser.parse_args()

if args.ecuation:
	print("Ecuation: ", converter.parser.convert(args.ecuation))
	print("Ecuation: ", args.ecuation)