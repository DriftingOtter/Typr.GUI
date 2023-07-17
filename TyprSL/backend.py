import random
import string
import time




wordList = "/home/daksh/Documents/Typr/WordLists/Loki_Word_List_EN.txt"




#==========================================
# Random Challenge Text Generation Function
#==========================================
def generateChallengeText(numOfWords):

    global wordList

    displayText = []

    with open(wordList, "r") as currenText:
        # Reads The Line Number From Text
        lines = currenText.readlines()
        numLines = len(lines)

    # Generate a random line number between 0 to number of lines in the file
    randomLineGen = random.randint(0, numLines - 1)

    # makes loop for adding words into the displayText VAR
    for z in range(0, numOfWords):
        if z != numOfWords:
            randomLineGen = random.randint(
                0, 977
            )  # the number of words in the word list

            displayText.append(lines[randomLineGen])
            randomLineGen = random.randint(0, numLines - 1)
        else:
            break

    
    # Removes The \n Sequence From The List
    displayText = [word[:-1] for word in displayText]

    return displayText







