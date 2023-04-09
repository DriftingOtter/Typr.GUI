#=======================
# Imports & Dependencies
#=======================
from tkinter import *
import random
import string
import time



#============================
# Variable States For Program
#============================
internalTimeLimit = 10 # (Default State: 10)
time_Limit = internalTimeLimit  # (Default State: 10)
internalTXTcounter = 0  # (Default State: 0)
timeSTART = 0 # (Default State: 0)
timeSTOP = 0 # (Default State: 0)
timeTaken = 0 # (Default State: 0)
timeFinished = int() # (Default State: int() )
keys_pressed = 0 # (Default State: int(0) )
timr_state = False  # (Default State: False)
highlightrunning = False  # (Default State: False)
restartState = False  # (Default State: False)
usr_error_Count = 0  # (Default State: 0)
numOfWords = 1  # (Default State: int() )
displayText = []  # (Default State: [])
internalText = []  # (Default State: [])
word_count = int()  # (Default State: int() )
wordsPerMinute = str() # (Default State: str() )
textACC = int() # (Default State: int() )
wordList = "/home/otter/Documents/Typr/WordLists/Loki_Word_List_EN.txt"



#======================
# Application Functions
#======================
def countdown():

    global usrEntryBox, time_Limit, restartState
    global internalTimeLimit, timeFinished

    if restartState:
        return

    # change text in label
    displayTimer["text"] = time_Limit

    if time_Limit > 0:

        if time_Limit > 0:

            earlyFinishCheck()

        if time_Limit > 0:

            time_Limit = time_Limit - 1

        # call countdown again after 1000ms (1s)
        root.after(1000, countdown)

    if time_Limit == 0:

        usrEntryBox.config(state=DISABLED)
        timeFinished = internalTimeLimit
        testOverCalculation()



def testOverCalculation():

    global timeSTART, timeSTOP, timeTaken, wordsPerMinute
    global word_count, displayText, usrEntryBox
    global timeFinished

    timeSTOP = time.time()
    timeTaken = timeSTOP - timeSTART

    gross_WPM(word_count, timeTaken)

    plyr_text = usrEntryBox.get("1.0", "end-1c")
    textAcc(str(plyr_text), displayText, word_count)

    timeFinished = round(timeTaken)

    displayResult()



def is_typing(event):

    global time_Limit, timr_state, timeSTART, restartState

    # check if the user is typing in the Text widget
    if timr_state == False and restartState == False:

        if len(usrEntryBox.get("1.0", "end-1c")) > 0:

            countdown()
            timeSTART = time.time()
            timr_state = True



def check_letter(event):

    global internalText, usrEntryBox, internalTXTcounter
    global highlightrunning, usr_error_Count

    if highlightrunning:
        return

    highlightrunning = True 


    current_letter = usrEntryBox.get("insert-1c", "insert")
    
    correct_letter = internalText[internalTXTcounter]

    usrEntryBox.tag_config("ErrorColor", background="red")


    if event.keysym == "BackSpace":

        if internalTXTcounter > 0:

            internalTXTcounter -= 1
            
            usrEntryBox.tag_remove("ErrorColor", "insert-1c", "insert")

            if usr_error_Count > 0:

                usr_error_Count -= 1
    
    else:

        if current_letter != correct_letter:

            if len(internalText) > internalTXTcounter:

                internalTXTcounter += 1

            usrEntryBox.tag_add("ErrorColor", "insert-1c", "insert")

            usr_error_Count += 1

        else:

            if len(internalText) > internalTXTcounter:

                internalTXTcounter += 1

            usrEntryBox.tag_remove("ErrorColor", "insert-1c", "insert")


    highlightrunning = False



def earlyFinishCheck():

    global usrEntryBox, displayText
    global timr_state, time_Limit, timeFinished

    if timr_state == True:

        last_letter = usrEntryBox.get("end-2c", "end-1c")

        usrTextLength = len(usrEntryBox.get("1.0", "end"))

        if usrTextLength == len(displayText):

            if last_letter.strip() == (displayText[-2:]).strip():

                usrEntryBox.config(state=DISABLED)
                
                time_Limit = 0



def restartTestDuringTest(event):

    global time_Limit, displayTimer, internalTimeLimit, restartState
    global usrEntryBox, challengeText, displayText, timr_state
    global timeSTART, timeSTOP, timeTaken
    global wordsPerMinute

    restartState = True

    time_Limit = internalTimeLimit
    timeSTART = 0
    timeSTOP = 0
    timeTaken = 0

    wordsPerMinute = str()

    displayTimer["text"] = "Please Begin Typing..."

    displayText = []

    generateChallengeText()

    if challengeText.get(1.0,"end") != "":
        challengeText.config(state = NORMAL)
        challengeText.delete("1.0", "end")
        challengeText.insert(INSERT, displayText)
        challengeText.config(state = DISABLED)
    else:
        challengeText.config(state = NORMAL)
        challengeText.insert(INSERT, displayText)
        challengeText.config(state = DISABLED)

    usrEntryBox.config(state = NORMAL)
    usrEntryBox.delete("1.0", "end")

    # Remove Result Widgets
    displayResultWPM.pack_forget()
    displayResultAcc.pack_forget()
    displayResultTimeTaken.pack_forget()
    restartTestButton.pack_forget()
    quitTestButton.pack_forget()


    # Packs Test Widgets
    gameInputAndOutputFrame.pack(anchor="center", expand=False, fill="none")
    gameInputAndOutputFrame.place_configure(relx=0.5, rely=0.5, anchor="center") 
    displayTimer.pack(pady=10)
    challengeText.pack(anchor=CENTER, pady=20)
    challengeText.insert(INSERT, displayText)
    challengeText.config(state=DISABLED)
    usrEntryBox.pack(anchor=CENTER)

    
    timr_state = False
    restartState = False



def restartTestAfterTest():

    restartTestDuringTest(None)
   


def backToMenu():

    navBar.pack_forget()
    smallappTitle.pack_forget()

    for widget in gameInputAndOutputFrame.winfo_children():
        widget.pack_forget()

    gameInputAndOutputFrame.place_forget()
    displayTimer.pack_forget()
    challengeText.delete("1.0", "end")
    challengeText.pack_forget()
    usrEntryBox.pack_forget()

    titlePageAppTitle.pack(side=TOP)
    titlePagePlayButton.pack(pady=5)
    titlePageQuitButton.pack(pady=5)
    titlePageFrame.place(relx=0.5, rely=0.5, anchor="center")



def gross_WPM(word_count, timeTaken):

    global wordsPerMinute

    wordsPerMinute = round(((word_count / timeTaken) * 100))



def textAcc(plyr_text, displayText, word_count):

    global textACC

    textACC = len(set(plyr_text.split()) & set(displayText.split()))
    textACC = round((textACC / word_count) * 100)
 


def generateChallengeText():

    global wordList, displayText, internalText, word_count, usrEntryBox

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

    # Removes  default array boiler plate
    displayText = "".join([str(elem) for elem in displayText])

    # arranges the text into 1 line via removing enter spaces
    displayText = displayText.translate({ord(c): " " for c in string.whitespace})

    # Finds Word Length Of Text
    word_count = len(displayText.split())
    word = displayText.strip()

    for character in word:

        internalText.append(character)

    else:
        pass



def displayResult():

    global displayTimer, gameInputAndOutputFrame
    global wordsPerMinute, textACC
    global timeFinished
    global restartTestButton

    displayTimer.pack_forget()
    challengeText.pack_forget()
    usrEntryBox.pack_forget()
    gameInputAndOutputFrame.pack_forget()

    displayResultWPM.pack(pady=10)
    displayResultAcc.pack(pady=10)
    displayResultTimeTaken.pack(pady=10)

    if wordsPerMinute != None:

        displayResultWPM['text'] = "Words Per Minute: " + str(wordsPerMinute)

    else:

        displayResultWPM['text'] = "[ERROR] No WPM Detected"

    if textACC != None:

        displayResultAcc['text'] = "Accuracy: " + str(textACC) + "%"

    else:

        displayResultAcc['text'] = "[ERROR] No Acc Detected"

    if timeFinished != None:

        displayResultTimeTaken['text'] = "Time Taken: " + str(timeFinished) + "s"

    else:

        displayResultTimeTaken['text'] = "[ERROR] No Acc Detected"


    restartTestButton.pack(pady=5)
    quitTestButton.pack(pady=5)



def titlePageQuit():

    root.destroy()



def titlePagePlay():

    global titlePageFrame, titlePageAppTitle, titlePagePlayButton, titlePageQuitButton

    #=======================
    # Removing Title Widgets
    #=======================
    for widget in titlePageFrame.winfo_children():
        widget.pack_forget()

    titlePageFrame.place_forget()

    #=======================
    # Inital Text Generation
    #=======================
    generateChallengeText()

    #===================
    # Packs Test Widgets
    #===================
    navBar.pack(anchor='n')
    navBar.pack_propagate(False)
    smallappTitle.pack(anchor='w', padx=10)
    gameInputAndOutputFrame.pack(anchor="center", expand=False, fill="none")
    gameInputAndOutputFrame.place_configure(relx=0.5, rely=0.5, anchor="center") 
    displayTimer.pack(pady=10)
    challengeText.pack(anchor=CENTER, pady=20)
    challengeText.insert(INSERT, displayText)
    challengeText.config(state=DISABLED)
    usrEntryBox.pack(anchor=CENTER)

    children = root.winfo_children()



#====================
# Application Widgets
#====================
root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Typr")
root.config(bg="#1A1A1A")



navBar = Frame(
        master=root, 
        bg=root['bg'], 
        height=100,
        width=root.winfo_screenwidth()
)



smallappTitle = Label(

        master=navBar,
        text="Typr",
        font=("Rubik Bold", 50, 'italic'),
        bg=root['bg'],
        fg="#ffffff"
)



gameInputAndOutputFrame = Frame(
    master=root, 
    bg=root["bg"], 
    width=(root.winfo_screenwidth() - 100)
)



displayTimer = Label(
    master=gameInputAndOutputFrame,
    text="Please Begin Typing...",
    font=("Rubik ExtraBold Italic", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



displayResultWPM = Label(
    master=gameInputAndOutputFrame,
    font=("Rubik ExtraBold", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



displayResultAcc = Label(
    master=gameInputAndOutputFrame,
    font=("Rubik ExtraBold Italic", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



displayResultTimeTaken = Label(
    master=gameInputAndOutputFrame,
    font=("Rubik ExtraBold Italic", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



restartTestButton = Button(
    master=gameInputAndOutputFrame,
    font=("Rubik Bold", 30),
    bg="#1A1A1A",
    fg="#ffffff",
    text="RETRY",
    command=restartTestAfterTest,
)



quitTestButton = Button(
    master=gameInputAndOutputFrame,
    font=("Rubik Bold", 30),
    bg="#1A1A1A",
    fg="#ffffff",
    text="RETURN TO MENU",
    command=backToMenu,
)



challengeText = Text(
    master=gameInputAndOutputFrame,
    font=("Rubik", 40),
    width=50,
    height=1,
    bg=root["bg"],
    fg="#ffffff",
    wrap=WORD,
    relief=FLAT,
    borderwidth=0,
    takefocus=0,
)



usrEntryBox = Text(
    master=gameInputAndOutputFrame,
    font=("Rubik", 40),
    width=challengeText["width"],
    height=1,
    bg=root["bg"],
    fg="#ffffff",
    relief=FLAT,
    borderwidth=0,
    takefocus=0,
    insertbackground="#ffffff",
    insertofftime=0,
    insertwidth=5,
)



titlePageFrame = Frame(
        master=root,
        bg=root['bg']
        )
titlePageFrame.pack()
titlePageFrame.place(relx=0.5, rely=0.5, anchor="center")



titlePageAppTitle = Label(
        master=titlePageFrame,
        text="Typr",
        font=("Rubik ExtraBold", 100),
        bg=root['bg'],
        fg=("#ffffff"),
) 
titlePageAppTitle.pack(side=TOP)



titlePagePlayButton = Button(
        master=titlePageFrame,
        text="Begin Test",
        font=("Rubik Bold", 30),
        bg=root['bg'],
        fg="#ffffff",
        relief=FLAT,
        command=titlePagePlay,
        )
titlePagePlayButton.pack(pady=5)



titlePageQuitButton = Button(
        master=titlePageFrame,
        text="Quit",
        font=("Rubik Bold", 30),
        bg=root['bg'],
        fg="#ffffff",
        relief=FLAT,
        command=titlePageQuit,
        )
titlePageQuitButton.pack(pady=5)



#=========================
# Bindings For Application
#=========================
root.bind(
    "<Configure>",
    lambda event: gameInputAndOutputFrame.place_configure(
        relx=0.5, rely=0.5, anchor="center"
    ),
)



usrEntryBox.bind("<KeyPress>", is_typing)
usrEntryBox.bind("<KeyRelease>", check_letter)



root.bind("<Escape>", restartTestDuringTest)



if __name__ == "__main__":
    root.mainloop()

