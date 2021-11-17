# ScriptName: my_functions.py
# Author: Jason Quinlan

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def count(my_list, value):
    '''
    function - count how many times <value> occurs in <my_list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return:
    '''
    # set counter
    i = 0
    # accumulator to count how many times <value> occurs
    # set to zero to cover no <value> in <list>
    num_values = 0
    # loop over the length of the <list>
    while i < len(my_list):
        # if <value> and <list> index i are the same
        if my_list[i] == value:
            # increment the accumulator
            num_values += 1
        # increment the counter
        i += 1
    # return how many times <value> occurs in <list>
    return num_values

def index(my_list:str, value):
    '''
    b. index(my_list, value)-function to return the first index that value occurs in my_list.  
       Return -1 if the value does not occur in my_list
        i.index("hello", "o") -> 4
        ii.index("hello", "p") -> -1
    '''
    
    i = 0
    while i <= len(my_list) -1:
        if value == my_list[i]:
            return i
        elif value not in my_list:
            return "-1"
        else:
            i+=1

def get_value(my_list:str, index:int):
    '''
    c. get_value(my_list, index) -function to return the value that occurs in my_list at index. 
       If index does not return a valid value from my_list, it should return the error message as outlined in item3 below.
            i.get_value("hello", 1) -> "e"
    '''
    try:
        if index <= len(my_list)-1:
            return my_list[index]
        elif index > len(my_list)-1:
            return "houston, we have a problem!"
    except:
        return "houston, we have a problem!"

def insert(my_list, index, value):
    '''
    d. insert(my_list, index, value) 
    -  function to return my_list, after you have added value at index 
       (remember to check the length of my_list and if index is larger than len(my_list) add as a new index at the end my_list)
            i.insert("hello", 1, "a") -> "hallo"
            ii.insert("hello", 5, "p") -> "hellop"
    '''
    list_size = len(my_list)
    i = 0
    while i <= list_size:
        if i == index:
            [i] = value
            return my_list
        elif index > len(my_list):
            [i] = value
            return my_list
        i+=1

