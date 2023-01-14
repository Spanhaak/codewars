from datetime import datetime, timedelta
def format_duration(seconds):
    ''' This function is to display converted seconds into a human readable format '''

    if seconds == 0:
        return 'now'
    my_list = []

    # converting the seconds to time
    sec = timedelta(seconds=seconds)
    d = datetime(1,1,1) + sec

    year = ("%d" % (d.year-1))
    my_list.append(int(year))
    year = int(year)
    day = (seconds // 86400 - year * 365)
    my_list.append(int(day))
    hour = ("%d" % (d.hour))
    my_list.append(int(hour))
    minute = ("%d" % (d.minute))
    my_list.append(int(minute))
    second = ("%d" % (d.second))
    my_list.append(int(second))

    # format the result back
    return_list = []

    # format the year
    if my_list[0] == 0:
        pass
    if my_list[0] > 1:
        year = str(year)
        return_list.append(year + " years")
    if my_list[0] == 1:
        year = str(year)
        return_list.append(year + " year")

    # format the day
    if my_list[1] == 0:
        pass
    if my_list[1] > 1:
        day = str(day)
        return_list.append(day + " days")
    if my_list[1] == 1:
        day = str(day)
        return_list.append(day + " day")    
    
    # format the hour
    if my_list[2] == 0:
        pass
    if my_list[2] > 1:
        return_list.append(hour + " hours")
    if my_list[2] == 1:
        return_list.append(hour + " hour") 

    # format the minute
    if my_list[3] == 0:
        pass
    if my_list[3] > 1:
        return_list.append(minute + " minutes")
    if my_list[3] == 1:
        return_list.append(minute + " minute") 

    # format the second
    if my_list[4] == 0:
        pass
    if my_list[4] > 1:
        return_list.append(second + " seconds")
    if my_list[4] == 1:
        return_list.append(second + " second")

    # add 'and' between the last two entries
    if len(return_list) > 1:
        return_list.insert(-1, 'and') 
    else:
        pass    

   # deal with the comma situation
    if len(return_list) == 6:
        value = return_list[0]
        del return_list[0]
        value = value+','
        return_list.insert(0, value)  
        value = return_list[1]
        del return_list[1]
        value = value+','
        return_list.insert(1, value)
        value = return_list[2]
        del return_list[2]
        value = value+','
        return_list.insert(2, value)

    # deal with the comma situation
    if len(return_list) == 5:
        value = return_list[0]
        del return_list[0]
        value = value+','
        return_list.insert(0, value)  
        value = return_list[1]
        del return_list[1]
        value = value+','
        return_list.insert(1, value)

    # deal with the comma situation
    if len(return_list) == 4:
        value = return_list[0]
        del return_list[0]
        value = value+','
        return_list.insert(0, value) 

    end_result = ' '.join(return_list)
    return end_result
