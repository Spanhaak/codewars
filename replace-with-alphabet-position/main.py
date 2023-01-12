import re

def alphabet_position(text):
    ''' This function takes the input and returns a string of numbers corresponding the number of the char in the alphabet '''
    
    # first get rid of all the punctuation and numbers
    s = re.sub(r'\W+', '', text)
    s = ''.join([i for i in s if not i.isdigit()])
    
    # convert all to lowercase
    s = s.lower()
    
    # create a list that will be used to fill up in the loop
    my_list = []

    # then loop over the list and return the numbers
    # i'm using ord for this -96 to get the proper number in the alphabet
    # a would return 97 
    for char in s: 
        my_list.append(ord(char)-96)

    # transform the list into a string
    my_list = ' '.join(str(e) for e in my_list)
