def solution(number):
    ''' Multiples of 3 and 5'''
    
    # generate list of natural numbers
    start, end, intval = 1, number, 1
    solution_list=[item for item in range(start, end, intval)]

    # create an empy list to hold the numbers that needs counting
    counting_list = []
    
    # run through all the numbers and determine if they are already in the list
    # if not in the list, add them
    for nums in solution_list:
        if nums / 3 >= 1 and nums /3 % 1 == 0.0:
            if nums not in counting_list:
                counting_list.append(nums)
        if nums / 5 >= 1 and nums /5 % 1 == 0.0:
            if nums not in counting_list:
                counting_list.append(nums)
    
    total = sum(counting_list)
    
    return(total)
