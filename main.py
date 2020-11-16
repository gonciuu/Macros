import tkinter as tk
from pynput.mouse import Button, Controller
import time
import keyboard

mouse = Controller()

OptionList = [
    Button.left,
    Button.right,
]


class App:

    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg='black')
        self.window.title("Macro")
        self.window.geometry("1000x580")

        self.title = tk.Label(master=self.window, text="CPS", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=0, row=0, padx=20, pady=5)

        self.cpsEntry1 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.cpsEntry1.config(font=("Segoe UI", 12))
        self.cpsEntry1.grid(column=0, row=1, padx=20, pady=5)

        self.title = tk.Label(master=self.window, text="TIME", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=1, row=0, padx=20, pady=5)

        self.timeEntry1 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.timeEntry1.config(font=("Segoe UI", 12))
        self.timeEntry1.grid(column=1, row=1, padx=20, pady=5)

        self.title = tk.Label(master=self.window, text="BIND", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=2, row=0, padx=20, pady=5)

        self.bindEntry1 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.bindEntry1.config(font=("Segoe UI", 12))
        self.bindEntry1.grid(column=2, row=1, padx=20, pady=5)

        self.buttonType1 = tk.StringVar(self.window)
        self.buttonType1.set(OptionList[0])

        self.optButton1 = tk.OptionMenu(self.window, self.buttonType1, *OptionList)
        self.optButton1.config(font=("Segoe UI", 12), width=10, fg='white', bg='black')
        self.optButton1.grid(column=3, row=1, padx=20, pady=5)

        self.applyBind1 = tk.Button(master=self.window, width=10, bg='black', fg='white', text="Apply",
                                    command=lambda: self.applyMacro(1, variable=self.buttonType1))
        self.applyBind1.config(font=("Segoe UI", 12))
        self.applyBind1.grid(column=4, row=1, padx=20, pady=5)

        self.cpsEntry2 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.cpsEntry2.config(font=("Segoe UI", 12))
        self.cpsEntry2.grid(column=0, row=2, padx=20, pady=5)

        self.timeEntry2 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.timeEntry2.config(font=("Segoe UI", 12))
        self.timeEntry2.grid(column=1, row=2, padx=20, pady=5)

        self.bindEntry2 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.bindEntry2.config(font=("Segoe UI", 12))
        self.bindEntry2.grid(column=2, row=2, padx=20, pady=5)

        self.buttonType2 = tk.StringVar(self.window)
        self.buttonType2.set(OptionList[0])

        self.optButton2 = tk.OptionMenu(self.window, self.buttonType2, *OptionList)
        self.optButton2.config(font=("Segoe UI", 12), width=10, fg='white', bg='black')
        self.optButton2.grid(column=3, row=2, padx=20)

        self.applyBind2 = tk.Button(master=self.window, width=10, bg='black', fg='white', text="Apply",
                                    command=lambda: self.applyMacro(2, variable=self.buttonType2))
        self.applyBind2.config(font=("Segoe UI", 12))
        self.applyBind2.grid(column=4, row=2, padx=20, pady=5)

        self.window.mainloop()

    @staticmethod
    def mouseMacro(click_count, duration, bt):
        time.sleep(2)
        for x in range(duration):
            for y in range(click_count):
                mouse.click(bt, 1)
                time.sleep(1 / click_count)

    def applyMacro(self, macroNumber, variable):


        index = 0
        for i in OptionList:
            if str(i) == variable.get():
                index = OptionList.index(i)

        if macroNumber == 1:
            try:
                keyboard.remove_hotkey(self.bindEntry1.get())
            except:
                print("")
            keyboard.add_hotkey(self.bindEntry1.get(),
                                callback=lambda: self.mouseMacro(int(self.cpsEntry1.get()), int(self.timeEntry1.get()),
                                                                 OptionList[index]))
        elif macroNumber == 2:
            try:
                keyboard.remove_hotkey(self.bindEntry2.get())
            except:
                print("")

            keyboard.add_hotkey(self.bindEntry2.get(),
                                callback=lambda: self.mouseMacro(int(self.cpsEntry2.get()), int(self.timeEntry2.get()),
                                                                 OptionList[index]))


app = App()
