import json
import os
import os.path
import pkg_resources

DICTSPATH = os.path.join('blindtex', 'lang', 'dicts')

def read_json_file(fileName):
    '''This function takes a file a return its content as a string.
            Args:
                    fileName(str): The name of the file to be oppened.
            Returns:
                    str: The content of the file.'''
    try:
        myFile = open(fileName,'r')
        stringDocument = json.load(myFile)
        myFile.close()
        return stringDocument
    except IOError:
        print("File %s could not be openned."%(fileName))
        return ""

def translate_lineal_read(list_of_tokens,lang='es'):
    diccionary = read_json_file(pkg_resources.resource_filename(__package__, 'dicts/spanish.json'))
    list_translated = []
    for token in list_of_tokens:
        if diccionary.get(token):
            list_translated.append(diccionary[token])
        else:
            list_translated.append(token)
    return list_translated
