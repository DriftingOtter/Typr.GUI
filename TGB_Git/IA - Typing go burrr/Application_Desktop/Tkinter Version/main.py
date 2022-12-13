# ------------------------------------------------------------------------------#
# Name: Typing Go Burrr
# Version: 1.0.0
# Summary: A Minimalistic Typing Test Application
# Home-page: N/A
# Author: Daksh Kaul
# Author-email: dakshkaul7790@gmail.com
# License: N/A
# ------------------------------------------------------------------------------#


# Imports And Dependencies
from tkinter import *
import ctypes
import random
import string
import time
import threading


# Defs

time_limit_vals = [15, 30, 60, 120]
current_time_limit = time_limit_vals[0]
current_time_limit_str = "Time Limit:", str(current_time_limit)


def change_time_limit():

    global time_limit_vals, current_time_limit, current_time_limit_str

    if current_time_limit == time_limit_vals[0]:

        current_time_limit = time_limit_vals[1]

    elif current_time_limit == time_limit_vals[1]:

        current_time_limit = time_limit_vals[2]

    elif current_time_limit == time_limit_vals[2]:

        current_time_limit = time_limit_vals[3]

    else:

        current_time_limit = time_limit_vals[0]

    current_time_limit_str = "Time Limit:", str(current_time_limit)
    timer_limit_changer.config(text=current_time_limit_str)

    time_display_TEXT.config(state=ACTIVE)
    time_display_TEXT.config(text=current_time_limit_str)
    time_display_TEXT.config(state=DISABLED)


# Funtion For Clock Count Down
countdown_clock = None


def countdown(count):

    global countdown_clock

    # Puts count into a str var that has formating for display
    count_display = "Time:", str(count), "s"
    countdown_clock = count

    # Displays Text
    time_display_TEXT.config(state=ACTIVE)
    time_display_TEXT.config(text=count_display)
    time_display_TEXT.config(state=DISABLED)

    if count > 0:
        # call countdown again after 1000ms (1s)
        app.after(1000, countdown, count - 1)

        countdown_clock = count

    else:

        check_timer_script()


# Script To Start Timer And Timer Checking Script
def start_timer(event):

    countdown(current_time_limit)

    text_entry_TEXT.unbind("<Key>")

    do_start()


# Script To Check If The Timer Is Up
def check_timer_script():

    global countdown_clock, text_entry_TEXT

    if countdown_clock == 0:

        # Stops User From Typing
        text_entry_TEXT.config(state=DISABLED)

        ans_checking_script()

        return

    else:

        pass


# calculate words per minute and accuracy
def calculate_wpm_and_accuracy(time_taken, num_words):
  # calculate words per minute
  wpm = num_words / (time_taken / 60)
  
  # calculate accuracy
  accuracy = num_words / (time_taken / 60)
  
  # return the results
  return wpm, accuracy


# Script To Check Users Answers
def ans_checking_script():

    user_entered_text = text_entry_TEXT.get(1.0, END)

    # Checks If User Input Is Same As Printed Text
    if user_entered_text.strip() == displayTextSTR.strip():
        
        #Closes Main File Before Use
        currenText.close()

        user_words_typed = len((user_entered_text.split()))

        wpm, acc = calculate_wpm_and_accuracy(current_time_limit,user_words_typed)

        # print the results
        print("Words per minute:", wpm)
        print("Accuracy:", acc)

        pass

    else:

        #Closes Main File Before Use
        currenText.close()

        user_words_typed = len((user_entered_text.split()))

        wpm, acc = calculate_wpm_and_accuracy(current_time_limit,user_words_typed)

        # print the results
        print("Words per minute:", wpm)
        print("Accuracy:", acc)

        pass


# Script To Thread Process into multiple CPU cores
def do_start():
    worker = threading.Thread(target=check_timer_script)
    worker.start()


# Tkinter Boiler Plate
app = Tk()

# Captures The Users Screen Width And Height
widthSCREEN = app.winfo_screenwidth()
heightSCREEN = app.winfo_screenheight()

# Gives Dimenstions to Window
app.geometry("%dx%d" % (widthSCREEN, heightSCREEN))

# Gives Title To Window
app.title("Typing Go Burrr")

# Give Window A Specific Color
app.config(background="#222831")

# Allows Application To Render Based Upon Users Display DPI
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Gives Application An Icon
appIcon = PhotoImage(
    file="C:/Users/daksh/OneDrive/Desktop/Typing go burrr/IA - Typing go burrr/Application_Desktop/Tkinter Version/TGB_Icon.png"
)
app.iconphoto(True, appIcon)


# Frame for the title of the app
titleFrame = Frame(
    master=app,
    bg="#222831",
    relief=FLAT,
    borderwidth=0,
    width=widthSCREEN,
    height=50,
)
# Adds Frame Into Main Loop
titleFrame.pack(anchor=NW, side=TOP, fill=X)


# First Section Of The Title | 'typing'
titleLabel1 = Label(
    master=titleFrame,
    text="Typing ",
    font=("Arial", 50, "bold", "italic"),
    bg="#222831",
    foreground="#EEEEEE",
)
# Adds Label Into Main Loop
titleLabel1.pack(side=LEFT, padx=10, pady=10)


# Second Section Of The Title | 'Go'
titleLabel2 = Label(
    master=titleFrame,
    text="Go ",
    font=("Arial", 50, "bold", "italic"),
    bg="#222831",
    foreground="#7971EA",
)
# Adds Label Into Main Loop
titleLabel2.pack(side=LEFT, pady=10)


# Third Section Of The Title | 'Burrr'
titleLabel3 = Label(
    master=titleFrame,
    text="Burrr",
    font=("Arial", 50, "bold", "italic"),
    bg="#222831",
    foreground="#EEEEEE",
)
# Adds Label Into Main Loop
titleLabel3.pack(side=LEFT, pady=10)


# Adds Button To Change Time Limit On Test
timer_limit_changer = Button(
    master=titleFrame,
    text=current_time_limit_str,
    command=change_time_limit,
    width=15,
    height=1,
    font=("Arial", 20, "bold", "italic"),
    fg="#EEEEEE",
    bg="#222831",
    relief=FLAT,
    borderwidth=0,
    activebackground="#222831",
    activeforeground="#7971EA",
)
# Adds Button Into Main Loop
timer_limit_changer.pack(anchor=E, side=RIGHT)


# Adds Frame For User And Application Display
text_display_Frame = Frame(master=app, width=1000, height=200, bg="#222831")
# Adds Frame Into Main Loop
text_display_Frame.pack(anchor=CENTER, pady=heightSCREEN / 3)

# Adds Live Timer For Countdown
time_display_TEXT = Label(
    master=text_display_Frame,
    width=15,
    height=1,
    font=("Arial", 40, "bold", "italic"),
    fg="#7971EA",
    bg="#222831",
    relief=FLAT,
    borderwidth=0,
    disabledforeground="#7971EA",
)
# Adds Text Box Into Main Loop
time_display_TEXT.pack(anchor=W, pady=50)

# Forces Text To Be On Left Hand Side
time_display_TEXT.config(justify="left")

# Filler Text For Time Display
time_display_TEXT.config(text=current_time_limit_str)

# Makes The Text Box Read-Only
time_display_TEXT.config(state=DISABLED)


# Makes Text Box That The Application Can Display Text In During The Test
text_display_TEXT = Text(
    master=text_display_Frame,
    width=100,
    height=3,
    wrap=WORD,
    font=("Arial", 20, "bold"),
    fg="#EEEEEE",
    bg="#222831",
    relief=FLAT,
    borderwidth=0,
    takefocus=0,
)
# Adds The Text Box Into Main Loop
text_display_TEXT.pack()


text_display_TEXT.config(state=DISABLED)


# ---------------------------------------------------------------------------------------------------------------

# Test Dependent Variables

# Holds Word List Location
worldList = "C:/Users/daksh/OneDrive/Desktop/Typing go burrr/IA - Typing go burrr/Word List/Master_EN_Word_List.txt"

# Reads Word List Into A Variable
currenText = open(worldList, "r")

# Reads The Line Number From Text
lines = currenText.readlines()

# Pre-delclears the variabe before generation
displayText = []

# makes loop for adding words into the displayText VAR
for i in range(0, 50):
    if i != 10:
        randomLineGen = random.randint(0, 2000)
        displayText.append(lines[randomLineGen])
    else:
        break

# Removes  default array boiler plate
displayText = "".join([str(elem) for elem in displayText])

# Stores display data into a string only var
displayTextSTR = displayText.translate({ord(c): " " for c in string.whitespace})

# Displays Text without white spaces
text_display_TEXT.config(state=NORMAL)
text_display_TEXT.insert(1.0, displayTextSTR)
text_display_TEXT.config(state=DISABLED)


# Finds Word Length Of Text
word_count = len(displayTextSTR.split())


# --------------------------------------------------------------------------------------------------------------


# User Entry Box
text_entry_TEXT = Text(
    master=text_display_Frame,
    width=100,
    height=3,
    wrap=WORD,
    font=("Arial", 20, "bold"),
    fg="#EEEEEE",
    bg="#222831",
    relief=FLAT,
    borderwidth=0,
    insertunfocussed=SOLID,
    insertbackground="#7971EA",
    insertwidth=5,
    insertofftime=0,
    insertborderwidth=0,
)
# Adds Box Into Main Loop
text_entry_TEXT.pack()

# Binds Entry Box To Have Fuction To Start Test
text_entry_TEXT.bind("<Key>", start_timer)


# Frame For Buttons On The Bottom
bottom_Frame = Frame(
    master=app,
    background="#222831",
    width=widthSCREEN,
    height=100,
    borderwidth=0,
    relief=FLAT,
)
# Adds Frame Into Main Loop
bottom_Frame.pack(side=BOTTOM, fill=X)


# Allows The Application To Be Run If The File Has Property Of '__main__'
if __name__ == "__main__":
    app.mainloop()
