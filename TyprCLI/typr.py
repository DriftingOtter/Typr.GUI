#!/usr/bin/python

import sys
import string
import random
import time
import os

from rich import print
from rich.traceback import install
from rich.panel import Panel
from rich.console import Console


# Enables Console From Rich
console = Console()
install()



time_START = float()
time_STOP = float()
challengeText = str()
plyr_response = str()



def generateChallengeText(numOfWords):
    wordList = "/home/daksh/Documents/Typr/WordLists/Loki_Word_List_EN.txt"
    challengeText = []

    with open(wordList, "r") as currentText:
        lines = currentText.readlines()

    numLines = len(lines)

    for words in range(numOfWords):
        randomLineGen = random.randint(0, numLines - 1)
        challengeText.append(lines[randomLineGen].strip())

    return challengeText



# Converts The Generated ChallengeText List -> String
def conv_LTS(lst):
    strText = " ".join([str(elem) for elem in lst])
    strText = strText.translate({ord(c): " " for c in string.whitespace})

    return str(strText)



def displayChallengeText(challengeText):
    print(
        Panel(
            challengeText,
            title="[bold italic]Typr[/]",
        )
    )



def test():
    global time_START, time_STOP, plyr_response

    time_START = time.monotonic()

    try:
        plyr_response = console.input("[bold blue]> [/]")
    except KeyboardInterrupt:
        sys.exit()

    time_STOP = time.monotonic()

    testResults = [time_START, time_STOP, str(plyr_response)]

    return testResults



def accuracy(plyr_response, challengeText):
    try:
        correctWords = sum(
            1 for word in plyr_response.split() if word in challengeText.split()
        )
        totalWords = len(challengeText.split())
        accuracyPercentage: int = int((correctWords / totalWords) * 100)
    except ZeroDivisionError:
        accuracyPercentage = "INVALID"

    return accuracyPercentage



def timeTaken(time_START, time_STOP):
    try:
        timetaken = int(time_STOP - time_START)
    except ZeroDivisionError:
        timetaken = "INVALID"

    return timetaken



def wordsPerMinute(time_START, time_STOP, plyr_response):
    try:
        wordsTyped = len(plyr_response.split())
        timeTakenInMinutes = (time_STOP - time_START) / 60
        wordsPerMinute = wordsTyped / timeTakenInMinutes
        wordsPerMinute = round(wordsPerMinute)
    except ZeroDivisionError:
        wordsPerMinute = "INVALID"

    return wordsPerMinute



def calculateResults(testResults, challengeText):
    wpm = wordsPerMinute(testResults[0], testResults[1], testResults[2])
    acc = accuracy(testResults[2], challengeText)
    ttk = timeTaken(testResults[0], testResults[1])

    testResults = [acc, ttk, wpm, testResults[2], challengeText]

    return testResults



def displayUserScore(testResults):
    try:
        os.system("clear")

        if testResults[3].strip() == testResults[4].strip() and testResults[3] != "":
            print(
                Panel(
                    f"[bold green]Accuracy: [/]{testResults[0]}%\n[bold yellow]Time Taken: [/]{testResults[1]}s\n[bold purple]Words Per Minute: [/]{testResults[2]}",
                    title="[bold italic green]You Did It! Wanna Do Another ?[/]",
                )
            )

        elif testResults[3].strip() != testResults[4].strip() and testResults[3] != "":
            print(
                Panel(
                    f"[bold green]Accuracy: [/]{testResults[0]}%\n[bold yellow]Time Taken: [/]{testResults[1]}s\n[bold purple]Words Per Minute: [/]{testResults[2]}",
                    title="[bold italic red]Nice Try! Some Mistakes There Though, Wanna Do Another ?[/]",
                )
            )

        else:
            print(
                Panel(
                    '"Practice makes perfect" - Some one smart.',
                    title="[bold italic yellow]Test Invalid, try again.[/]",
                )
            )

    except KeyboardInterrupt:
        sys.exit()



if __name__ == "__main__":

    # Default Test Word Count
    wordCount: int = 10

    # Gather script arguments
    args = sys.argv

    # Checks for args
    try:
        if len(args) > 1:
            if args[1] == "-wc":
                wordCount = int(args[2])
            else:
                raise ValueError("Incorrect argument")
        else:
            raise IndexError("Missing argument")

    # If there are no ags commands, then don't show error
    except IndexError:
        pass

    # If garbage args are given
    except ValueError:
        print(
                Panel(
                    "Incorrect flag given. Please try the '-h' flag to check avalible flags.",
                    title="[bold italic red]Invalid Arguments.[/]",
                )
            )

    os.system("clear")

    challengeText = conv_LTS(generateChallengeText(wordCount))
    displayChallengeText(challengeText)
    displayUserScore(calculateResults(test(), challengeText))
