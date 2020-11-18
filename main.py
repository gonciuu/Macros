import tkinter as tk
from pynput.mouse import Button, Controller
import time
import keyboard
import mouse as control_mouse

mouse = Controller()

OptionList = [
    Button.left,
    Button.right,
]


class App:

    def __init__(self):
        self.applyInfiniteMacro()
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
                                    command=lambda: self.applyMacro(self.buttonType1, self.bindEntry1, self.cpsEntry1,
                                                                    self.timeEntry1))
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
        self.optButton2.grid(column=3, row=2, padx=20, pady=5)

        self.applyBind2 = tk.Button(master=self.window, width=10, bg='black', fg='white', text="Apply",
                                    command=lambda: self.applyMacro(self.buttonType2, self.bindEntry2, self.cpsEntry2,
                                                                    self.timeEntry2))
        self.applyBind2.config(font=("Segoe UI", 12))
        self.applyBind2.grid(column=4, row=2, padx=20, pady=5)

        self.cpsEntry3 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.cpsEntry3.config(font=("Segoe UI", 12))
        self.cpsEntry3.grid(column=0, row=3, padx=20, pady=5)

        self.timeEntry3 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.timeEntry3.config(font=("Segoe UI", 12))
        self.timeEntry3.grid(column=1, row=3, padx=20, pady=5)

        self.bindEntry3 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.bindEntry3.config(font=("Segoe UI", 12))
        self.bindEntry3.grid(column=2, row=3, padx=20, pady=5)

        self.buttonType3 = tk.StringVar(self.window)
        self.buttonType3.set(OptionList[0])

        self.optButton3 = tk.OptionMenu(self.window, self.buttonType3, *OptionList)
        self.optButton3.config(font=("Segoe UI", 12), width=10, fg='white', bg='black')
        self.optButton3.grid(column=3, row=3, padx=20, pady=5)

        self.applyBind3 = tk.Button(master=self.window, width=10, bg='black', fg='white', text="Apply",
                                    command=lambda: self.applyMacro(self.buttonType3, self.bindEntry3, self.cpsEntry3,
                                                                    self.timeEntry3))
        self.applyBind3.config(font=("Segoe UI", 12))
        self.applyBind3.grid(column=4, row=3, padx=20, pady=5)

        self.window.mainloop()

    @staticmethod
    def mouseMacro(click_count, duration, bt):
        time.sleep(1)
        for x in range(duration):
            for y in range(click_count):
                mouse.click(bt, 1)
                time.sleep(1 / click_count)

    def applyMacro(self, variable, bindEntry, cpsEntry, timeEntry):
        index = 0
        for i in OptionList:
            if str(i) == variable.get():
                index = OptionList.index(i)
        try:
            keyboard.remove_hotkey(bindEntry.get())
        except:
            print("")

        keyboard.add_hotkey(bindEntry.get(), callback=lambda: self.mouseMacro(int(cpsEntry.get()), int(timeEntry.get()),
                                                                              OptionList[index]))

    def applyInfiniteMacro(self):
        control_mouse.on_click(callback=lambda: print('xd'), args=[])
        control_mouse.on_right_click(callback=lambda: print('xd1'), args=[])
        control_mouse.on_middle_click(callback=lambda: print('xd2'), args=[])



app = App()
