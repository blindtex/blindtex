#-*-:coding:utf-8-*-
#Diccionario que contiene todoas las palabras ordinarias que se pueden utilizar
#Funciones: en esta sección, dejaremos todas las funciones que se requieran
from pkg_resources import _sget_dict


class dictionary:

    def __init__(self,dict):#Se agrega el diccionario tan pronto como se crea el objeto.
        self.dict = dict


    #TODO Agrega un comando con su respectiva lectura
    def addReading(self,key,value):#Agregar el comando y la lectura Puede variar cuando las configuraciones estén listas.
        str(value)
        str(key)
        if (self.dict.get(key) is not None):
            return('Key is alredy exist')
        else:
            self.dict[str(key)] = value
    #--------------------------------------------------------------------------

    def changeReading(self,key,value,conf):#Agregar una lectura nueva
        if (self.dict.get(key) is None):
            print('Key is alredy exist, do you want add it?')
            An=input("y/n")
            if An=='y':
                dict.addReading(key,value)
            elif An=='n':
                return
        else:
            self.dict[str(key)][conf] = value
    #--------------------------------------------------------------------------

    def showReading(self,key,conf):#Retorna la lectura configurada, falta implementar para lectura de más de una configuración
        if (self.dict.get(key) is None):
            return('Key does not alredy exist')
        else:
            return(self.dict.get(key)[conf])

    #--------------------------------------------------------------------------

    def showlatex(self,value):#Devuelve el comando al que está asociado el valor
		 theValueExists = False
		 for item in self.dict.items():
		 	if value in item[1]:
		 		key = item[0]
		 		theValueExists = True
				print 'TheValueExists'
		 if(theValueExists):
		 	return key
		 else:
		 	return 'The value does not key'
    #--------------------------------------------------------------------------

    def isThere(self,key):#--->revisar
        if (self.dict.get(key) is not None and self.dict.get(key) is not None):
            return(True)
        else:
            return(False)

            #def showCommand():#listara los comandos del diccionario
            #alpha : 'mm a' 'aaa'
