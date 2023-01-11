def count_bits(n):
    ''' This function returns the bits of a number '''
    count = 0
    right_bits = format(n,'b')
    for bit in right_bits:
        if bit == '1':
            count += 1
        else:
            continue
    return count