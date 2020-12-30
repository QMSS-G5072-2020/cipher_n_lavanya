def cipher(text, shift, encrypt=True):
    
    """
    About the Function
    ------------------
    This function applies the Caesar cipher, which is a simple and well-known encryption technique, on text input. 
    Each letter in the text is replaced by a letter some fixed number of positions down the alphabet.
    
    Inputs
    ------
    text:
        This is any Python string input. This is the text that is to be enciphered.
    shift:
        This is any Python integer input. This specifies the number of positions down the alphabet for the letters in the text to be replaced by.
    encrypt:
        This is set to a default value of True, which indicates that the shift is to be added to the position of each letter in the input text to obtain the new position of each letter in the enciphered text. If this parameter is set to False, the shift will be subtracted from the position of each letter in the input text instead.
        
    Output
    ------
    This is the enciphered text after the Caesar cipher has been applied to the input text.
    
    Examples
    --------
    >>> from cipher_ln2444 import cipher
    >>> cipher('apple', 1)
    'bqqmf'
    >>> cipher('bqqmf', 1, False)
    'apple'
    """
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text