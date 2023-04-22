#====================
# Ott6r // Daksh Kaul
#====================



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
time_Limit = internalTimeLimit  # (Default State: internalTimeLimit)
internalTXTcounter = 0  # (Default State: 0)
timeSTART = 0 # (Default State: 0)
timeSTOP = 0 # (Default State: 0)
timeTaken = 0 # (Default State: 0)
timeFinished = int() # (Default State: int())
keys_pressed = 0 # (Default State: 0)
timr_state = False  # (Default State: False)
highlightrunning = False  # (Default State: False)
restartState = False  # (Default State: False)
usr_error_Count = 0  # (Default State: 0)
numOfWords = 10  # (Default State: 10)
displayText = []  # (Default State: [])
internalText = []  # (Default State: [])
word_count = int()  # (Default State: int())
wordsPerMinute = str() # (Default State: str())
textACC = int() # (Default State: int())
wordList = "/home/otter/Documents/Typr/WordLists/Loki_Word_List_EN.txt"



#========================
# Display Timer Countdown
#========================
def countdown():

    global usrEntryBox, time_Limit, restartState
    global internalTimeLimit, timeFinished


    if restartState == True:
        return


    if len(usrEntryBox.get("1.0", "end-1c")) <= 0:
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



#=======================
# Test Over Calculations
#=======================
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



#================================================
# Function To Check If Typing Has Already Started
#================================================
def is_typing(event):


    global time_Limit, timr_state, timeSTART, restartState, usrEntryBox

    # check if the user is typing in the Text widget
    if timr_state == False and restartState == False:

            if len(usrEntryBox.get("1.0", "end-1c")) > 0:

                countdown()
                timeSTART = time.time()
                timr_state = True



#====================
# Syntax Highlighting
#====================
def check_letter(event):

    global internalText, usrEntryBox, internalTXTcounter
    global highlightrunning, usr_error_Count

    if highlightrunning:
        return

    highlightrunning = True 


    current_letter = usrEntryBox.get("insert-1c", "insert")

    try:
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

    except:
        pass


    highlightrunning = False



#============================================
# Checker Functions For Early Test Completion
#============================================
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



#=====================================
# Restart Function For During The Test
#=====================================
def restartTestDuringTest(event):

    global time_Limit, displayTimer, internalTimeLimit, restartState
    global usrEntryBox, challengeText, displayText, timr_state
    global timeSTART, timeSTOP, timeTaken
    global wordsPerMinute, internalTXTcounter

    restartState = True
    time_Limit = 0

    internalTimeLimit = 10 # (Default State: 10)
    time_Limit = internalTimeLimit  # (Default State: internalTimeLimit)
    internalTXTcounter = 0  # (Default State: 0)
    timeSTART = 0 # (Default State: 0)
    timeSTOP = 0 # (Default State: 0)
    timeTaken = 0 # (Default State: 0)
    timeFinished = int() # (Default State: int())
    keys_pressed = 0 # (Default State: 0)
    highlightrunning = False  # (Default State: False)
    usr_error_Count = 0  # (Default State: 0)
    numOfWords = 10  # (Default State: 10)
    displayText = []  # (Default State: [])
    internalText = []  # (Default State: [])
    word_count = int()  # (Default State: int())
    wordsPerMinute = str() # (Default State: str())
    textACC = int() # (Default State: int())

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
    if displayResultWPM.winfo_ismapped():
        displayResultWPM.pack_forget()


    if displayResultAcc.winfo_ismapped():
        displayResultAcc.pack_forget()


    if displayResultTimeTaken.winfo_ismapped():
        displayResultTimeTaken.pack_forget()

    if restartTestButton.winfo_ismapped():
        restartTestButton.pack_forget()

    
    if quitTestButton.winfo_ismapped():
        quitTestButton.pack_forget()


    # Packs Test Widgets
    iOFrame.pack(anchor="center", expand=False, fill="none")
    iOFrame.place_configure(relx=0.5, rely=0.5, anchor="center") 
    displayTimer.pack(pady=10)
    challengeText.pack(anchor=CENTER, pady=20)
    challengeText.insert(INSERT, displayText)
    challengeText.config(state=DISABLED)
    usrEntryBox.pack(anchor=CENTER)

    timr_state = False
    restartState = False



#====================================
# Restart Function After Test Is Over
#====================================
def restartTestAfterTest():
    restartTestDuringTest(None)
   


#=============================
# Return To Main Menu Function
#=============================
def returnToMenu():

    global displayText, challengeText, usrEntryBox, displayTimer
    global timeSTOP, timeSTART, time_Limit, internalTimeLimit, timeTaken
    global wordsPerMinute, internalTXTcounter

    if navBar.winfo_ismapped():

        if smallappTitle.winfo_ismapped():
            navBar.pack_forget()
            smallappTitle.pack_forget()


    for child in iOFrame.winfo_children():
        if child.winfo_ismapped():

            child.pack_forget()


    if iOFrame.winfo_ismapped():
        iOFrame.place_forget()


    if displayTimer.winfo_ismapped():
        displayTimer.pack_forget()


    if challengeText.winfo_ismapped():
        challengeText.delete("1.0", "end")
        challengeText.pack_forget()


    if usrEntryBox.winfo_ismapped():
        usrEntryBox.pack_forget()

    titlePageAppTitle.pack(side=TOP)
    titlePagePlayButton.pack(pady=5)
    titlePageQuitButton.pack(pady=5)
    titlePageFrame.place(relx=0.5, rely=0.5, anchor="center")

    #=========================================
    # Resets Elements Before Returning To Menu
    #=========================================

    time_Limit = internalTimeLimit
    timeSTART = 0
    timeSTOP = 0
    timeTaken = 0

    wordsPerMinute = str()

    displayTimer["text"] = "Please Begin Typing..."
    displayText = []

    internalTXTcounter = 0

    challengeText.config(state=NORMAL)
    challengeText.delete("1.0", "end")

    usrEntryBox.config(state=NORMAL)
    usrEntryBox.delete("1.0", "end")

     
    #=========================
    # Bindings For Widgets
    #=========================
    root.unbind( "<Configure>", lambda event: iOFrame.place_configure(relx=0.5, rely=0.5, anchor="center"),)

    usrEntryBox.unbind("<KeyPress>", is_typing)
    usrEntryBox.unbind("<KeyRelease>", check_letter)



    root.unbind("<Escape>", restartTestDuringTest)



#=============================
# Words Per Minute Calculation
#=============================
def gross_WPM(word_count, timeTaken):

    global wordsPerMinute

    wordsPerMinute = round(((word_count / timeTaken) * 100))



#===========================
# Text Accurarcy Calculation
#===========================
def textAcc(plyr_text, displayText, word_count):

    global textACC

    textACC = len(set(plyr_text.split()) & set(displayText.split()))
    textACC = round((textACC / word_count) * 100)
 


#==========================================
# Random Challenge Text Generation Function
#==========================================
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

    # Concatenates Array Elem Into String In Same Var
    displayText = "".join([str(elem) for elem in displayText])

    # Aligns text onto 1 line by removing empty whitespaces
    displayText = displayText.translate({ord(c): " " for c in string.whitespace})

    # Finds Word Length Of Text
    word_count = len(displayText.split())
    word = displayText.strip()

    for character in word:
        internalText.append(character)
    else:
        pass



#===============================
# Result Display Widget Function
#===============================
def displayResult():

    global displayTimer, iOFrame
    global wordsPerMinute, textACC
    global timeFinished
    global restartTestButton

    if displayTimer.winfo_ismapped() == True:
        displayTimer.pack_forget()


    if challengeText.winfo_ismapped() == True:
        challengeText.pack_forget()


    if usrEntryBox.winfo_ismapped() == True:
        usrEntryBox.pack_forget()


    if iOFrame.winfo_ismapped() == True:
        iOFrame.pack_forget()

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



#========================
# Main Menu Quit Function
#=======================
def titlePageQuit():

    root.destroy()



#========================
# Main Menu Play Function
#========================
def titlePagePlay():

    global titlePageFrame, titlePageAppTitle
    global titlePagePlayButton, titlePageQuitButton

    #=======================
    # Removing Title Widgets
    #=======================

    for child in titlePageFrame.winfo_children():
        if child.winfo_ismapped():

            child.pack_forget()


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

    iOFrame.pack(anchor="center", expand=False, fill="none")
    iOFrame.place_configure(relx=0.5, rely=0.5, anchor="center")

    displayTimer.pack(pady=10)

    challengeText.pack(anchor=CENTER, pady=20)
    challengeText.insert(INSERT, displayText)
    challengeText.config(state=DISABLED)

    usrEntryBox.pack(anchor=CENTER)

    children = root.winfo_children()

    
    #=========================
    # Bindings For Widgets
    #=========================
    root.bind( "<Configure>", lambda event: iOFrame.place_configure(relx=0.5, rely=0.5, anchor="center"),)

    usrEntryBox.bind("<KeyPress>", is_typing)
    usrEntryBox.bind("<KeyRelease>", check_letter)

    root.bind("<Escape>", restartTestDuringTest)





#===================
# Root Window Config
#===================
root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Typr")
root.config(bg="#1A1A1A")



#===============
# Navagation Bar
#===============
navBar = Frame(
        master=root, 
        bg=root['bg'], 
        height=100,
        width=root.winfo_screenwidth()
)



#==============================
# During Test Application Title
#==============================
smallappTitle = Label(
        master=navBar,
        text="Typr",
        font=("Rubik Bold", 50, 'italic'),
        bg=root['bg'],
        fg="#ffffff"
)



#==============================
# Master Frame For Test Widgets
#==============================
iOFrame = Frame(
    master=root, 
    bg=root["bg"], 
    width=(root.winfo_screenwidth() - 100)
)



#============================
# On-screen Timer During Test
#============================
displayTimer = Label(
    master=iOFrame,
    text="Please Begin Typing...",
    font=("Rubik ExtraBold Italic", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



#===============================
# Result Words Per Minute Widget
#===============================
displayResultWPM = Label(
    master=iOFrame,
    font=("Rubik ExtraBold", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



#==============================
# Result Player Accuracy Widget
#==============================
displayResultAcc = Label(
    master=iOFrame,
    font=("Rubik ExtraBold Italic", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



#==========================================
# Result Player Test Completion Time Widget
#==========================================
displayResultTimeTaken = Label(
    master=iOFrame,
    font=("Rubik ExtraBold Italic", 80),
    bg="#1A1A1A",
    fg="#ffffff",
)



#=============================
# Result Screen Restart Button
#=============================
restartTestButton = Button(
    master=iOFrame,
    font=("Rubik Bold", 30),
    bg="#1A1A1A",
    fg="#ffffff",
    text="RETRY",
    command=restartTestAfterTest,
)



#==================================
# Result Screen Quit-To-Menu Button
#==================================
quitTestButton = Button(
    master=iOFrame,
    font=("Rubik Bold", 30),
    bg="#1A1A1A",
    fg="#ffffff",
    text="RETURN TO MENU",
    command=returnToMenu,
)



#===================================
# Widget To Display Text To Be Typed
#===================================
challengeText = Text(
    master=iOFrame,
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



#===========================================
# Test Box For Player To Type In During Test
#===========================================
usrEntryBox = Text(
    master=iOFrame,
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



#=======================
# Main Menu Master Frame
#=======================
titlePageFrame = Frame(
        master=root,
        bg=root['bg']
)
titlePageFrame.pack()
titlePageFrame.place(relx=0.5, rely=0.5, anchor="center")



#============================
# Main Menu Application Title
#============================
titlePageAppTitle = Label(
        master=titlePageFrame,
        text="Typr",
        font=("Rubik ExtraBold", 100),
        bg=root['bg'],
        fg=("#ffffff"),
) 
titlePageAppTitle.pack(side=TOP)



#======================
# Main Menu Play Button
#======================
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



#==================================
# Main Menu Quit Application Button
#==================================
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

if __name__ == "__main__":
    root.mainloop()

