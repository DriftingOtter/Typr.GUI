from tkinter import *
import ctypes
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

def countdown(timercount):

    # change text in label        
    displayTimer['text'] = timercount

    if timercount > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, timercount-1)

# count down 'FLAG' vaiable
countdown_started = False

def is_typing(event):

    global countdown_started

    # check if the user is typing in the Text widget
    if event.widget == usrEntryBox:
        
        if not countdown_started:
            startcountdown()
            countdown_started = True
    
    else: 

        pass    

def startcountdown():

    countdown(10)


internalTXTcounter = 0
def check_letter(event):

    global internalText, usrEntryBox, internalTXTcounter

    last_letter = usrEntryBox.get("end-2c", "end-1c")

    usrEntryBox.tag_config("ErrorColor", background='red')

    if event.keysym == "BackSpace":
        if internalTXTcounter > 0:
            internalTXTcounter -= 1
            usrEntryBox.tag_remove("ErrorColor", "end-2c", "end-1c")
    else:
        if last_letter != internalText[internalTXTcounter]:
            usrEntryBox.tag_add("ErrorColor", "end-2c", "end-1c")
        else:
            internalTXTcounter += 1
            usrEntryBox.tag_remove("ErrorColor", "end-2c", "end-1c")


#------------------------------------------------------------------------------------------

# Holds Word List Location
worldList = "C:/Users/daksh/OneDrive/Desktop/Typr/WordLists/Loki_Word_List_EN.txt"

with open(worldList, "r") as currenText:
    # Reads The Line Number From Text
    lines = currenText.readlines()


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

# Pre-delclears the variabe before generation
internalText = []
word = displayText.strip()

for character in word:
    internalText.append(character)
else:
    pass

#----------------------------------------------------------------------------------------------

root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Typr")
root.config(bg="#1A1A1A")
ctypes.windll.shcore.SetProcessDpiAwareness(True)

gameInputAndOutputFrame = Frame(master=root, bg=root['bg'], width=root.winfo_screenwidth()-100)
gameInputAndOutputFrame.pack(anchor="center", expand=False, fill=None)

displayTimer =  Label(
    master=gameInputAndOutputFrame,
    text="0s",
    font=('Rubik ExtraBold Italic', 30), 
    bg="#1A1A1A", 
    fg="#ffffff"
)
displayTimer.pack(pady=10)

challengeText = Text(
    master=gameInputAndOutputFrame,  
    font=('Rubik Bold', 40),
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
    font=('Rubik Bold', 40), 
    width=50,
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

if __name__ == "__main__":
    root.mainloop()
