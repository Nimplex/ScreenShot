import pyautogui as autogui
from tkinter import *
from tkinter import filedialog
import time

window = Tk()
window.title("ScreenShot")
window.resizable(width=False, height=False)
def makescreenshot():
    if len(inp.get()) > 0:
        filename = filedialog.askdirectory()
        if len(filename) > 0:
            window.withdraw()
            time.sleep(0.18)
            
            img = autogui.screenshot()
            img.save(filename + "/" + inp.get() + ".png")
            
            window.update()
            window.deiconify()

txt = Label(window, text="Nazwa pliku")
inp = Entry(window, width=50)
btn = Button(window, text="Zrób screena", command=makescreenshot)

txt.grid()
inp.grid()
btn.grid()

txt = Label(window, text="")
txt.grid()

window.mainloop()
