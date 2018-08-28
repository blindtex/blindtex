import argparse
import pkg_resources
from blindtex.latex2ast import converter
from blindtex.interpreter import reader
from blindtex.lang import translator
from blindtex.iotools import iotools

DEFAULT_DICT_PATH = 'lang/dicts/spanish.json'

def read_equation(latex_equation, mode='lineal', dictionary_path = ''):

    # User enter custom dictionary path ?
    if dictionary_path == '':
        # Read of blindtex dictionary
        dictionary = iotools.read_json_file(pkg_resources.resource_filename(__package__, DEFAULT_DICT_PATH))
    else:
        # Read of custom file
        dictionary = iotools.read_json_file(dictionary_path)

    if mode == 'lineal':
        list_object_math = converter.latex2list(latex_equation)
        list_lineal_reading = reader.lineal_read_formula_list(list_object_math)
        list_lineal_reading_translated_to_spanish = translator.translate_lineal_read(list_lineal_reading, dictionary)
    return ' '.join(list_lineal_reading_translated_to_spanish)

def main():
    parser = argparse.ArgumentParser(description="Tool for LaTeX's equations convertion")

    parser.add_argument('-e','--equation', dest='equation',
                                            help = 'Latex equation to translate',
                                            default='')

    parser.add_argument('-d','--dictionary', dest='dictionary_path',
                                            help = 'Path to dictinary in json format',
                                            default='')
    args = parser.parse_args()

    if args.equation:
        print(read_equation(args.equation,'lineal',args.dictionary_path))
    else:
        parser.print_help()
