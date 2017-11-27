from sys import argv
from parser import convert
from literalparser import convert as literalconvert

print(literalconvert(argv[1]))
print(convert(argv[1]))



