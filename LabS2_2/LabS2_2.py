
def dnaSeq():
    textFile = open("dna.txt", "r")

    dnaFile = textFile.read()
    personDna = dnaFile.split("\n\n")
    i = 0
    for item in personDna:
        print(i, ":", item)
        i += 1

    textFile.close()
    return

def meanBoutsPerPatient():
    textFile = open("InflammatoryIBS.csv", "r")

    lines = textFile.readlines()
    noOfBouts = 0
    lineNo = 0
    sumBouts = 0
    for line in lines:
        lineValues = line.split(",")
        i = 0
        while i < len(lineValues):
            boutValue = lineValues[i]
            sumBouts = sumBouts + int(boutValue)
            noOfBouts += 1
            i += 1
        meanbouts = sumBouts / noOfBouts
        lineNo += 1
        print("Patient ", lineNo ," had", round(meanbouts), "bouts on average")
    
    textFile.close()
    return 

def meanBoutsAcrossAllPatients():
    textFile = open("InflammatoryIBS.csv", "r")
    allPatients = textFile.read()
    allBouts = allPatients.split(",") 



    textFile.close()
    return


meanBoutsPerPatient()
# dnaSeq()