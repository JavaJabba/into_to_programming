
eircodeAreas = {'A63': 'Greystones', 'A98':'Bray', 'P17':'Kinsale', 'A86':'Dunboyne', 'W23':'Cellbridge', 
'F45':'Castlerea', 'F35':'Ballyhaunis', 'H14':'Belturbet', 'N39':'Longford', 'F56':'Ballymote'}

def generateEircodeAreas (filename):
    # IGNORE THIS FUNCTION AS WE HAVEN@T COVERED FILES - DICTIONARY HARD CODED ABOVE
    #connect to the file
    #read the contents from the file (into a list) and generate the dictionary. 
    return eircodeAreas

def getTownLand(eircode):
    #get the routing key from the eircode e.g. A63F4E2
    routingKey = eircode[0:3]
    townland = eircodeAreas[routingKey]

    #use this routing key as a key into the dictionary to get the value i.e. the townland
    return townland

def checkLegitEirCode(eircode):
    legitimate = True
    #check the length of the eircode (7 characters)
    #.isalpha .isnumeric
    if len(eircode) != 7:
        legitimate = False
        print ("Eircode needs to be 7 digits!")
        return legitimate
    elif eircode[0].isalpha() == False:
        legitimate = False
        print ("First Character must be a letter!")
        return legitimate
    elif eircode[1].isnumeric() == False or eircode[2].isnumeric() == False:
        legitimate = False
        print("The second and third characters need to be numbers!")
        return legitimate

    #check if the first character of the routing key is a letter

    #check if the 2nd and 3rd characters of the routing are numbers

    return legitimate

# eircodeAreas = generateEircodeAreas ("eircodes.txt")          
userEirCode = input("Please enter your eircode: ")
legit = checkLegitEirCode(userEirCode)
if legit:
    area = getTownLand(userEirCode)
    print ("You live in: ", area)