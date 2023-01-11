def digital_root(n):
    ''' This function builds the digital root of the input '''
    # build a list of numbers
    number  = str(n)
    num_list =[]

    for num in number:
        num_list.append(num)
    print(f"The list of numbers                     :",num_list)

    int_num_list = ([int(x) for x in num_list])   
         
    # Sum all items in the list
    sum = 0
    for item in int_num_list:
        sum = sum + item
    print(f"Sum of all items in the list            :",sum)        

    # Determine how many digits the number has
    n = int(sum)
    count = 0
    while(n > 0):
        count = count + 1
        n = n // 10
    print(f"The # of digits in sum are              :",count)

    # deal with the longer numbers
    counter = count 
    while counter != 0 :
        n = int(sum)
        count = 0
        while(n > 0):
            count = count + 1
            n = n // 10
        print(f"The # of digits in sumloop are          :",count)
        
        temp_list = []
        for i in str(sum):
            temp_list.append(i)
        int_temp_list = ([int(x) for x in temp_list])     
        print(int_temp_list)    
        # Sum all items in the list
        sum = 0
        for item in int_temp_list:
            sum = sum + item
        print(f"Sum of all items in the list            :",sum) 

        if sum < 2 :
            print(f"End number is: ", sum)
            return sum
        counter = counter -1
    return sum    