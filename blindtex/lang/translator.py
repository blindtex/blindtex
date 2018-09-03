def translate_lineal_read(list_of_tokens, dictionary):
    """
    Args:
        list_of_tokens(list): List of token to translate
        dictionary(dict): Python dictionary with tokens and their traduction

    Returns
        dict: List of token translated using dictinary
    """
    list_translated = []
    for token in list_of_tokens:
        if dictionary.get(token):
            list_translated.append(dictionary[token])
        else:
            list_translated.append(token)
    return list_translated
