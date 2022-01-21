
#for loops
name = "aisling"

#type 1: get ITEM in an iterable object
for letter in name:
    #do something
    print(letter + "*")

#type 2: Get you an INDEX and using that to get an item.
#range(start, stop, step)
for index in range(len(name)):
    print(name[index] + "*")

#type 3: get both item and index
for index, letter in enumerate(name):
    print(index, letter)
