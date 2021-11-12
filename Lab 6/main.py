# ScriptName:   main.py
# Author:       Dylan Murray 121747725

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
    # print(seasons(1))
    # print(seasons(2))
    # print(seasons(3))
    # print(seasons(4))
    # print(seasons("sunny"))
    # print(seasons(8))
    # print(seasons(0))

    # print(slice_reverse(12321))
    # print(slice_reverse([1, 2, 3, 2, 1]))                          
    # print(slice_reverse("rotavator"))                              
    # print(slice_reverse(("r","o","t","a","v","a","t","o","r")))    
    # print(slice_reverse(" "))                                      
    # print(slice_reverse("abcdba"))                                 
    # print(slice_reverse(11.11))

    print(add_to_list(5, [1,3,7,9]))
    print(add_to_list("c", ["a","b","d","e"]))
    print(add_to_list(5, [1,5,7,9]))
    print(add_to_list(5))
    print(add_to_list(5, 5))
    print(add_to_list(5, ["a","d","e"]))

if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
