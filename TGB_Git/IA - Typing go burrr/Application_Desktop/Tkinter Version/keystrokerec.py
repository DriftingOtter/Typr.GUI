#Key press prototype
#Tracks keys as pressed, ignoring the keyboard repeater
#Current keys down are kept in a dictionary.
#That a key is pressed is flagged, and the last key pressed is tracked

import tkinter

winWid = 640
winHei = 480
keyDown = False
lastKey = "none"
keyChange = keyDown
keyList = {}

def onKeyDown(event):
    global keyDown, lastKey, keyList
    if (event.char in keyList) != True:
        keyList[event.char] = "down"
        print(keyList)
    keyDown = True
    lastKey = event.char

def onKeyUp(event):
    global keyDown
    if (event.char in keyList) == True:
        keyList.pop(event.char)
    if len(keyList) == 0:
        keyDown = False
    print(keyList)
    
#onTimer is present to show keyboard action as it happens. 
#It is not needed to track the key changes, and it can be 
#removed.
def onTimer(): 
    global keyChange, timerhandle
    if keyDown != keyChange:
        keyChange = keyDown
        if keyDown:
            print("Key down, last key pressed - " + lastKey)
        else:
            print("Key up, last key pressed - " + lastKey)
    timerhandle = window.after(20,onTimer)
    
def onShutdown():
    window.after_cancel(timerhandle)
    window.destroy()    

window = tkinter.Tk()
frame = tkinter.Canvas(window, width=winWid, height=winHei, bg="black")
frame.pack()

frame.bind("<KeyPress>", onKeyDown)
frame.bind("<KeyRelease>", onKeyUp)
frame.focus_set()

timerhandle = window.after(20,onTimer)
window.protocol("WM_DELETE_WINDOW",onShutdown)
window.mainloop()