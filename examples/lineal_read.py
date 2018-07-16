import argparse
from blindtex import blindtex

def main():
    parser = argparse.ArgumentParser(description="Tool for LaTeX's equations convertion")

    parser.add_argument('-e','--equation', dest='equation',
                                            help = 'Latex format equation to convert',
                                            default="")
    args = parser.parse_args()

    if args.equation:
        print(blindtex.read_equation(args.equation))

if __name__=='__main__':
    main()
