def encode(message, shift):
    alphabet =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    partialStart = ''
    partialend = ''
    shiftedAlphabet= ''
    encodedMessage = ''

    if shift == 0:
        shiftedAlphabet = alphabet
    elif shift > 0 and shift < 26:
        partialStart = alphabet[:shift]
        partialend = alphabet[:shift]
        shiftedAlphabet = partialend + partialStart
    elif shift < 0 and shift > -26:
        shift = shift * (-1)
        partialStart = alphabet[:shift]
        partialend = alphabet[:shift]
        shiftedAlphabet = partialend + partialStart
    else:
     return("shift_error")
 
    for letter in alphabet:
       letter_index = alphabet.index(letter)
       encodedMessage = encodedMessage + shiftedAlphabet[letter_index]



    return encodedMessage 
    
encode("BDE", 3)