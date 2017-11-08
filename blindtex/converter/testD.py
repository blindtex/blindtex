def addWord(key,value):
    global Ordinary
    if (Ordinary.get(key) is not None):
        print('Key is alredy exist')
    else:
        Ordinary[str(key)] = value


key = 'delta'
value = 'delta'
Ordinary = {'alpha': 'alfa', 'beta': 'beta', 'gamma' : 'gamma'}
addWord(key,value)

