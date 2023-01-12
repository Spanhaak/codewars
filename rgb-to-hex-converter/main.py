def rgb(r, g, b):
    ''' this function converts RGB values to HEX color code '''
    print(f'Original value :',r,g,b)

    if r <= 0 :
        r = 00
    if r >= 255:
        r = 255
    if g <= 0 :
        g = 00
    if g >= 255:
        g = 255
    if b <= 0 :
        b = 00
    if b >= 255:
        b = 255        

    test = '%02x%02x%02x' % (r, g, b)
    test = test.upper()

    print (f'Converted value:',test.upper)

    return test

