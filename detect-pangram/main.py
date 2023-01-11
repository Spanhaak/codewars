import string
def is_pangram(s):
    ''' This function detects if the given input is a pangram '''
    
    # it is a bit lame, but I don't know how to do it without hardcoding the alphabet
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    # remove punctuation and empty spaces
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.replace(" ", "")

    # loop over the string and compare with the letters
    for each_letter in letters:
        if each_letter not in s.lower():
            return False

    return True
    