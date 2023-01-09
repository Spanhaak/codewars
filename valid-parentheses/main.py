import re
def valid_parentheses(string):
    ''' check if the right parentheses are used '''

    # remove the letters from the string so the parentheses are left
    pattern = r'[a-zA-Z]'
    string = re.sub(pattern, '', string )

    # start counters for counting parentheses
    counter1 = 0
    counter2 = 0

    # if the string starts with a bad parentheses, return false
    if string.startswith(")") or string.startswith("())"):
        return False

    # if the string end with a bad parentheses, return false
    if string.endswith("(") or string.endswith("(("):
        return False

    # count the parentheses and compare if they are opened and close the same amount of times
    for char in string:
        if char == "(":
            counter1 = counter1 + 1
        if char == ")":
            counter2 = counter2 + 1
        else:
            pass

    if counter2 == counter1:
        return True
    else:
        return False    


valid_parentheses("n(idk)c()iya)qkkmrh(mz(jebofa))r(wczbu(idjmwz)") # ((())()())