#======================
# Imports
#======================
import sys
import random
import string
import time
import os

from rich.traceback import install
from rich import print 
from rich.panel import Panel
from rich.console import Group
from rich.console import Console



#==========================
# Enables Console From Rich
#==========================
console = Console()



#=======================
# Enables Rich Traceback
#=======================
install()



#============================
# Applicaton Global Variables
#============================
time_START = float()
time_STOP = float()
internalText = []
displayText = []
wordList = "/home/otter/Documents/Typr/WordLists/Loki_Word_List_EN.txt"



#==========================
# Text Generation Functions
#==========================
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



#======================
# Display Text Function 
#======================
def displayChallengeText():

    global displayText

    print(
        Panel(
            displayText,

            title="[bold italic]Typr[/]",
            )
        )



#====================
# User Input Function
#====================
def plyrStart():

    global time_START, time_STOP, plyr_text

    # Records Start Time
    time_START = time.time()

    # Records Users Input
    try:
        plyr_text = console.input("[bold blue]> [/]")
    except:
        pass

    # Records Stop Time
    time_STOP = time.time()



#======================
# Calculation Functions
#======================
def textAcc(plyr_text, displayText, word_count):

    # Calculates Text Acc
    textACC = len(set(plyr_text.split()) & set(displayText.split()))

    textACC = int((textACC / word_count) * 100)

    return textACC



def timeTaken(time_STOP, time_START):

    # Gather Time Taken
    timetaken = int(time_STOP - time_START)

    return timetaken



def wordsPerMinute(time_STOP, time_START, word_Count):

    # Calculates Time Taken
    timeTaken = time_STOP - time_START

    # Calculates Words Per Minute
    wordsPerMinute = round((word_Count / (time_STOP - time_START) * 100))

    return wordsPerMinute



#====================
# Display Users Score
#====================
def displayUserScore():

    try:

        global plyr_text, displayText, time_STOP, time_START

        # Checks If User Input Is Same As Printed Text
        if plyr_text.strip() == displayText.strip() and plyr_text != "" and plyr_text.strip() >= displayText.strip():

            textAccuracy = textAcc(plyr_text, displayText, len((displayText).split()))
            timeTakenForTest = timeTaken(time_STOP, time_START)
            wordsPerMin = wordsPerMinute(time_STOP, time_START, len((displayText).split()))


            print(
                Panel(
                    f"[bold green]Accuracy: [/]{textAccuracy}%\n[bold yellow]Time Taken: [/]{timeTakenForTest}s\n[bold purple]Words Per Minute: [/]{wordsPerMin}",
                    title="[bold italic green]You Did It ! Wanna Do Another ?[/]",
                )
            )

        elif plyr_text.strip() != displayText.strip() and plyr_text != "" and plyr_text.strip() >= displayText.strip():

            textAccuracy = textAcc(plyr_text, displayText, len((displayText).split()))
            timeTakenForTest = timeTaken(time_STOP, time_START)
            wordsPerMin = wordsPerMinute(time_STOP, time_START, len((displayText).split()))


            print(
                Panel(
                    f"[bold green]Accuracy: [/]{textAccuracy}%\n[bold yellow]Time Taken: [/]{timeTakenForTest}s\n[bold purple]Words Per Minute: [/]{wordsPerMin}",
                    title="[bold italic red]Nice Try! Some Mistakes There Though, Wanna Do Another ?[/]",
                )
            )

        elif plyr_text.strip() < displayText.strip():

            print(
                Panel(
                    "[bold red]Invalid test, text not fully typed.[/]",
                    title="[bold italic red]ERROR[/]"
                    )
                )

        else:

             print(
                Panel(
                    "[bold red]Invalid Test, No Text Entered.[/]",
                    title="[bold italic red]ERROR[/]"
                    )
                )

    except:
        pass



if __name__ == "__main__":
    os.system('clear') # clears terminal window
    generateChallengeText()
    displayChallengeText()
    plyrStart()
    displayUserScore()

