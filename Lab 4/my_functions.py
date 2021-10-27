# ScriptName:       my_functions.py
# Author:           Dylan Murray 121747725
import math

def cast_string(param):

    return(str(param))

def seperated_input(param1, param2, sepr="", endr="\n"):
    ''' a.the function will take four parameters:
            i.param1 -string value
            ii.param2 -string value
            iii.sepr -sep string value(defaults to “”)
            iv.endr -end string value(defaults to “\n”) '''

    param1_str = cast_string(param1).capitalize()
    param2_str = cast_string(param2).capitalize()

    print(param1_str, param2_str, sep=sepr, end=endr)
    
    return


def three_numbers(number1, number2, number3):
    '''
    Ask the user for 3 numbers.  
    Pass the 3 numbers to a functioncalled three_numbers(number_1, number_2, number_3). 
    If all the numbers are the same returnTrue, otherwise returnFalse.  
    '''
    if type(number1) and type(number2) and type(number3) != int:
        return False

    if number1 == number2 == number3:
        return True
    else:
        return False

def seasons(number):
    '''
    Ask the user for a  number, and pass this number to the function.
    Depending on the number passed to the function, the function will return
    the corresponding season of the year where 1=Winter, 2=Spring, 3=Summer, and 4 = Autumn.  
    Add code to return an error message if any other number is entered:
    '''
    if number >4:
        return "Number entered, 5, is outside of input values"
    elif type(number) != int:
        return "Input value must be a number"

    if number == 1:
        return "Winter"
    elif number == 2:
        return "Spring"
    elif number == 3:
        return "Summer"
    elif number == 4:
        return "Autumn"

def grades(number):
    '''
    Ask the user for a  number, and pass this number to a function called grades(), 
    which will return the corresponding grade letter. If the user enters a value 
    outside of 0-100 the grade should return ‘X’. If a user enters a non-number, 
    return an error message 'Input value must be a number'
    '''

    if type(number) != int:
        return "Input value must be a number"
    elif number >100:
        return "X"

    if 85<= number <=100:
        return "A"
    elif 70<= number <=84:
        return "B"
    elif 55<= number <=69:
        return "C"
    elif 40<= number <=54:
        return "D"
    elif 25<= number <=39:
        return "E"
    elif 0<= number <=24:
        return "F"

def equal_numbers(number1, number2):
    '''
    Ask the user for 2 numbers, and pass these 2 numbers to a function called equal_numbers(). 
    If the two numbers are equal, then return the square root of the number as a float
    If the two numbers are not equal, then returnthe squares of both numbers as integers. 
    '''
    if type(number1) and type(number2) != int:
        return "Input value(s) must be a number"
    
    if number1 == number2:
        return math.sqrt(float(number1))
    elif number1 != number2:
        return (number1 ** 2), (number2 ** 2)
    

