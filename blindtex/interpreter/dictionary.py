# -*-:coding:utf-8-*-
# Diccionario que contiene todoas las palabras ordinarias que se pueden utilizar
# Funciones: en esta sección, dejaremos todas las funciones que se requieran
from pkg_resources import _sget_dict
import json
import os

class dictionary(object):
    '''Dictionary class containing LaTeX commands and its possible readings.
    Attributes:
        dict(dictionary): Is the principal dictionary, its items are of the form "command(str) : [conf(int), readings(list of strings)]"
                        command is a LaTeX command, conf(self.dict[command][0]) is the chosen reading at the moment, acts as a index,
                         readings(self.dict[command][1]) is a list of all the possible readings of command.
        fileName(str): Is the name of the json file where the dictionary will be saved.'''    
    def __init__(self, *args, **kwargs):
        '''Args:
                *args: jsonFileName(str): Is the name of the file from where the dictionary will be charged.
                **kwargs: dict = myDictionary(dict) : a dictionary to work, it will be not saved until saveAs command is called.'''
        if ('dict' in kwargs):
            self.dict = kwargs['dict']
        else:
            self.open(args[0])

    #--------------------------------------------------------------------------

    def open(self, jsonFileName):
        '''Function to open and charge the dictionary from a json file.
            Args:
                jsonFileName(str): Is the name of the file from where the dictionary will be charged. '''
        self.fileName = jsonFileName                
        try:
            myFile = open(jsonFileName,'r')
            self.dict = json.load(myFile)
            myFile.close()
        except IOError:
            print('File %s could not be oppened.'%jsonFileName)
    #--------------------------------------------------------------------------
    def save(self):
        '''Function to save in fileName the dictionary dict.'''
        try:
            myFile = open(self.fileName, 'w')
            json.dump(self.dict, myFile)
            myFile.close()
        except IOError:
            print('File could not be oppened.')
    #--------------------------------------------------------------------------
    def saveAs(self,newJsonFileName):
        '''Function to create a new json file to save the dictionary.
            Args:
                newJsonFileName(str): The name of the file where the dictionary will be saved.'''
        self.fileName = newJsonFileName + '.json'
        try:
            myFile = open(newJsonFileName + '.json', 'w')
            json.dump(self.dict, myFile)
            myFile.close()
        except IOError:
            print('File could not be oppened.')
    #--------------------------------------------------------------------------
    def addReading(self, key, newValue):
        '''Function to add a reading to a existing key.
            Args:
                key(str): The command that will have a new reading.
                newValue(str): The new reading to the command.'''
        try:
            self.dict[key][1].append(newValue)
            #self.dict[key][0] = len(self.dict[key][1]) - 1
        except KeyError:
            print('Command %s does not exist.'%key)
    #--------------------------------------------------------------------------
    def changeReadingIndex(self, key, index):
        '''Function to change the reading of a command.
        Args:
            key(str): The command that will change its reading.
            index(int): The index of the new reading.''' 
        try:
            if(index < len(self.dict[key][1])):
                self.dict[key][0] = index                
            else:
                print('The value number %d is not in the readings list.'%index)
        except KeyError:
            print('Command %s does not exist.'%key)
    #--------------------------------------------------------------------------
    #TODO Agrega un comando con su respectiva lectura
    def addCommand(self,key,value):#Agregar el comando y la lectura Puede variar cuando las configuraciones estén listas.
        if (self.dict.get(str(key)) is not None):
            return False
        else:
            try:
                #Add the command to the dicctionary in regexes, to be recognized.
                #Open the regexes file.
                myFile = open(os.path.join('converter','dicts','regexes.json'), 'r')#THIS IS NOT THE PATH
                dictOfDicts = json.load(myFile)
                myFile.close()
                #Adds the new command in the dict of Dicts
                (path, dictName) = os.path.split(self.fileName)
                dictName  = dictName.replace('.json','')
                dictOfDicts[dictName] = dictOfDicts[dictName] + "|%s"%key
                myFile = open(os.path.join('converter','dicts','regexes.json'), 'w')
                json.dump(dictOfDicts, myFile)
                myFile.close()
            except IOError:
                print('File %s could not be oppened.'%'regexes.json')
                return False
            #Add the command with its reading to the dictionary itself.
            self.dict[(key)] = [0,[(value)]]
        return True
    #--------------------------------------------------------------------------

    def changeReading(self,key,value):#Agregar una lectura nueva
        '''Function to change the reading of a command.
        Args:
            key(str): The command that will change its reading.
            value(str): The new reading, if it exists.'''
        try:
            self.dict[(key)][0] = self.dict[(key)][1].index((value))
        except KeyError:
            print('Command %s does not exist.'%key)
        except IndexError:
            print('Reading %s does not exist.'%value)
    #--------------------------------------------------------------------------

    def showReading(self,key):#Retorna la lectura configurada, falta implementar para lectura de más de una configuración
        '''Function to show the current reading a command has.
            Args:
                key(str): The command to be read.
            Returns:
                str: The reading pointed by conf in the list.'''
        try:
            #dict(key)[0] is the index of the reading (the configuration) in the list that is dict(key)[1].
            # So, we are accessing the value in the index dict(key)[0] that is in the list dict(key)[1]. 
            return (self.dict.get(key)[1][self.dict.get(key)[0]])
        except KeyError:
            #print('Command %s does not exist.'%key)
            return key #This is because I think if the dictionary does not have the command it is better to return the same command than crash the program. David-Casas
    #---------------------------------------------------------------------------
    def showReadingIndex(self,key, index):
        try:
            return (self.dict.get(key)[1][index])
        except KeyError:
            #print('Command %s does not exist.'%key)
            return key #See ShowReading
    #--------------------------------------------------------------------------
    
    def showReadings(self, key):
        '''Function to show all the readings that a command has.
            Args:
                key(str): The command.'''
        try:
            return(self.dict[key][1])
        except KeyError:
            print('Command %s does not exist.'%key)

    #--------------------------------------------------------------------------            
    def showLatex(self,value):#Devuelve el comando al que está asociado el valor
        '''Function to sohw the command of a reading, it such exists.
            Args:
                value(str): The reading the user wants to know tha associated command.
            Returns:
                str: The command of the reading. '''
        theValueExists = False
        for item in self.dict.items():
            if value in item[1][1]:
                key = item[0]
                theValueExists = True
                break
        if(theValueExists):
            return key
        else:
            return 'The value %s has no LaTeX command associated.'%value
    #--------------------------------------------------------------------------

    def isThere(self,key):
        '''
            Function to know if certain command is in the dictionary.
            Args:
                key(str): The possible command.
            Returns:
                bool: True if the command is in the dict, false otherwise. 
        '''
        if (key in self.dict):
            return (True)
        else:
            return (False)
