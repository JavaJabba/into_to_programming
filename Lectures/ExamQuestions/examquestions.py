'''
The “Fizz Buzz” test is commonly given to graduate programmers to examine their basic 
logic and programming skills: Write a program that prints the numbers from 1 to 100. For 
multiples of three, print “Fizz” instead of the number. For multiples of five, print “Buzz” 
instead of the number. For numbers which are multiples of both three and five print 
“FizzBuzz” instead of the number. 
'''

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

'''
The function below accepts a string as an input and returns a string with the vowels 
removed. Rewrite the highlighted section using a list comprehension. 
def removeVowels(sentence): 
vowels = “aeiou” 
   filtered_list = [] 
    for l in sentence: 
        if l not in vowels: 
           filtered_list.append(l) 
             return “ “.join (filtered_list) 
'''

# def removeVowels(sentence):
#     vowels = "aeiou" 
#     filtered_list = [l for l in sentence if l not in vowels]
#     return " ".join (filtered_list) 

'''
Rewrite the code below to use lambda and map(). You can assume the output of map is cast 
to a list. You should still zip the two lists.          
 
list1 = [1,2,3] 
list2 = [10,20,30] 
totals = [] 
for tup in zip(list1, list2): 
  totals.append (tup[0] + tup[1]) 
print (totals) 
'''

# list1 = [1,2,3] 
# list2 = [10,20,30] 
# totals = list(map(lambda pair: pair[0] + pair[1], zip(list1, list2)))

'''
What is the output of the following program? 
for x in range(1,6): 
     for y in range(1,x+1): 
            print (x,' ',y) 
'''

#1,1 2,1 2,2 3,1 3,2 3,3 4,1 4,2 4,3 4,4 5,1 5,2 5,3 5,4 5,5 

'''
What would the output of the following code be? 
 
    numbers = [1,2,3,4] 
    print (numbers[::-2])
'''

#4, 2

'''
What is the output of the following program? 
 
x = 6 
while x < 9: 
    print(x) 
    x = x + 2 
print(x) 
while x > 7: 
    print (x) 
    x = x - 1 
'''

# 6,8,10,10,9,8

'''
You have been tasked with writing software to grade student MCQ assessments. The MCQ 
contained 25 questions and the answers are in a list called answer_key as shown:  
 
answer_key  = 
['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D'] 
 
The students answers are in a file called students.txt in the following format: 
 
N00000001,A,A,D,D,C,D,D,A,,C,D,B,C,,B,C,B,D,A,C,,A,,C,D 
N00000002,,A,,D,,B,D,A,C,C,D,,A,A,A,C,B,D,C,C,A,A,B,,D 
 
The first number is the student ID. The following 25 letters are the student responses to 
particular questions. If no letter follows the comma, the student did not answer.  
 
 
 
Process the file to find out : 
 
a) The total number of students who took the MCQ.  
b) The grade for each student. This can be done by comparing the student's answers to the 
list answer_key. Scores are calculated as follows: +4 points for every right answer, 0 
points for every skipped and incorrect answer. 
c) The highest overall score. 
d) The lowest overall score. 

Write the answers from parts a, c and d above to a file called analysis.txt. 
'''
# answer_key  = ['B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D'] 

# inFile = open("students.txt", "r")
# outFile = open("analysis.txt", "w")

# students = inFile.readlines()
# studentScores = []
# for student in students:
#     student = student.strip("\n")
#     student = student.split(",")
#     studentID = student[0]
#     studentAnswers = student[1:]
#     studentScore = 0
#     for answerPos in  range(len(studentAnswers)):
#         if studentAnswers[answerPos] == answer_key[answerPos]:
#             studentScore += 4
#     studentScores.append(studentScore) #grade for every student

# #total number of students
# numStudents = len(studentScores)
# outFile.write("The number of students is %s" % numStudents)

# #highest score
# maxScore = max(studentScores)
# outFile.write("The Maximum Score is %s" % maxScore)

# #lowest score
# lowScore = min(studentScores)
# outFile.write("The Lowest Score is %s" % lowScore)


# inFile.close()
# outFile.close()

'''

'''