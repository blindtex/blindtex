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

key = 'delta'
value = 'delta'
Ordinary = {'alpha': ['alfa', 'test @'], 'beta': ['beta'], 'gamma' : ['gamma']}



Ordinary.values()

for key in Ordinary.keys():
    Ordinary.get(key).append('teta')
    lista = Ordinary.get(key)
    print(lista)

print(Ordinary)

