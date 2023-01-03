def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o' ,'u','A', 'E', 'I', 'O' ,'U']
    for vowel in string_:
        if vowel in vowels:
            string_ = string_.replace(vowel, "")
    return string_