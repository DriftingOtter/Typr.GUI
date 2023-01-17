# Imports
import random
import string
import time


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


# Holds Word List Location
worldList = "V1.0.0/TypingGoBurrr_CLI/Source Code/Loki_Word_List_EN.txt"

with open(worldList, "r") as currenText:
    # Reads The Line Number From Text
    lines = currenText.readlines()



# Pre-delclears the variabe before generation
internalText = []

# makes loop for adding words into the displayText VAR
for i in range(0, 10):
    if i != 10:
        randomLineGen = random.randint(0, 977)  # the number of words in the word list
        word = lines[randomLineGen].strip()
        for character in word:
            internalText.append(character)
    else:
        break



# Pre-delclears the variabe before generation
displayText = []

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

print(displayText)
print("\n")

# Records Start Time
time_START = time.time()

# Allows User Input
plyr_text = input("// ")

# Records Stop Time
time_STOP = time.time()

# Checks If User Input Is Same As Printed Text
if plyr_text.strip() == displayText.strip():

    # Print Result Message
    print("\nYou Did It ! Wanna Do Another ?\n")

    print("Accuracy:", TextAcc(plyr_text, displayText, word_count), "%")
    print("Time Taken:", TimeTaken(time_STOP, time_START), "s")
    print("Words Per Minute:", WordsPerMinute(time_STOP, time_START, word_count, TimeTaken(time_STOP, time_START)))

else:

    # Print Result Message
    print("\nNice Try! Some Mistakes There Though, Wanna Do Another ?\n")

    print("Accuracy:", TextAcc(plyr_text, displayText, word_count), "%")
    print("Time Taken:", TimeTaken(time_STOP, time_START), "s")
    print("Words Per Minute:", WordsPerMinute(time_STOP, time_START, word_count, TimeTaken(time_STOP, time_START)))


    