'''
Rewrite the body of the below function to solve the same task using:
(i)	A list comprehension only.
(ii)	Zip, map and lambda functions. You do not need to consider changing the map object to a list and can assume this is done for you. 

       def chooseLargest(a,b):
	   results = []
      	   list_len = len(a)
      	   for i in range (list_len):
          	results.append(max(a[i], b[i]))
       	   print results
       
chooseLargest([1,2,3,4,5],[2,2,9,0,9])

You are still permitted to use the inbuilt max() function. The inputs and output of the function should not change. 

'''

def chooseLargest(a,b):
	results = []
	list_len = len(a)
	for i in range (list_len):
		results.append(max(a[i], b[i]))
    
	print (results)
       
chooseLargest([1,2,3,4,5],[2,2,9,0,9])

#List Comprehension
# results = [expression iterator conditional]
def chooseLargest(a,b):
	list_len = len (a)
	results =  [max(a[i], b[i]) for i in range (list_len)]
	print (results)

#Zip, Map and Lambda rewrite
def chooseLargest(a,b):
	list_len = len (a)
	results =  [max(a[i], b[i]) for i in range (list_len)]
	print (results)

# map(some function, some iterable)
def chooseLargest(a,b):
	results = list(map(lambda pair:max(pair[0], pair[1]), zip(a,b)))
	#	results = list(map(lambda num1, num2:max(num1, num2), (a,b)))

