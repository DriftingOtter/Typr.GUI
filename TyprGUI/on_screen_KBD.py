from tkinter import *
import ctypes

root = Tk()
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
root.title("On Screen Keyboard - Typr")
root.config(bg="#1A1A1A")
ctypes.windll.shcore.SetProcessDpiAwareness(True)

def refactorSpecialChar(text):

    global specialChar_mapping

    # Look up the corresponding character in the char_mapping dictionary
    # If the text is not in the mapping, use the original text
    return specialChar_mapping.get(text, text)

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

# Makes frame that acts as a 'case' for the key to be displayed in
keyboardCase = Frame(
    master=root, 
    borderwidth=40, 
    bg="#050505", 
    height=125, 
    width=250, 
    relief=GROOVE
)
# keyboardCase.pack()

# indivisual rows for key to be placed in
key_row1 = Frame(
    master=keyboardCase,
    width=125,
    takefocus=0
)
key_row1.pack(side=TOP)

key_row2 = Frame(
    master=keyboardCase,
    width=125,
    takefocus=0
)
key_row2.pack(anchor=CENTER)

key_row3 = Frame(
    master=keyboardCase,
    width=125,
    takefocus=0
)
key_row3.pack(anchor=CENTER)

key_row4 = Frame(
    master=keyboardCase,
    width=125,
    takefocus=0
)
key_row4.pack(anchor=CENTER)

key_row5 = Frame(
    master=keyboardCase,
    width=125,
    takefocus=0
)
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
            takefocus=0
        )
        btn.pack(side="left")

# Binding For Applications
root.bind("<Key>", key_press)
root.bind("<KeyRelease>", key_release)

root.mainloop()