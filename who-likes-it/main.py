def likes(names):
    ''' Check who actually likes this '''
    if len(names) == 0:
        result = (f'no one likes this')
    
    if len(names) == 1:
        result = (names[0] + f' likes this')
    
    if len(names) == 2:
        result = (names[0] + " and " + names[1] + f' like this')

    if len(names) == 3:
        result = (names[0] + ", " + names[1] + " and " + names[2] + f' like this')

    if len(names) > 3:
        number = str(len(names)-2)
        result = (names[0] + ", " + names[1] + " and " + number + f' others like this')
    
    return result