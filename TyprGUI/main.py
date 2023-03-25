
#  $$$$$$\    $$\               
# $$  __$$\   $$ |              
# $$ /  $$ |$$$$$$\    $$$$$$\  
# $$ |  $$ |\_$$  _|  $$  __$$\ 
# $$ |  $$ |  $$ |    $$ |  \__|
# $$ |  $$ |  $$ |$$\ $$ |      
#  $$$$$$  |  \$$$$  |$$ |      
#  \______/    \____/ \__|      
#
# Computer Science HL IA 
#
# <3

# Imports
from tkinter import *
import random
import string

# Variable States For Program
time_Limit = 10 # (Default State: 10)
internalTXTcounter = 0 # (Default State: 0)
keys_pressed = 0 # (Default State: 0)
timr_state = False # (Default State: False)
running = False # (Default State: False)
usr_error_Count = 0 # (Default State: 0)
numOfWords = 5 # (Default State: int() )
displayText = []
internalText = []
word_count = int()
wordList = "/home/otter/Documents/Typr/WordLists/Loki_Word_List_EN.txt"

def countdown():

    global usrEntryBox, time_Limit

    # change text in label        
    displayTimer['text'] = time_Limit

    if time_Limit > 0:

        if time_Limit > 0:
            earlyFinishCheck()
        else:
            pass

        if time_Limit > 0:
            time_Limit = time_Limit - 1

        #TODO:Change Sleep Interval Based On Func Time Taken (AT END OF PROJECT)
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown)

    if time_Limit == 0:
        usrEntryBox.config(state=DISABLED)
        #gross_WPM()
        #netWordsPerMinute()
 
def is_typing(event):

    global time_Limit, timr_state

    # check if the user is typing in the Text widget
    if event.widget == usrEntryBox and timr_state == False:
        
        countdown()
        timr_state = True

def check_letter(event):

    global internalText, usrEntryBox, internalTXTcounter 
    global running, usr_error_Count

    if running:
        return

    running = True

    usrEntryBox.unbind("<KeyRelease>", check_letter)

    last_letter = usrEntryBox.get("end-2c", "end-1c")

    usrEntryBox.tag_config("ErrorColor", background="red")

    if event.keysym == "BackSpace":
        if internalTXTcounter > 0:
            internalTXTcounter -= 1
            usrEntryBox.tag_remove("ErrorColor", "end-2c", "end-1c")

            if usr_error_Count >= 0:
                usr_error_Count -= 1
    else:
        if last_letter != internalText[internalTXTcounter]:
            internalTXTcounter += 1
            usrEntryBox.tag_add("ErrorColor", "end-2c", "end-1c")
            usr_error_Count += 1
        else:
            internalTXTcounter += 1
            usrEntryBox.tag_remove("ErrorColor", "end-2c", "end-1c")

    usrEntryBox.bind("<KeyRelease>", check_letter)
    running = False

def earlyFinishCheck():

    global usrEntryBox, displayText, timr_state, time_Limit

    if timr_state == True:

        last_letter = usrEntryBox.get("end-2c", "end-1c")
        usrTextLength = len(usrEntryBox.get("1.0", "end"))

        # TODO: fix function 
        if usrTextLength == len(displayText):

            if last_letter.strip() == (displayText[-2:]).strip():
                usrEntryBox.config(state=DISABLED)
                time_Limit = 0

def key_press_counter(event):

    global keys_pressed, usrEntryBox

    last_char = usrEntryBox.get("end-2c", "end-1c")

    if last_char and last_char.isalpha():

        keys_pressed += 1

def gross_WPM():

    global time_Limit, word_count, usrEntryBox, keys_pressed

    grossWPM = round(((keys_pressed / 5) / (time_Limit/60)))

    print("Gross Words Per Minute:", grossWPM)

    return grossWPM

def netWordsPerMinute():

    global time_Limit, word_count, usrEntryBox, keys_pressed, usr_error_Count

    grossWPM = round(((keys_pressed / 5) / (time_Limit/60)))

    error_Rate = usr_error_Count / (time_Limit/60)

    netWPM = round(grossWPM - error_Rate)

    print("Net Words Per Minute:",netWPM)

    return netWPM

def generateChallengeText():
    
    global wordList, displayText, internalText, word_count, usrEntryBox
    
    with open(wordList, "r") as currenText:
        # Reads The Line Number From Text
        lines = currenText.readlines()

    # makes loop for adding words into the displayText VAR
    for z in range(0, numOfWords):
        if z != numOfWords:
            randomLineGen = random.randint(0, 977)# the number of words in the word list
            displayText.append(lines[randomLineGen])
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

generateChallengeText()

root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Typr")
root.config(bg="#1A1A1A")

gameInputAndOutputFrame = Frame(master=root, bg=root['bg'], width=root.winfo_screenwidth()-100)
gameInputAndOutputFrame.pack(anchor="center", expand=False, fill='none')
gameInputAndOutputFrame.place_configure(relx=.5, rely=.5, anchor="center")

displayTimer =  Label(
    master=gameInputAndOutputFrame,
    text="Please Begin Typing...",
    font=('Rubik ExtraBold Italic', 80), 
    bg="#1A1A1A", 
    fg="#ffffff"
)
displayTimer.pack(pady=10)

challengeText = Text(
    master=gameInputAndOutputFrame,  
    font=('Rubik', 40),
    width=50,
    height=1, 
    bg=root['bg'], 
    fg="#ffffff",
    wrap=WORD,
    relief=FLAT,
    takefocus=0
)
challengeText.pack(anchor=CENTER, pady=20)
challengeText.insert(INSERT, displayText)
challengeText.config(state=DISABLED)

usrEntryBox = Text(
    master=gameInputAndOutputFrame, 
    font=('Rubik', 40), 
    width=challengeText['width'],
    height=1, 
    bg=root['bg'], 
    fg="#ffffff", 
    relief=FLAT,
    takefocus=0,
    insertbackground="#ffffff", 
    insertofftime=0, 
    insertwidth=5
)
usrEntryBox.pack(anchor=CENTER)

# Bindings For Application

root.bind("<Configure>", lambda event: gameInputAndOutputFrame.place_configure(relx=.5, rely=.5, anchor="center"))

usrEntryBox.bind("<KeyPress>", is_typing)
usrEntryBox.bind("<KeyRelease>", check_letter)
usrEntryBox.bind("<KeyRelease>", key_press_counter)


if __name__ == "__main__":
    root.mainloop()
