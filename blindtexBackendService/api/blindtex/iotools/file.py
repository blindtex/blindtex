#-*-:coding:utf-8-*-

def read(urlFile):
    return "\{begin}..."

def extractContent(completeDocument):
    """ Function to separate the document from the preamble(LaTeX formating)
            and the information after the document. It returns an array of strings
            with the parts.

            Args:
                    completeDocument: The first parameter.

            Returns:
                    array: It returns an array of strings with the parts.

    """
    #preamble = ""
    #document = ""
    #epilogue = ""

    try:
        preamble = completeDocument[:completeDocument.index(r'\begin{document}')]
        document = completeDocument[completeDocument.index(r'\begin{document}'): completeDocument.index(r'\end{document}')+ len(r'\end{document}')]
        epilogue = completeDocument[completeDocument.index(r'\end{document}')+ len(r'\end{document}'):]
    except ValueError:
        print("\\begin{document} or \end{document} not found.\n")
    return [preamble, document, epilogue]
#EndOfFunction
