''' Create Phone number '''
''' create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
'''

def create_phone_number(n):
    first_set       = str(n[:3])
    first_set       = ''.join(c for c in first_set if c not in '(])[, {}<>')

    second_set      = str(n[3:6])
    second_set      = ''.join(c for c in second_set if c not in '(])[, {}<>')

    third_set       = str(n[6:10])
    third_set       = ''.join(c for c in third_set if c not in '(])[, {}<>')
    number          = "(" + first_set + ")" + " " + second_set + "-" + third_set
    return number

create_phone_number(number)    