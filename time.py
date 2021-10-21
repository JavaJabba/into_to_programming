#Script Name:       time.py
#Author:            Dylan Murray 121747725

import math

def tv_watched(question_string):
    user_input = int(input(question_string))
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
    return user_input

