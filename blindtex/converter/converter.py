import os
from sys import argv

def run(arg):
    try:
        print(convert(arg))
    except:
        print("Error, please check the requirements and configurations")

if os.name == "nt":
    print os.name
    from blindtex.converter.parser import convert
    run(argv[1])
if os.name == "posix":
    print os.name
    from parser import convert
    run(argv[1])




