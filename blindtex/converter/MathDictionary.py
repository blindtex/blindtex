#-*-:coding:utf-8-*-
#Diccionario que contiene todoas las palabras ordinarias que se pueden utilizar
Ordinary = {'alpha': 'alfa', 'beta': 'beta', 'gamma' : 'gamma', 'delta' : 'delta' ,'epsilon' : 'epsilon', 'varepsilon':'var epsilon' , 'zeta' : 'zeta',
            'eta':'eta', 'theta' : 'teta','vartheta':'var teta', 'iota' : 'iota', 'kappa':'kappa', 'lambda':'lambda', 'mu':'mi', 'nu':'ni', 'xi':'xi',
            'pi':'pi', 'varpi': 'var pi', 'rho':'ro', 'varrho': 'var ro','sigma':'sigma', 'varsigma': 'var sigma', 'tau':'tau', 'upsilon':'ipsilon',
            'phi':'fi', 'varphi':'var fi', 'chi':'ji', 'psi':'psi', 'omega':'omega', 'Gamma': 'gama may&uacute;scula', 'Delta':'delta may&uacute;scula',
            'Theta': 'teta may&uacute;scula', 'Lambda': 'lambda may&uacute;scula', 'Xi': 'xi may&uacute;scula', 'Pi': 'pi may&uacute;scula',
            'Sigma': 'sigma may&uacute;scula', 'Upsilon': 'ipsilon may&uacute;scula', 'Phi': 'fi may&uacute;scula', 'Psi': 'psi may&uacute;scula',
            'Omega': 'omega may&uacute;scula','aleph': 'alef', 'hbar': 'hache barra', 'imath': 'i caligr&aacute;fica, sin punto',
            'jmath': 'j caligr&aacute;fica, sin punto', 'ell' : 'ele caligr&aacute;fica','vp': 'p caligr&aacute;fica', 'Re': 'parte real',
            'Im': 'parte imaginaria', 'partial': 'parcial', 'infty': 'infinito','prime': 'prima','emptyset':'conjunto vac&iacute;o','nabla':'nabla',
            'surd':'ra&iacute;z','top': 'transpuesto', 'bot': 'perpendicular','|': 'paralelo, norma', 'angle': '&aacute;ngulo',
            'triangle': 'tri&aacute;ngulo','backslash': 'barra invertida', 'forall':'para todo','exists':'existe','neg': 'negaci&oacute;n',
            'flat': 'bemol', 'natural':'becuadro','sharp':'sostenido','clubsuit':'trebol','diamondsuit': 'diamante','heartsuit': 'corazón','spadsuit': 'picas'}


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
        return(Ordinary.get(key))
#--------------------------------------------------------------------------

def showLaTex(key):
    str(key)
    if (Ordinary.get(key) is None):
        print('Key does not alredy exist')
    else:
        return(key)
#--------------------------------------------------------------------------

def isThere(key):
    if (Ordinary.get(key) is not None and Ordinary.get(key) is not None):
        return(True)
    else:
        return(False)
