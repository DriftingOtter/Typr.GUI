# ------------------------------------------------------------------------------#
# Name: Typing Go Burrr (Command Line Version)
# Version: 1.0.0
# Summary: A Minimalistic Typing Test Application In The Terminal
# Home-page: N/A
# Author: Daksh Kaul
# Author-email: dakshkaul7790@gmail.com
# License: N/A
# ------------------------------------------------------------------------------#

# Imports
import random
import string
import time 

# Holds Word List Location
worldList = 'C:/Users/daksh/OneDrive/Desktop/Typing go burrr/IA - Typing go burrr/Word List/Master_EN_Word_List.txt'

# Reads Word List Into A Variable 
currenText = open(worldList,"r")

# Reads The Line Number From Text
lines = currenText.readlines()

# Pre-delclears the variabe before generation
displayText = []

# makes loop for adding words into the displayText VAR
for i in range (0,10):
    if i != 10:
        randomLineGen = random.randint(0, 2000)
        displayText.append(lines[randomLineGen])
    else:
        break

# Removes  default array boiler plate
displayText = ''.join([str(elem) for elem in displayText])

# Displays Text without white spaces 
print(displayText.translate({ord(c): ' ' for c in string.whitespace}))
print("")

# Stores display data into a string only var
displayTextSTR = displayText.translate({ord(c): ' ' for c in string.whitespace})

# Finds Word Length Of Text 
word_count = len(displayTextSTR.split())

# Records Start Time
time_START = time.time()

# Allows User Input
plyr_text = input(">> ")

# Records Stop Time
time_STOP = time.time()

# Checks If User Input Is Same As Printed Text
if plyr_text.strip() == displayTextSTR.strip():

    # Print Result Message
    print("\nYou Did It ! Wanna Do Another ?\n")

    # Calculates Text Acc
    textACC = len(set(plyr_text.split()) & set(displayTextSTR.split()))
    textACC = ((textACC/word_count)*100)

    # Calculates Time Taken
    timeTaken = time_STOP - time_START
    wordPM = int((word_count/timeTaken)*100)

    # Gather Time Taken
    timer_counter_val = int(time_STOP - time_START)

    # Displays The WPM and ACC
    print("Words Per Minute:", wordPM, "\n")
    print("Accuracy:", textACC, "%\n")
    print("Time Taken:", timer_counter_val, "s\n")

else:

    # Print Result Message
    print("\nNice Try! Some Mistakes There Though, Wanna Do Another ?\n")

    # Calculates Text Acc
    textACC = len(set(plyr_text.split()) & set(displayTextSTR.split()))
    textACC = ((textACC/word_count)*100)

    # Calculates Time Taken
    timeTaken = time_STOP - time_START
    wordPM = int((word_count/timeTaken)*100)

    # Gather Time Taken
    timer_counter_val = int(time_STOP - time_START)

    # Displays The WPM and ACC
    print("Words Per Minute:", wordPM, "\n")
    print("Accuracy:", textACC, "%\n")
    print("Time Taken:", timer_counter_val, "s\n")

# Closes Main File After Use
currenText.close()
