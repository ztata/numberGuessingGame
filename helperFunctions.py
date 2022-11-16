import random

def generateRandomNumber():
    number = random.randint(1,10)
    return number

def checkValidNumber(num):
    if num == None:
        return False
    elif num > 10:
        return False
    elif num < 1:
        return False
    else:
        return True

def parseUserInput(num):
    return int(num) if num.isdecimal() else None

def repeatGame():
    validInput = False
    while validInput == False:
        userInput = input("Would you like to guess again (Y/N)?")
        if userInput.strip().lower() == "y":
            return True
        elif userInput.strip().lower() == "n":
            print("See you soon!")
            return False
        else:
            print("You have to either enter a Y or an N to continue")


