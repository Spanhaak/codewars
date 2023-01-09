''' Work in progress '''
def dirReduc(arr):
    ''' Make sure you only take routes that make sense and not do needless steps'''

    number_directions =[]

    amount_of_directions = len(arr)
    print(amount_of_directions)

    for direction in arr:
        if direction == "WEST":
            number_directions.append(-2)
        if direction == "EAST":
            number_directions.append(+2)
        if direction == "NORTH":
            number_directions.append(+1)        
        if direction == "SOUTH":
            number_directions.append(-1)

    print(number_directions)

    if number_directions[0] + number_directions[1] == 0:
       number_directions.remove(number_directions[0])
       number_directions.remove(number_directions[1])
       print(number_directions)
    if number_directions[0] + number_directions[1] == 0:
       number_directions.remove(number_directions[0])
       number_directions.remove(number_directions[1])
       print(number_directions)
    if number_directions[0] + number_directions[1] == 0:
       number_directions.remove(number_directions[0])
       number_directions.remove(number_directions[1])
       print(number_directions)      


u=["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirReduc(u)

