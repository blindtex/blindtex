#!/usr/bin/python3
import argparse
from blindtex import tex2all

def main():
    parser = argparse.ArgumentParser(description="Tool for LaTeX's equations convertion")

    parser.add_argument('-e','--equation', dest='equation',
                                            help = 'Latex format equation to convert',
                                            default="")
    args = parser.parse_args()

    if args.equation:
        print(tex2all.read_equation(args.equation))

if __name__=='__main__':
    main()
