#-*-:coding:utf-8-*-
#Diccionario que contiene todoas las palabras ordinarias que se pueden utilizar
#Funciones: en esta sección, dejaremos todas las funciones que se requieran
from pkg_resources import _sget_dict
import json

class dictionary(object):
	'''Dictionary class containing LaTeX commands and its possible readings. 
	Attributes:
		dict(dictionary): Is the principal dictionary, its items are of the form "command(str) : [conf(int), readings(list of strings)]"
						command is a LaTeX command, conf(self.dict[command][0]) is the chosen reading at the moment, acts as a index,
 						readings(self.dict[command][1]) is a list of all the possible readings of command.
		fileName(str): Is the name of the json file where the dictionary will be saved.'''
	def __init__(self, dict):#Se agrega el diccionario tan pronto como se crea el objeto.
		'''Args:
				dict(dictionary): Is the dictionary to work'''	
		self.dict = dict
	#TODO: Por el momento hay un conflicto con parser. Tal vez cuando ya se tengan todos los diccionarios en sus respectivos json se pueda quitar la cuarentena.
	#def __init__(self, jsonFileName):
	#	'''Args:
	#			jsonFileName(str): Is the name of the file from where the dictionary will be charged.'''
	#	self.open(jsonFileName)

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
				newJsonFileName(str): The name of the file in  the dictionary will be saved.'''
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
			self.dict[key][0] = len(self.dict[key][1]) - 1
		except KeyError:
			print('Command %s does not exist.'%key)
	#--------------------------------------------------------------------------
	def changeReading(self, key, index):
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
		str(value)
		str(key)
		if (self.dict.get(key) is not None):
			return('Key already exists.')
		else:
			self.dict[str(key)] = value
	#--------------------------------------------------------------------------

	def changeReading(self,key,value):#Agregar una lectura nueva
		'''Function to change the reading of a command.
		Args:
			key(str): The command that will change its reading.
			value(str): The new reading, if it exists.'''
		try:
			self.dict[key][0] = self.dict[key][1].index(value)
		except KeyError:
			print('Command %s does not exist.'%key)
		except IndexError:
			print('Reading %s does not exist.'%value)
	#--------------------------------------------------------------------------

	def showReading(self,key,conf):#Retorna la lectura configurada, falta implementar para lectura de más de una configuración
		'''Function to show the current reading a command has.
			Args:
				key(str): The command to be read.
				conf(int): The current configuration to read.
			Returns:
				str: The reading pointed by conf in the list.'''
		try:
			return str(self.dict.get(key)[1][conf])
		except KeyError:
			print('Command %s does not exist.'%key)

	#--------------------------------------------------------------------------
	
	def showReadings(self, key):
		'''Function to show all the readings that a command has.
			Args:
				key(str): The command.'''
		try:
			print(self.dict[key][1])
		except KeyError:
			print('Command %s does not exist.'%key)

	#--------------------------------------------------------------------------			
	def showlatex(self,value):#Devuelve el comando al que está asociado el valor
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

	def isThere(self,key):#--->revisar
		'''Function to know if certain command is in the dictionary.
			Args:
				key(str): The possible command.
			Returns:
				bool: True if the command is in the dict, false otherwise. '''
		if (key in self.dict):
			return(True)
		else:
			return(False)

	#def showCommand():#listara los comandos del diccionario
	#alpha : 'mm a' 'aaa'
