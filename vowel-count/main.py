def get_count(sentence):
    ''' Return the number (count) of vowels in the given string '''
    counting = 0
    vowels = ['a', 'e', 'i', 'o' ,'u']
    for vowel in sentence:
        if vowel in vowels:
            counting=counting+1
    return counting