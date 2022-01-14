import random

def collectStringInput():
    usersPlay = input()
    return usersPlay

def generateIntegerValue():
    intVal = random.randint(1,6)
    return intVal

def convertIntegerToRPS(generateIntegerValue):
    if generateIntegerValue() == 1:
        computersPlay = 'p'
    elif generateIntegerValue() == 2:
        computersPlay = 'r'
    elif generateIntegerValue() == 3:
        computersPlay = 's'
    elif generateIntegerValue() == 4:
        computersPlay = 'P'
    elif generateIntegerValue() == 5:
        computersPlay = 'R'
    else:
        computersPlay = "S"
    return chr(computersPlay)

def evaluateWinning(collectStringInput, convertIntegerToRPS):
    if collectStringInput == 'r' or collectStringInput == 'R':
        if convertIntegerToRPS == 'p' or convertIntegerToRPS == 'P':
            return "Paper covers rock.\nComputer WINS!"
        elif convertIntegerToRPS == 's' or convertIntegerToRPS == 'S':
            return "Rock smashes scissor.\nPlayer WINS!"
        else:
            return "Tie!"
    elif collectStringInput == 'p' or collectStringInput == 'P':
        if convertIntegerToRPS == 's' or convertIntegerToRPS == 'S':
            return "Scissor cuts paper.\nComputer WINS!"
        elif convertIntegerToRPS == 'r' or convertIntegerToRPS == 'R':
            return "Paper covers rock.\nPlayer WINS!"
        else:
            return "Tie!"
    else:
        if convertIntegerToRPS == 'r' or convertIntegerToRPS == 'R':
            return "Rock smashes scissor.\nComputer WINS!"
        elif convertIntegerToRPS == 'p' or convertIntegerToRPS == 'P':
            return "Scissor cuts paper\nPlayer WINS!"
        else:
            return "Tie!"
    
    
