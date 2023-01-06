def dirReduc(arr):
    ''' Make sure you only take routes that make sense and not do needless steps'''
    # Translate the array into lower case
    lowercase_list = []
    for direction in arr:
        arr = direction.lower()
        lowercase_list.append(arr)

    # How many are in the list
    amount_of_directions = len(lowercase_list)
    print(f"how many items      :", len(lowercase_list))

    while amount_of_directions > -1:
        print(lowercase_list[amount_of_directions])
        if lowercase_list[amount_of_directions] == 'north':
            print(lowercase_list[amount_of_directions])

        else:
            continue    

        print(f"run", str(amount_of_directions))
        amount_of_directions = amount_of_directions - 1    



u=["SOUTH", "NORTH", "SOUTH", "EAST", "NORTH","NORTH", "NORTH","south" ]
dirReduc(u)
