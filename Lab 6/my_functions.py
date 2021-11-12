# ScriptName:       my_functions.py
# Author:           Dylan Murray 121747725



from typing import List


def seasons(number):
    '''
    - Within this function, define a list of the seasons, and select the season based on the input value where 1=Winter, 2=Spring, 3=Summer, and 4=Autumn.  
    - Remember list indexing begins at 0.  All other error message handling, param names, etc.,in the original function, must be kept.
    '''
    seasons_list = ["Winter", "Spring", "Summer", "Autumn"]

    if type(number) != int:
        return "Input value must be a number"
    elif number >4:
        return "Number entered, 5, is outside of input values"
    elif number <= 0:
        return "Number entered needs to be between 1 and 4"
    else:
        return seasons_list[number -1]
    
def slice_reverse(input_value):
    '''
    - Write a function, slice_reverse(input_value), which determine if the input_value is a palindrome 
        i.e. reads the same backwards as forwards. 
    - The program should return True or False (booleans) depending on the input.
    '''
    
    if type(input_value) == int or type(input_value) == float:
        input_value = str(input_value) 

    if input_value == input_value[::-1]:
        return True
    else:
        return False

def add_to_list(value, list=[]):
    '''
    - I want you to create a function called add_to_list(value, list), which will return a sorted list.
    - This function will add value to the list if the list does not already contain the value.
    - For now, you can assume the list param is already sorted. 
    - You can use the python function “sort()” to sort your returning list. 
    - Sort() will NOT allow you to mix ints, floats and strings.
    '''
    try:
        if value not in list:
            list.append(value)
            list.sort()
            return list
        else:
            return list
    except:
        return "Incorrect value defined for param list"    

def add_to_list_no_sort(value, list=[]):
    '''
    - This function will add value to the list if the list does not already contain the value. 
    - For now, you can assume the list param is already sorted. 
    - In your function set an appropriate default value for the list param. 
    - In this function, you cannot use the python function “sort()” to sort your returning list. 
    - But you can now mix ints, floats and strings. If mixing ints, floats and strings, use ASCII values for strings when comparing. 
    '''

    
    
    

    


