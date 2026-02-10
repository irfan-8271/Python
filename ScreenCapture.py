import pyautogui
import time

def screenshot():
    name = input("You will have 5 seconds to bring the desired interface on screen after typing \n Enter the name to save with \t")
    name = name+ (str)time.time()+".jpg"
    loc = f'D:/Programs/PYTHON/{name}'
    time.sleep(5)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()

screenshot()