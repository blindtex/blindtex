
from io import io
from sys import argv
#The execution of the program.
if(len(argv)==2):
	io.convertToHtml1(argv[1])
	
elif(len(argv)==3):
	io.convertToHtml2(argv[1],argv[2])
	
else:
	print"Wrong number of arguments, expected one or two (file name or filename + bibliography) and received %d."%(len(argv) -1)
#End of execution.
