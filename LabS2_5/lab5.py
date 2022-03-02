

def readDraws(filename):
    textfile = open(filename, 'r')
    lines = textfile.readlines()
    lineNo = 0
    draws = []
    for line in lines:
        line = line.split()
        draws.append(line)
        lineNo += 1
    textfile.close()
    return draws

def checkWinners(lotteryDraws):
    userDraws = input("Enter your Lottery Numbers:\t")
    userDraws = userDraws.split()
    userDraws.sort()
    for list in lotteryDraws:
        list.sort()
        for number in range(len(userDraws)):
            if userDraws[number] != list[number]:
                print("Better luck next time")
        return "You Have Won!"



print(readDraws("lotteryNumbers.txt"))
lotteryDraws = readDraws("lotteryNumbers.txt")
print(checkWinners(lotteryDraws))