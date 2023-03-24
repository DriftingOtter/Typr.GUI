
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
timerCount = int() # (Default State: int() )
internalTXTcounter = 0 # (Default State: 0)
keys_pressed = 0 # (Default State: 0)
timr_state = False # (Default State: False)
running = False # (Default State: False)
usr_error_Count = 0 # (Default State: 0)

def countdown(timercount):

    global usrEntryBox, timerCount

    # change text in label        
    displayTimer['text'] = timerCount

    if timerCount > 0:

        earlyFinishCheck()

        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, timerCount-1)

    if timerCount == 0:
        usrEntryBox.config(state=DISABLED)
        gross_WPM()
        netWordsPerMinute()
 
def is_typing(event):

    global time_Limit, timr_state

    # check if the user is typing in the Text widget
    if event.widget == usrEntryBox and timr_state == False:
        
        countdown(time_Limit)
        timr_state = True

def check_letter(event):

    global internalText, usrEntryBox, internalTXTcounter, running, usr_error_Count

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

    global internalText, usrEntryBox, internalTXTcounter 
    global displayText, timerCount

    while timercount > 0:
    
        last_letter = usrEntryBox.get('end-2c', 'end-1c')

        if event.sym == "Return" and last_letter.strip() == displayText[-1]:

            timerCount = 0

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

def results_Popup():

    # Create the toplevel window
    top_level = Toplevel(master=root)
    top_level.geometry("500x1000")
    top_level.config(bg="#1a1a1a")
    top_level.title("Results")

    # Remove the status bar
    top_level.overrideredirect(True)

    # Create the title label
    title_label = Label(
        master= top_level, 
        text="RESULTS", 
        font=("Rubik Bold",50), 
        bg="#1a1a1a", 
        fg="white", 
        anchor="center"
    )
    title_label.pack(anchor="center")

    # Set the value for the grossWPM variable
    grossWPM = 150

    # Create the grossWPM label
    wpm_label = Label(
        master=top_level, 
        text=f"Gross WPM: {grossWPM}", 
        font=("Rubik",15), 
        bg="#1a1a1a", 
        fg="white", 
        anchor="center"
    )
    wpm_label.pack(anchor="center", pady=10)

    # Set the value for the netWPM variable
    netWPM = 140

    # Create the netWPM label
    net_wpm_label = Label(
        master=top_level, 
        text=f"Net WPM: {netWPM}", 
        font=("Rubik",15), 
        bg="#1a1a1a", 
        fg="white", 
        anchor="center"
    )
    net_wpm_label.pack(anchor="center")

    

#------------------------------------------------------------------------------------------

# Holds Word List Location
worldList = "/home/otter/Documents/Typr/WordLists/Loki_Word_List_EN.txt"

with open(worldList, "r") as currenText:
    # Reads The Line Number From Text
    lines = currenText.readlines()

# Pre-declears the variabe before generation
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
