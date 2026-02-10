import pyautogui
import time
import tkinter as gui

def screenshot():
    name = input("You will have 5 seconds to bring the desired interface on screen after typing \n Enter the name to save with \t")
    name = name+ (str)time.time()+".jpg"
    loc = f'D:/Programs/PYTHON/{name}'
    time.sleep(5)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

root = gui.Tk()
frame = gui. Frame(root)
frame.pack ()
button = gui. Button (frame, text= "Take ScreenShot", command=screenshot)
button.pack(side=gui. LEFT)