
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

# great_show = ("ed", "ed", "ed", 2009)

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

# if "plank" in great_show:
#     print(great_show.index("plank"))
# else:
#     print("no index for plank")

# var1 = 7
# if var1 <= len(great_show)-1:
#     print(great_show[var1])
# else:
#     print("no index of that size")

# print(great_show[-1])
# print(great_show[len(great_show)-1])


# #list slicing
# a_list = [11,2,9,4,3]
# print(a_list)
# #list[start: end-1]
# a_list = a_list[1:4]
# print(a_list)

#populating a list using a while loop
# HP_list = []
# HP_item = input("Tell me something you liked from the Harry Potter movies: (press enter to stop)")

# while HP_item !="":
#     HP_list.append(HP_item)
#     HP_item = input("Tell me something you liked from the Harry Potter movies: (press enter to stop)")

# print(HP_list)


#increment loop
# i = 0
# while i < 10:
#     print(i, end =" ")
#     i += 2

#word slicing with while loop
# word = input("enter a word/phrase >>>> ")
# word_size = len(word)
# i = 0
# while i < word_size:
#     if i == word_size-1:
#         print(word[i])
#     elif word[i] !=" ":
#         print(word[i], end="_")    
#     i += 1
# print()



#list bug fix
# def add_to_list(value, alist:list=[]) -> list:
#     alist.append(value)
#     return alist

# def add_to_list(value, alist = None) -> list:
#     if alist == None:
#         alist = []
#     alist.append(value)
#     return alist

i=0
alist = [5,6,7,8,9]
while i < len(alist):
    print("index:", i, " - value:", alist[i])
    i += 1

# i = len(alist)-1
# while i >= 0:
#     print("index:", i, " - value:", alist[i])
#     i -= 1


