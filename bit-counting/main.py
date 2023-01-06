def count_bits(n):
    count = 0
    right_bits = format(n,'b')
    for bit in right_bits:
        if bit == '1':
            count += 1
        else:
            continue
    return count