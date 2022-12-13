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
import os
import random
import string
import time 
import sys

# Fuction Class For Game Containing
def typing_go_burrr():

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
        print("\n----------You Did It ! Wanna Do Another ?----------\n")

        # Calculates Text Acc
        textACC = len(set(plyr_text.split()) & set(displayTextSTR.split()))
        textACC = ((textACC/word_count)*100)

        # Calculates Time Taken
        timeTaken = time_STOP - time_START
        wordPM = int((word_count/timeTaken)*100)

        # Gather Time Taken
        timer_counter_val = int(time_STOP - time_START)

        # Displays The WPM and ACC
        print(" // Words Per Minute:", wordPM, "\n")
        print(" // Accuracy:", textACC, "%\n")
        print(" // Time Taken:", timer_counter_val, "s\n")

        print("\n---------------------------------------------------\n")

    else:

        # Print Result Message
        print("\n----------Nice Try! Some Mistakes There Though, Wanna Do Another ?----------\n")

        # Calculates Text Acc
        textACC = len(set(plyr_text.split()) & set(displayTextSTR.split()))
        textACC = ((textACC/word_count)*100)

        # Calculates Time Taken
        timeTaken = time_STOP - time_START
        wordPM = int((word_count/timeTaken)*100)

        # Gather Time Taken
        timer_counter_val = int(time_STOP - time_START)

        # Displays The WPM and ACC
        print(" // Words Per Minute:", wordPM, "\n")
        print(" // Accuracy:", textACC, "%\n")
        print(" // Time Taken:", timer_counter_val, "s\n")

        print("\n----------------------------------------------------------------------------\n")

    # Closes Main File After Use
    currenText.close()

# Fuction For Clearing Screen
def clearscreen(numlines=100):

  if os.name == "posix":

    # Unix/Linux/MacOS/BSD/etc
    os.system('clear')

  elif os.name in ("nt", "dos", "ce"):

    # DOS/Windows
    os.system('CLS')

  else:

    # Fallback for other operating systems.
    print('\n' * numlines)

# Fuction To Print A Basic Terminal GUI Menu
def menu():

    print("\n-----------------TYPING GO BURRR--------------\n")
    print("[1] - Start Game\n")
    print("\n")
    print("[2] - Quit\n")
    print("----------------------------------------------\n")

# Pre-declear Variable
menu_option_picker = None

# Fuction To Take User Input For Menu
def menu_user_input_fuction():

    # Declear The Variable As Gobal Var
    global menu_option_picker

    # Take In Value For User Option At Title Screen
    menu_option_picker = int(input(">> "))


# Loops / Waits For User To Input Option
while menu_option_picker != 0:

    # Checks For Option 1
    if menu_option_picker == 1:

        # Clearing The Screen
        clearscreen()

        # Starting Game
        typing_go_burrr()

        break

    # Checks For Option 2
    elif menu_option_picker == 2:

        # Closes The Application
        sys.exit()

    # Checks For Return Value State
    else:
        
        # Acts As Return Value
        menu()
        menu_user_input_fuction()
            

# Calls Menu Fuction 
menu()

# Calls Menu User Input Fuction
menu_user_input_fuction()
