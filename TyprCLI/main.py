# Imports
import random
import string
import time
import os
from colorama import Fore, Back, Style
from colorama import init

# Auto resets styles after each print
init(autoreset=True)

time_START = float()
time_STOP = float()
word_count = int()
internalText = []
displayText = []

# Holds Word List Location
wordList = "/home/otter/Documents/Typr/WordLists/Loki_Word_List_EN.txt"


# Functions For Calculation
def TextAcc(plyr_text, displayText, word_count):

    # Calculates Text Acc
    textACC = len(set(plyr_text.split()) & set(displayText.split()))
    textACC = (textACC / word_count) * 100

    return int(textACC)


def TimeTaken(time_STOP, time_START):

    # Gather Time Taken
    time_taken = int(time_STOP - time_START)

    return time_taken


def WordsPerMinute(time_STOP, time_START, word_count, timeTaken):

    # Calculates Time Taken
    timeTaken = time_STOP - time_START

    # Calculates Words Per Minute
    wordsPM = int((word_count / timeTaken) * 100)

    return wordsPM


def generateChallengeText():

    global wordList, displayText, internalText, word_count

    with open(wordList, "r") as currenText:
        # Reads The Line Number From Text
        lines = currenText.readlines()




    # makes loop for adding words into the displayText VAR
    for i in range(0, 10):
        if i != 10:
            randomLineGen = random.randint(0, 977)  # the number of words in the word list
            word = lines[randomLineGen].strip()
            for character in word:
                internalText.append(character)
        else:
            break


    # makes loop for adding words into the displayText VAR
    for z in range(0, 10):
        if z != 10:
            randomLineGen = random.randint(0, 977)  # the number of words in the word list
            displayText.append(lines[randomLineGen])
        else:
            break

    # Removes  default array boiler plate
    displayText = "".join([str(elem) for elem in displayText])

    # arranges the text into 1 line via removing enter spaces
    displayText = displayText.translate({ord(c): " " for c in string.whitespace})


    # Finds Word Length Of Text
    word_count = len(displayText.split())

    print(Fore.RED + "[", displayText, Fore.RED + "]")
    print("\n")


def plyrStart():

    global time_START, time_STOP, plyr_text

    # Records Start Time
    time_START = time.time()

    # Allows User Input
    plyr_text = input(Fore.CYAN + "> ")

    # Records Stop Time
    time_STOP = time.time()


def checkPlyrScore():

    global plyr_text, displayText, word_count, time_STOP, time_START, word_count

    # Checks If User Input Is Same As Printed Text
    if plyr_text.strip() == displayText.strip():

        # Print Result Message
        print(Fore.GREEN + "\nYou Did It ! Wanna Do Another ?\n")

        print(Fore.BLUE + "Accuracy:", TextAcc(plyr_text, displayText, word_count), "%")
        print(Fore.YELLOW + "Time Taken:", TimeTaken(time_STOP, time_START), "s")
        print(Fore.MAGENTA + "Words Per Minute:", 
              WordsPerMinute(time_STOP, time_START, word_count, TimeTaken(time_STOP, time_START)))

    else:

        # Print Result Message
        print(Fore.RED + "\nNice Try! Some Mistakes There Though, Wanna Do Another ?]\n")


        print(Fore.GREEN + "[Accuracy:", TextAcc(plyr_text, displayText, word_count), "%]")
        print(Fore.YELLOW + "[Time Taken:", TimeTaken(time_STOP, time_START), "s]")
        print(Fore.MAGENTA + "[Words Per Minute:", 
              WordsPerMinute(time_STOP, time_START, word_count, TimeTaken(time_STOP, time_START)),"]")




while True:

    os.system('clear')
    generateChallengeText()
    plyrStart()
    checkPlyrScore()

    tryagain = input(Fore.BLUE + "\nWanna Another Try ? (y/n): ")

    if tryagain.lower() == 'n':   
        break
    else:
        
        os.system('clear')
        pass
        


