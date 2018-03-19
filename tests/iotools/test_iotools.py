import pytest
from blindtex.iotools import iotools

text = "Hello world..."

# Funcion para crear un archivo en el espacio temporal de pruebas
def writetoafile(fname, string):
    with open(fname, 'w') as fp:
        fp.write(string)

def test_openFile(tmpdir):
	# Se crea el archivo 'output.txt' en el espacio temporal
    file = tmpdir.join('output.txt')
    # Se escribe el texto en el archivo temporal
    writetoafile(file.strpath, text)  # or use str(file)

    # Se prueba la funcion que realiza la lectura de archivos
    file_dummy = iotools.openFile(file.strpath)
    assert file_dummy == 'Hello world...'
