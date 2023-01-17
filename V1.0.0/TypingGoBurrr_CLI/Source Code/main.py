from tkinter import *
import ctypes
import random
import string
import time

def refactorSpecialChar(text):

    global specialChar_mapping

    # Look up the corresponding character in the char_mapping dictionary
    # If the text is not in the mapping, use the original text
    return specialChar_mapping.get(text, text)


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


def key_press(event):

    for row in (key_row1, key_row2, key_row3, key_row4, key_row5):
        for btn in row.winfo_children():
            if isinstance(btn, Button):
                if (str(btn["text"]).strip() in (event.char, event.keysym)) or (
                    str(btn["text"]).lower().strip() in (event.char, event.keysym)
                ):
                    btn["relief"] = "sunken"


def key_release(event):
    for row in (key_row1, key_row2, key_row3, key_row4, key_row5):
        for btn in row.winfo_children():
            if isinstance(btn, Button):
                if (str(btn["text"]).strip() in (event.char, event.keysym)) or (
                    str(btn["text"]).lower().strip() in (event.char, event.keysym)
                ):
                    btn["relief"] = "raised"


# ------------------------------------------------------------------------------------------

# Holds Word List Location
worldList = "V1.0.0/TypingGoBurrr_CLI/Source Code/Loki_Word_List_EN.txt"

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

# ----------------------------------------------------------------------------------------------

root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("Typing Go Burrr")
root.config(bg="#1A1A1A")
ctypes.windll.shcore.SetProcessDpiAwareness(True)


title = Label(
    master=root,
    text="Typing Go Burrr",
    font=("Rubik ExtraBold Italic", 50),
    bg="#1A1A1A",
    fg="#ffffff",
)
title.pack(anchor=W, side=TOP)

gameInputAndOutputFrame = Frame(master=root, bg=root["bg"])
gameInputAndOutputFrame.pack(anchor="center")

challengeText = Label(
    master=gameInputAndOutputFrame,
    text=displayText,
    font=("Rubik Bold", 40),
    bg="#1A1A1A",
    fg="#ffffff",
    width=root.winfo_screenwidth() - 100,
)
challengeText.pack(anchor=CENTER)

usrEntryBox = Text(
    master=gameInputAndOutputFrame,
    font=("Rubik Bold", 40),
    width=50,
    height=1,
    bg="#1A1A1A",
    fg="#A0C3D2",
    relief=FLAT,
)
usrEntryBox.pack(anchor=CENTER)
usrEntryBox.config(insertbackground="#ffffff", insertofftime=0, insertwidth=5)

# TODO:- make special character default to there original non-special value for check

# Makes frame that acts as a 'case' for the key to be displayed in
keyboardCase = Frame(
    master=root, borderwidth=40, bg="#050505", height=125, width=250, relief=GROOVE
)
# keyboardCase.pack()

# indivisual rows for key to be placed in
key_row1 = Frame(master=keyboardCase, width=125, takefocus=0)
key_row1.pack(side=TOP)

key_row2 = Frame(master=keyboardCase, width=125, takefocus=0)
key_row2.pack(anchor=CENTER)

key_row3 = Frame(master=keyboardCase, width=125, takefocus=0)
key_row3.pack(anchor=CENTER)

key_row4 = Frame(master=keyboardCase, width=125, takefocus=0)
key_row4.pack(anchor=CENTER)

key_row5 = Frame(master=keyboardCase, width=125, takefocus=0)
key_row5.pack(side=BOTTOM)


# Create a list of keys to display on the keyboard
keys_row1 = [
    "    `    ",
    "    1    ",
    "    2    ",
    "    3    ",
    "    4    ",
    "    5    ",
    "    6    ",
    "    7    ",
    "    8    ",
    "    9    ",
    "    0    ",
    "    -    ",
    "    =    ",
    "             BackSpace               ",
]

keys_row2 = [
    "                        Tab                     ",
    "    Q    ",
    "    W    ",
    "    E    ",
    "    R    ",
    "    T    ",
    "    Y    ",
    "    U    ",
    "    I    ",
    "    O    ",
    "    P    ",
    "    [    ",
    "    ]    ",
    "   \\    ",
]

keys_row3 = [
    "       Caps_Lock       ",
    "    A    ",
    "    S    ",
    "    D    ",
    "    F    ",
    "    G    ",
    "    H    ",
    "    J    ",
    "    K    ",
    "    L    ",
    "    ;    ",
    '    "    ',
    "                Return              ",
]

keys_row4 = [
    "                    Shift_L                  ",
    "    Z    ",
    "    X    ",
    "    C    ",
    "    V    ",
    "    B    ",
    "    N    ",
    "    M    ",
    "    ,    ",
    "    .    ",
    "    /    ",
    "                  Shift_R                 ",
]

keys_row5 = [
    "   Control_L   ",
    "    Win_L  ",
    "  Alt_L    ",
    "                                                         Space                                                       ",
    "  Alt_R    ",
    "Left",
    "Up",
    "Down",
    "Right",
]

rows = (keys_row1, keys_row2, keys_row3, keys_row4, keys_row5)

for i, key_row in enumerate((key_row1, key_row2, key_row3, key_row4, key_row5)):
    for key in rows[i]:
        btn = Button(
            key_row,
            text=key,
            border=10,
            relief=RAISED,
            padx=5,
            height=3,
            font=("Rubik Bold", 10),
            bg="#c4c1b9",
            takefocus=0,
        )
        btn.pack(side="left")


root.bind("<Key>", key_press)
root.bind("<KeyRelease>", key_release)
root.bind(
    "<Configure>",
    lambda event: gameInputAndOutputFrame.place_configure(
        relx=0.5, rely=0.5, anchor="center"
    ),
)
if __name__ == "__main__":
    root.mainloop()