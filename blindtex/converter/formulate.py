# -*-:coding:utf-8-*-

accents = {'&aacute;': u'á', '&eacute;': u'é', '&iacute;': u'í', '&oacute;': u'ó', '&uacute;': u'ú'}

invertedAccents ={u'á': '&aacute;' , u'é':'&eacute;', u'í':'&iacute;', u'ó': '&oacute;', u'ú':'&uacute;'}#Sure there is a better way.

latexAccents = {'&aacute;': u"\\'a", '&eacute;': u"\\'e", '&iacute;': u"\\'i", '&oacute;': u"\\'o", '&uacute;': u"\\'u"}
def replaceHtml(label):
	for key in accents:
		label = label.replace(key, accents[key])

	return label


# EndOfFunction

def backHtml(label):
        for key in invertedAccents:
                label = label.replace(key, invertedAccents[key])

        return label
#EndOfFunction

def LatexAccents(label):
        for key in latexAccents:
                label = label.replace(key, latexAccents[key])

        return label
#EndOfFunction
#TODO: I am repeating. Fix that.
def formulate(label, option):
	'''
	Function to put in a span tag with the desired label.

	Args:
		label(str): The label that is needed in a span tag, 
						if the label has accents it is recomended put them as html asks.
		option(int): Gives the following options:
					option = 0, return the label as '<span aria-label=\"label\">&nbsp;</span>'
					option = 1, return the changes the html accents for UTF-8 accents and returns label plus a space.
					option = 2, return the label as <math aria-label=\"label\">&nbsp;</math>

	Returns:
		str: The string according to the option

	'''
	if (option == 0):
		return replaceHtml(label) + ';'
	elif (option == 1):
		return replaceHtml(label) + '\n'
	elif (option == 2):
		return '<math aria-label=\"' + label + '\">&nbsp;</math> '
	elif (option == 3):
                return LatexAccents(label) + ";"

# EndOfFunction


def formulateLabel(label, option):
        if (option == 0):
                return "label: %s "%label
        if (option == 1):
                return "label: %s\n"%label
        if (option == 2):
                return '<span id="%s"></span>'%label
        if (option == 3):
                return "$Ecuaci\\acute{o}n \\label{%s}$"%label
#EndOf Function
