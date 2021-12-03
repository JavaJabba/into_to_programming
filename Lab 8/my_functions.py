# ScriptName:       my_functions.py
# Author:           Dylan Murray 121747725

import random

def while_loop(max_number=10):
    '''
    Write  a  function,  while_loop(max_number),  that  contains  a  while  loop  that  loops 
    from 1 to n, where n is a positive number (passed as parameter - max_number), 
    saving the number in a list on each loop.  The function shall return the list of all 
    numbers. Example of what is returned by the function call is shown. If no parameter 
    is passed to the function, while_loop() shall return the list of numbers from 1 to 10: 
        a. while_loop() -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
        b. while_loop(5) -> [1, 2, 3, 4, 5] (the list 1 to 5 is returned) 
    '''
    #establish my list variable to be type list.
    my_list = []
    #initiate while counter as 1 start.
    try:
        i = 1
        while i <= max_number or i >= max_number:
            #if max number is positive then execute
            if max_number >= 0:    
                my_list.append(i)
                if i == 12:
                    #if the the number reaches 12 then add the sum of values in list and return the list
                    my_list.append(sum(my_list))
                    #I could not understand how to break and still return the list.
                    return my_list
                elif i == max_number:
                    #if i has reached the max number then add the sum of the values in the list to the end.
                    my_list.append(sum(my_list))
                    return my_list
                #increment i
                i+=1
            #if max number is negative then execute
            elif max_number <=0:
                my_list.append(i)
                if i == -12:
                    #if the the number reaches 12 then add the sum of values in list and return the list
                    my_list.append(sum(my_list))
                    return my_list
                elif i == max_number:
                    #if i has reached the max number then add the sum of the values in the list to the end.
                    my_list.append(sum(my_list))
                    return my_list
                #decrement i
                i-=1 
    except:
        return "Did you break the break or should we continue"
    
def magic_8_ball(my_question, fixed_list=[]):
    '''
    Pass a question using the my_question param of the function and the 
    function will randomly choose one of the 20 possible answers as provided by the 
    Wiki. Maybe consider using a list to put the replies into. Call the function using - magic_8_ball(my_question) 
    
    add a second param, fixed_list, which is a list which contains index values from which 
    I only want the answer to come from - magic_8_ball(my_question, fixed_list).  I am 
    assuming the answers are read column by column.  So, if I pass in a list containing [0, 3, 8] 
    then the function will only return an answer that is randomly chosen from either “It is certain.” 
    or “Yes definitely.” or “Yes.”  Remember: if I call the function without this parameter, 
    all 20 answers are used to randomly generate the returned answered. 

    If a -1 is any of the value(s) in the fixed_list, I want your code to cause an error 
    (any error you want) and return as a string the error that occurred.  

    Make sure you add error handling for all non -1 error messages to return “I have spoken.” 
    '''
    try:
        #list of answer phrases.
        answer_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you know.", "Cannot predict now", "Concentrate and ask again.", "Don't count on it", "My reply is no.", "My sources say no", "Outlook not so good.", "Very doubtful."]
        #if fixed list is empty the pick random phrase from full list.
        if fixed_list == []:
            #get random number then find phrase in list at that value index.
            i = random.randint(0, 19)
            i = answer_list[i]
            return i
        else:
            #otherwise make new list of phrases from fixed list values.
            my_list = []
            i = 0
            while i < len(fixed_list):
            
                if fixed_list[i] == -1:
                    return "Connection to the spirit world lost, please add additional goats"
                #get int values from the fixed list and and create a new list with the phrases from them indexes.
                num = fixed_list[i]
                question = answer_list[num]
                my_list.append(question)
                i+=1
            else:
                #after list is created then get random answer based on any length of the list.
                length = len(my_list)
                i = random.randrange(0 , length)
                i = answer_list[i]
                return i
    except:
        return "I have spoken."
        
def all_pairs(s1, s2):
    '''
    Create a function called - all_pairs( s1, s2 ) with 2 parameters called:
    s1 - list/string    s2 - list/string
    which creates a list with all pairs of elements from sequences ‘s1’ and ‘s2’
    this all_pairs function returns two values:
    the first is a boolean to tell if an exception occurred
    the second is output of the function, if no exception occurred,
    or [-1] if an exception occurred
    '''
    #try and except to catch exceptions and return the required [-1].
    try:
        #initialise list.
        paired_list = []
        #for each item in s1.
        for i1 in s1:
            #get each item in s2.
            for i2 in s2:
                #cast to string and concat each value.
                pair = str(i1) + str(i2)
                #add pair to list.
                paired_list.append(pair)
        #return False as try except catches exceptions and also return the paired list.
        return False, paired_list
    except:
        return [-1]    
