# ScriptName:       main.py
# Author:           Dylan Murray 121747725

# template for calling functions in another file
# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    # seperated_input("one", "two", "-", "")
    # seperated_input("one", "two", "-", "!!!\n")
    
    # print(three_numbers(1,1,1))
    # print(three_numbers(1,1,2))
    # print(three_numbers(1,1,"hi"))

    # print(seasons(1))
    # print(seasons(5))
    # print(seasons(3))

    print(grades(32))
    print(grades(20))
    print(grades(76))
    print(grades("hi"))

    # print(equal_numbers(25,25))
    # print(equal_numbers(2,3))
    # print(equal_numbers(2,"hi"))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()

