

def readFile (filename):
    #read the file and return a list of words.
    textFile = open(filename, "r", encoding="utf-8")
    entireFile = textFile.read()
    words = entireFile.split(" ")
    return words

def depunctuate (words):
    punctuation = [",", ".", "!", "?", "-", "'"]
    words_cleaned = []
    #depunctuate the words and return a cleaned list
    i = 0
    while i < len(words):
        word = words[i]
        word = word.lower()
        for item in punctuation:
            if item in word:
                word = word.strip(item)
                words_cleaned.append(word)
        i += 1
    return words_cleaned

def countWords (words):
    #create a dictionary
    #if a word doesn't exist add it as a key with 1 as a value
    #it it does exist add 1 to the current count
        
    #process the dictionary to see which word has the highest count.
    #keep track of the highest word and associated count

    #write this to an output file
    return

#Main Program:

#read in the file to get a list of words (best use a function)
words_text = readFile("booksUTF.txt")

#depunctuate the lists of words
words_cleaned = depunctuate(words_text)
print(words_cleaned)

#count the words, calculate the max and write to a file
# countWords(words_cleaned)