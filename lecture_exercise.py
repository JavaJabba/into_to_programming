
'''
def average_of_two(number_1,number_2):

    average = (number_1+number_2)/2

    return average

print("%d"% average_of_two(2,4))
print("%d"% average_of_two(2,3))'''

#default function

def func_name (param1):
    '''
    docstring
    '''
    print("hello")

    return
    
# try:
#     print(hello_there)
# except: 
#     print("Oops")

# try:
#     7/"a"
# except Exception as e:
#     print("Oops")
#     print(e)

great_show = ("ed", "ed", "ed", 2009)

# var1 = 3
# print(len(great_show))
# print(great_show.count("ed"))
# print(great_show.index("ed"))
# print(great_show[var1])

# var1 = 7
# print(len(great_show))
# print(great_show.count("plank"))
# try:
#     print(great_show.index("plank"))
#     print(great_show[var1])
# except Exception as e:
#     print("oops")
#     # print(e)
if "plank" in great_show:
    print(great_show.index("plank"))
else:
    print("no index for plank")

var1 = 7
if var1 <= len(great_show)-1:
    print(great_show[var1])
else:
    print("no index of that size")

# print(great_show[-1])
# print(great_show[len(great_show)-1])
