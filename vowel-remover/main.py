def shortcut(s):
    '''Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.'''
    vowels = ['a', 'e', 'i', 'o' ,'u']
    for vowel in s:
        if vowel in vowels:
            s = s.replace(vowel, "")
    return s