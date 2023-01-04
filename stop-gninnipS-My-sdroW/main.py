def spin_words(sentence):
    splitted_words  = sentence.split()
    new_sentence    = []
    for word in splitted_words:
        if len(word) < 5:
            print (word)
            new_sentence.append(word)
        if len(word) > 4:
            word = word[::-1]
            new_sentence.append(word)
            print (word)
    sentence = ' '.join(new_sentence)            
    return sentence