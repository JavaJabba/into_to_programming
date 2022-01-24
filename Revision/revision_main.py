# ScriptName:   revision_main.py
# Author:       Dylan Murray 121747725

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from revision_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print(calcWindChillIndex(27, 2))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
