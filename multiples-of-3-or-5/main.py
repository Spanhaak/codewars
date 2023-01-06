def solution(number):
    ''' Multiples of 3 and 5'''
    # generate list of natural numbers
    start, end, intval = 1, number, 1
    solution_list=[item for item in range(start, end, intval)]
    print (solution_list)
    # create an empy list to hold the numbers that needs counting
    counting_list = []

    print("Starting loop")
    for nums in solution_list:
        if nums / 3 >= 1 and nums /3 % 1 == 0.0:
            if nums not in counting_list:
                counting_list.append(nums)
                print (nums) 
        if nums / 5 >= 1 and nums /5 % 1 == 0.0:
            if nums not in counting_list:
                counting_list.append(nums)
                print (nums)
    
    print(counting_list)

    total = sum(counting_list)
    print(total)


solution(16)
