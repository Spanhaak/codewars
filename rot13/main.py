def rot13(message):
    ''' This function applies the ceasar cipher called rot13 to the message '''

    # start an empty list
    my_list = []

    # since this is rot13, the shift is 13 chars
    # if you want a different shift, just adjust the number
    shift = 13

    # loop the message
    for each in message:
        # check if input is alphabetical
        if each.isalpha():   
            each = ord(each)
            # handle uppercase input
            if each >= 65 and each <= 90:
                # do the shift and convert it to the new value while taking into account that numbers rotate from the start if the value is higher than the end value of the alphabet
                converted_number = each + shift
                if converted_number > 90:
                    new_number = converted_number - 90 + 64
                    converted_number = chr(new_number)
                    my_list.append(converted_number)
                else:
                    converted_number = chr(converted_number) 
                    my_list.append(converted_number) 

            # handle lowercase input
            if each > 96 and each <= 122:
                # do the shift and convert it to the new value while taking into account that numbers rotate from the start if the value is higher than the end value of the alphabet
                converted_number = each + shift
                if converted_number > 122:
                    new_number = converted_number - 122 + 96
                    converted_number = chr(new_number)
                    my_list.append(converted_number)
                else:
                    converted_number = chr(converted_number)
                    my_list.append(converted_number)

        else:
            my_list.append(each)   
    
    end_result = ''.join(my_list)
    return end_result