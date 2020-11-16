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

        self.title = tk.Label(master=self.window, text="CPS", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=0, row=0, padx=20)

        self.cpsEntry1 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.cpsEntry1.config(font=("Segoe UI", 12))
        self.cpsEntry1.grid(column=0, row=1, padx=20)

        self.title = tk.Label(master=self.window, text="TIME", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=1, row=0, padx=20)

        self.timeEntry1 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.timeEntry1.config(font=("Segoe UI", 12))
        self.timeEntry1.grid(column=1, row=1, padx=20)

        self.title = tk.Label(master=self.window, text="BIND", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=2, row=0, padx=20)

        self.bindEntry1 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.bindEntry1.config(font=("Segoe UI", 12))
        self.bindEntry1.grid(column=2, row=1, padx=20)

        self.applyBind1 = tk.Button(master=self.window, width=10, bg='black', fg='white', text="Apply", command=lambda: self.applyMacro(1))
        self.applyBind1.config(font=("Segoe UI", 12))
        self.applyBind1.grid(column=3, row=1, padx=20)

        self.window.mainloop()

    @staticmethod
    def mouseMacro(click_count, duration, bt):
        time.sleep(2)
        for x in range(duration):
            for y in range(click_count):
                mouse.click(bt, 1)
                time.sleep(1 / click_count)

    def applyMacro(self, macroNumber):
        if macroNumber == 1:
            keyboard.add_hotkey(self.bindEntry1.get(), callback=lambda: self.mouseMacro(int(self.cpsEntry1.get()), int(self.timeEntry1.get()), Button.left))

app = App()
