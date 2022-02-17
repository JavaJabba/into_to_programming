

def load_data (filename):

    #create a dictionary - let's call it Infections
    infections = {}

    #read in the data from the file - How should I read this?
    inFile = open(filename, "r")
    #get every line of data
    lineNo = 0
    lines = inFile.read()
    for line in lines.split("\n"):
        if line != "":
            #split it on the comma
            line = line.split(",")
            index = 0
            while index < len(line):
                line[index] = line[index].strip()
                index +=1
            print(line)
            lineNo += 1
            


        #dict[key] = value
    inFile.close()
    # return infections

def daily_cases (cumulative):
    #create a new dictionary called newInfections

    #for every case in the cumulative dictionary i.e. for every county

        #for every list of cumulative infection values

            #if it's the first value recorded, take it as is. Record this in the newInfections dictionary as a new value

            #else get the current cumulative value
            #subtract the number from the day before
            #append it to the county in newInfections

    #return the newInfections dictionary
    return newInfections

load_data("occurences.txt")
# cumulativeInfections = load_data("occurences.txt")
# newInfectionRates = daily_cases (cumulativeInfections)