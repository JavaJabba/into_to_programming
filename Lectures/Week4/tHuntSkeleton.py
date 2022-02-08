clues = [[34, 21, 32, 41, 25], [14, 42, 43, 14, 31], [54, 45, 52, 42, 23], [33, 15, 51, 31, 35], [21, 52, 33, 13]]

def checkTreasure (clue, row, col):
    #check if the coordinates is the same as the clue.  e.g. first iteration: if 34 == 11:
    #if it is return true, if not return false. 
    #print out the clue anyway

    print(clue)
    coords = int(str(col) + str(row))
    if clue == coords:
        found = True
    else:
        found = False
    return found

#start up the top left - get the clue i.e. 34
clue = clues[0][0]
#get the coordinates i.e. the row number
row = 1
#get the coordinates i.e. the column
col = 1

#check if the treasure is found by calling the checkTreasure function which returns a true or false
found = checkTreasure(clue, row, col)

#while it's not found
while found == False:
    #get the new row number
    row = int(str(clue)[0])
    #get the new column number
    col = int(str(clue)[1])
    #get the new clue
    clue = clues[row - 1][col - 1] #-1 to return visually correct row/column
    #check if this is the treasure
    found = checkTreasure(clue, row, col)

#otherwise treasure is found. Tell us what it is and where. 
print("Treasure", clue ,"Found at,", row, col)
