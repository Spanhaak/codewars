def create_phone_number(n):
    ''' This function formats the numbers into a phone number '''
    first_set       = str(n[:3])
    first_set       = ''.join(c for c in first_set if c not in '(])[, {}<>')

    second_set      = str(n[3:6])
    second_set      = ''.join(c for c in second_set if c not in '(])[, {}<>')

    third_set       = str(n[6:10])
    third_set       = ''.join(c for c in third_set if c not in '(])[, {}<>')
    number          = "(" + first_set + ")" + " " + second_set + "-" + third_set
    return number
