#Funciones: en esta sección, dejaremos todas las funciones que se requieran

#TODO Agrega un comando con su respectiva lectura
def addReading(key,value):
    str(value)
    str(key)
    global Ordinary
    if (Ordinary.get(key) is not None):
        print('Key is alredy exist')
    else:
        Ordinary[str(key)] = value
#--------------------------------------------------------------------------

def changeReading(key,value):
    str(value)
    str(key)
    global Ordinary
    if (Ordinary.get(key) is None):
        print('Key is alredy exist, do you want add it?')
        An=input("y/n")
        if An=='y':
            addReading(key,value)
        elif An=='n':
            return
    else:
        Ordinary[str(key)] = value
#--------------------------------------------------------------------------

def showReading(key):
    str(key)
    global Ordinary
    if (Ordinary.get(key) is None):
        print('Key does not alredy exist')
    else:
        print(Ordinary.get(key))
#--------------------------------------------------------------------------

def showLaTex(key):
    str(key)
    if (Ordinary.get(key) is None):
        print('Key does not alredy exist')
    else:
        print(key)
#--------------------------------------------------------------------------

def isThere(key):
    if (Ordinary.get(key) is not None and Ordinary.get(key) is not None):
        print(True)
    else:
        print(False)


key = 'delta'
value = 'delta'
Ordinary = {'alpha': 'alfa', 'beta': 'beta', 'gamma' : 'gamma'}
addReading(key,value)

print(Ordinary)

changeReading("Theta","3")

print(Ordinary)

showReading("Theta")

isThere("Theta")




