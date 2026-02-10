import pyautogui
import time
import tkinter as gui

def screenshot():
    name = 'ScreenSHOT'
    name = name+ str(time.time())+".jpg"
    loc = f'D:/Programs/PYTHON/{name}'
    time.sleep(1)
    img = pyautogui.screenshot()
    img.save(loc)
    img.show()

root = gui.Tk()
frame = gui. Frame(root)
frame.pack ()
button = gui. Button (frame, text= "Take ScreenShot", command=screenshot)
button.pack(side=gui. LEFT)
close = gui.Button(frame,text="Exit",command=quit)
close.pack(side=gui.RIGHT)

root.mainloop()