def find_outlier(integers):
    ''' This function finds the outlier in the given input '''
    # determine if most is even or odd
    positive = 0
    if integers[0] % 2 == 0:
        positive = positive + 1
    if integers[1] % 2 == 0:
        positive = positive + 1   
    if integers[2] % 2 == 0:
        positive = positive + 1
    # handle the even and odd outliers
    if positive >= 2: 
        for num in integers:
            if num % 2 != 0:
                print(num)
                return num    
    else:
        for num in integers:
            if num % 2 == 0:
                print(num)
                return num    
