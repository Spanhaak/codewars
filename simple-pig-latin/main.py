def pig_it(text):
    '''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'''
    
    splitted_words = text.split()
    punctuation = '''.,:-?,!'''

    new_sentence = []
    for word in splitted_words:
        # check if the last letter is not a punctuation
        if word in punctuation:
            pig_word = word  
            new_sentence.append(pig_word)

        else:
            pig_word = word[1:]+word[0]+"ay"
            new_sentence.append(pig_word)   
    
    result = ' '.join(str(word) for word in new_sentence)
    
    return result
