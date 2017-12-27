#-*-:coding:utf-8-*-

accents = {'&aacute;':u'á', '&eacute;':u'é', '&iacute;':u'í', '&oacute;':u'ó', '&uacute;':u'ú'}

def replaceHtml(label):
	for key in accents:
		label = label.replace(key, accents[key])

	return label
#EndOfFunction
def formulate(label, option):
	'''
	Function to put in a span tag with the desired label.

	Args:
		label(str): The label that is needed in a span tag, 
						if the label has accents it is recomended put them as html asks.
		option(int): Gives the following options:
					option = 0, return the label as '<span aria-label=\"label\">&nbsp;</span>'
					option = 1, return the changes the html accents for UTF-8 accents and returns label plus a space.

	Returns:
		str: The string according to the option

	'''
	if(option == 0):
		return '<span aria-label=\"'+ label + '\">&nbsp;</span>'
	elif(option == 1):
		return replaceHtml(label)+ ' ' 
	else:
		return '<math aria-label=\"'+ label + '\">&nbsp;</math>'
		
#EndOfFunction

