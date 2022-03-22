#Name:  	        Dylan Murray  
#Student ID:      121747725
#Programme:       CS1117

########################## Question 1 ############################################

def calculate_score (board):

  symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}
  colTotals = []
  rowTotals = []
  '''Calculate the score per row and append it to the rowTotals list'''
  #Your code goes here
  #iterate through each list
  for i in range(len(board)):
    #sets the rowscore to 0 before going through each row
    rowScore = 0
    #then iterates through each item in the list
    for j in range(len(board)):
      #sets the symbol taken from the list to a variable for use as dictionary key
      symbol = board[i][j]
      #makes rowscore equal to the value in the dictionary equal to the symbol key
      rowScore = symbols[symbol] + rowScore
    #check if rowscore is less than zero, if true sets to 0 instead
    if rowScore < 0:
      rowScore = 0
    #append rowscore to rowtotal list before going back through for loops and setting rowscore to zero.
    rowTotals.append(rowScore)

  '''Calculate the score per column and append it to the colTotals list'''
  #Your code goes here
  
  #iterate through each list
  for i in range(len(board)):
    #sets the colscore to 0 before going through each row
    colScore = 0 
    #then iterates through each item in the list
    for j in range(len(board)):
      #this time it sets the symbol equal to the first symbol then moving to the next list and then repeating through
      symbol = board[j][i]
      #makes colscore equal to the value in the dictionary equal to the symbol key
      colScore = symbols[symbol] + colScore
    #check if colscore is less than zero, if true sets to 0 instead
    if colScore < 0:
      colScore = 0
    #append colscore to coltotal list before going back through for loops and setting rowscore to zero.
    colTotals.append(colScore)

  return rowTotals, colTotals

rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])
print (rTotals, cTotals)

########################## Question 2 ############################################
def identifyPivot (L):
    #Your code goes here

    #Iterate through each number in list.
    for i in range(len(L)):
      # check if the sum of numbers ahead of each number is equal to the sum of the numbers before each number.
      # couldnt get it to work on the first value but works on all others which seems like a problem with my list slicing in the range function.
      if sum(range(i+1, L[-1])) == sum(range(i-1, L[0], -1)):
        #then make pivot equal to the number in which this is true then return that value.
        pivot = L[i]
        return pivot
    #if the if statement doesnt find a match it continues to this line in 
    #which pivot will become -1 as there is no value in which this is true.
    pivot = -1
    return pivot

print(identifyPivot([9,1,9])) #returns 1
print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0