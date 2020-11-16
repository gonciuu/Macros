import tkinter as tk
from pynput.mouse import Button, Controller
import time
import keyboard

mouse = Controller()


class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg='black')
        self.window.title("Macro")
        self.window.geometry("1000x580")

        self.macroButton = tk.Button(master=self.window, text="15 cps macro (10 sec) [v] - pvp", command=lambda: self.mouseMacro(15, 10, Button.left))
        self.macroButton.config(font=("Segoe UI", 18))
        self.macroButton.grid(column=0, row=0)

        self.macroButton2 = tk.Button(master=self.window, text="20 cps macro (10 sec) [b] - pvp", command=lambda: self.mouseMacro(20, 10, Button.left))
        self.macroButton2.config(font=("Segoe UI", 18))
        self.macroButton2.grid(column=0, row=1)

        self.macroButton3 = tk.Button(master=self.window, text="30 cps macro (10 sec) [alt+b] - pvp", command=lambda: self.mouseMacro(30, 10, Button.left))
        self.macroButton3.config(font=("Segoe UI", 18))
        self.macroButton3.grid(column=0, row=2)

        keyboard.add_hotkey('v', callback=lambda: self.mouseMacro(15, 10, Button.left))
        keyboard.add_hotkey('b', callback=lambda: self.mouseMacro(20, 10, Button.left))
        keyboard.add_hotkey('alt+b', callback=lambda: self.mouseMacro(30, 10, Button.left))

        self.macroButton = tk.Button(master=self.window, text="15 cps macro (10 sec) [~] - building", command=lambda: self.mouseMacro(15, 10, Button.right))
        self.macroButton.config(font=("Segoe UI", 18))
        self.macroButton.grid(column=1, row=0)

        self.macroButton2 = tk.Button(master=self.window, text="20 cps macro (10 sec) [shift+2] - building", command=lambda: self.mouseMacro(20, 10, Button.right))
        self.macroButton2.config(font=("Segoe UI", 18))
        self.macroButton2.grid(column=1, row=1)

        self.macroButton3 = tk.Button(master=self.window, text="30 cps macro (10 sec) [shift+3] - building", command=lambda: self.mouseMacro(30, 10, Button.right))
        self.macroButton3.config(font=("Segoe UI", 18))
        self.macroButton3.grid(column=1, row=2)

        keyboard.add_hotkey('~', callback=lambda: self.mouseMacro(15, 10, Button.right))
        keyboard.add_hotkey('shift+2', callback=lambda: self.mouseMacro(20, 10, Button.right))
        keyboard.add_hotkey('shift+3', callback=lambda: self.mouseMacro(30, 10, Button.right))
        self.window.mainloop()

    def mouseMacro(self,  click_count, duration, bt):
        time.sleep(2)
        for x in range(duration):
            for y in range(click_count):
                mouse.click(bt, 1)
                time.sleep(1/click_count)


app = App()
