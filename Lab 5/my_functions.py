# ScriptName:       my_functions.py
# Author:           Dylan Murray 121747725

# template for calling functions in another file


def fizz_buzz(num1, divisor_1 = 3, divisor_2 = 5):
    '''
    1.
    - Pass a number, as parameter num1, to a function called fizz_buzz().
    - For multiples of 3, return “Fizz”. 
    - For multiples of 5, return“Buzz”. 
    - For numbers which are multiples of both 3and 5, e.g., 15, 30, etc, return “FizzBuzz”.
    - If none of the conditions are true, simply return the number itself. 
    - Return the error statement 'Input value(s) must be a number’ when the inputs are not integers

    2.
    - I now want you to add two additional parameters, namely divisor_1(parameter 2) and divisor_2(parameter 3).
    - Now the function requirements are:
        - For multiples of divisor_1 the function return “Fizz”. 
        - For multiples of divisor_2, return “Buzz”. 
        - For numbers which are multiples of both divisor_1 and divisor_2 return “FizzBuzz”. 
    '''
    
    try:

        if num1 % divisor_1 == 0 and num1 % divisor_2 == 0:
            return "FizzBuzz"
        elif num1 % divisor_1 == 0:
            return "Fizz"
        elif num1 % divisor_2 == 0:
            return "Buzz"
        else:
            return num1
    except:
        return "Input value(s) must be a number"


def grades(number):
    '''
    3.
    - I want you to rewrite the grades() function from Lab 4, adding a parameter called number.
    - In the original function, you passed a number to the function, which would return the corresponding Letter Grade.
    - The function will now also take a Letter Grade and should return the Numerical Grade range.

    '''
    try:
        if number == str and number == "A":
            return "85-100"
        elif number == str and number == "B":
            return "70-84"
        elif number == str and number == "C":
            return "55-69"
        elif number == str and number == "D":
            return "40-54"
        elif number == str and number == "E":
            return "25-39"
        elif number == str and number == "F":
            return "85-100"                        
        elif number == int and 85<= number <=100:
            return "A"
        elif number == int and 70<= number <=84:
            return "B"
        elif number == int and 55<= number <=69:
            return "C"
        elif number == int and 40<= number <=54:
            return "D"
        elif number == int and 25<= number <=39:
           return "E"
        elif number == int and 0<= number <=24:
            return "F"
    except:
        if number == int and 0 > number > 100:
            return "The input numerical grade is outside the range supported"
        elif number != int or number != str:
            return "Input value must be a number or a letter"
        elif number == str and number != ("A" or "B" or "C" or "D" or "E" or "F"):
            return "The input letter grade is outside the range supported"