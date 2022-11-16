import time
import helperFunctions

repeat = True
while repeat == True:
    print(" ")
    print("Welcome to the number guessing game.")
    print("Coming up with a number for you to guess now")
    number_to_guess = helperFunctions.generateRandomNumber()
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Okay, got it.")
    i = 3
    guessed_correctly = False
    
    while i > 0:
        userInput = input("Please enter your guess (between 1 and 10 inclusive): ")
        userInput = helperFunctions.parseUserInput(userInput)
        isValidInput = helperFunctions.checkValidNumber(userInput)
        if isValidInput == False:
            i -= 1
            print("You have to guess an integer between 1 and 10. Try again")
            print("You have " + str(i) + " guesses remaining")
            continue

        if userInput > number_to_guess:
            i -= 1
            print("Too high, try again!")
            print("You have " + str(i) + " guesses remaining")
            continue
        elif userInput < number_to_guess:
            i -= 1
            print("Too low, try again!")
            print("You have " + str(i) + " guesses remaining")
            continue
        else:
            guessed_correctly = True
            print("You guessed it, nice work!")
            break

    if guessed_correctly == True:
        print("You have a masterful grasp of numbers 1 to 10.")
    else:
        print("Keep at it and one day you will master the numbers between 1 and 10")

    repeat = helperFunctions.repeatGame()

print("Thanks for playing!")

