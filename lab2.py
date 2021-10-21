#Script Name:       lab2.py
#Author:            Dylan Murray 121747725

import math

#testing github changes

def what_is_my_name():
    #Get first name
    first_name = input("What is your first name? ")
    first_name.lower
    #Get surname
    surname = input("What is your surname? ")
    surname.lower
    #Print
    print("Hello %s" % first_name.capitalize + " " + surname + "!")
    
#what_is_my_name()

def what_is_my_type ():
    #Get int variable
    int_check = int(input("What is your favorite number? ")) 

    #check and print int variable type
    print("You have entered", int_check, "and it's variable type is:", type(int_check), "and this object has an id of", id(int_check))

what_is_my_type()

def tv_watched ():
    #get minutes watched
    tvTime = float(input("Enter minutes watching tv: "))

    #calculate time watched and separate the hours.
    hoursWatched = math.floor(tvTime/60)

    #calculate left over minutes.
    minutesWatched = math.floor(tvTime-(hoursWatched*60))

    #print formatting if else statement if time spent is either full hour or not.
    if minutesWatched == 0:
        print("There were", hoursWatched, "Hour(s) spent watching TV")
    elif minutesWatched >0:
        print("There were", hoursWatched, "Hour(s) and", minutesWatched, "Min(s) spent watching TV")

#tv_watched()