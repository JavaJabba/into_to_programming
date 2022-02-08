
#Solution 1:

totalNumRows = 4
totalNumCols = 5

#create an empty outer list
room = []

for rowNo in range(totalNumRows):
	#create an empty inner list, fill with zeros and append to outer list
	seats = []
	for colNo in range (totalNumCols):
		seats.append (0)
	room.append (seats)
print(room)

#Solution 2:
#create and initialise a 1d list to all zeros.
numTotalRows = 4
numTotalCols = 5
room = [0] * numTotalRows
print (room)
#print (a)
for i in range(numTotalRows):
	#change each of the zeros to a list of zeros
	room[i] = [0] * numTotalCols
print (room)

#line 22 and 27 is shorthand for the below!!
b = []
for i in range (numTotalRows):
	b.append(0)
#print (b)'''