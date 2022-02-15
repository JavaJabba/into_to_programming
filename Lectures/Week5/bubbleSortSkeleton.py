L1 = [5, 8, 2, 9, 7, 3]

def BubbleSort (list):

	#loop for every round or iteration over the list that we need to take n=20, n-1 iterations i.e 19
	for noPasses in range(len(list)-1):
		change = False
		#loop for every pair we need to examine - in a single given iteration
		for pairNo in range(len(list)-1):
			#if the second number is less than the first number
			if list[pairNo] > list[pairNo+1]:
				# be ware of x,y = y,x (works) and the inbuilt swap function. While they work we will do a "traditional" swap 
				#swap by creating a temporary third variable. 
				temp = list[pairNo]
				list[pairNo] = list[pairNo+1]
				list[pairNo+1] = temp
				change = True
		if change == False:
			return list
		#print the list at the end of the round. 
		print("Round", noPasses + 1, ":", list)

	#return the list
	return list

myList = BubbleSort (L1)
