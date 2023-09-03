import string
import random



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


def conv_LTS(lst): # Converts The Generated ChallengeText List -> String
    strText = " ".join([str(elem) for elem in lst])
    strText = strText.translate({ord(c): " " for c in string.whitespace})

    return str(strText)

