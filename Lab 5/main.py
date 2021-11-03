# ScriptName: main.py
# Author: <add your name here>

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
    # print(fizz_buzz(3))
    # print(fizz_buzz(5))
    # print(fizz_buzz(15))
    # print(fizz_buzz(14))
    # print(fizz_buzz("a"))
    # print(fizz_buzz(4, 4, 6))
    # print(fizz_buzz(6, 4, 6))
    # print(fizz_buzz(15, 3, 5))
    print(grades(86))
    print(grades("A"))
    print(grades(110))
    print(grades("H"))


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
