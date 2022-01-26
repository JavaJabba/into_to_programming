
# #for loops
# name = "aisling"

# #type 1: get ITEM in an iterable object
# for letter in name:
#     #do something
#     print(letter + "*")

# #type 2: Get you an INDEX and using that to get an item.
# #range(start, stop, step)
# for index in range(len(name)):
#     print(name[index] + "*")

# #type 3: get both item and index
# for index, letter in enumerate(name):
#     print(index, letter)

'''
Files:
1. Open connection to file
2. read file
3. close connection

textfile.readline()     -- reads a single line, includes /n, normally always with a loop.
textfile.read()         -- reads the entire file into one big string.
textfile.readlines()    -- reads entire file into a list of strings
'''

textfile = open("debanks.txt", "r")

#read
# lyric = textfile.readline()

# while lyric != "":
#     print(lyric)
#     lyric = textfile.readline()

for lyric in textfile:
    print(lyric)


textfile.close()