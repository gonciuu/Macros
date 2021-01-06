import tkinter as tk
from pynput.mouse import Button, Controller
import time
import keyboard
import mouse as control_mouse
import threading
import json

mouse = Controller()

OptionList = [
    Button.left,
    Button.right,
]


class App:

    def __init__(self):

        self.isInfiniteMacroEnable = 1
        self.setClicks()

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
                                                                    self.timeEntry1, 0))
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
                                                                    self.timeEntry2, 1))
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
                                                                    self.timeEntry3, 2))
        self.applyBind3.config(font=("Segoe UI", 12))
        self.applyBind3.grid(column=4, row=3, padx=20, pady=5)

        self.title = tk.Label(master=self.window, text="INFINITE MACRO", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=1, row=5, padx=20, pady=(20, 0))

        self.title = tk.Label(master=self.window, text="CPS", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=1, row=6, padx=20, pady=10)

        self.infiniteCpsEntry1 = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.infiniteCpsEntry1.config(font=("Segoe UI", 12))
        self.infiniteCpsEntry1.grid(column=1, row=7, padx=20, pady=5)
        self.applyInfiniteMacroButton = tk.Button(master=self.window, width=10, bg='black', fg='white', text="Apply",
                                                  command=lambda: self.applyInfiniteMacro())
        self.applyInfiniteMacroButton.config(font=("Segoe UI", 12))
        self.applyInfiniteMacroButton.grid(column=1, row=8, padx=20, pady=5)

        self.title = tk.Label(master=self.window, text="NINJA BRIDGE", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=3, row=5, padx=20, pady=(20, 0))

        self.title = tk.Label(master=self.window, text="BIND", bg='black', fg='white')
        self.title.config(font=("Segoe UI", 15))
        self.title.grid(column=3, row=6, padx=20, pady=(10, 0))

        self.ninjaBridgeEntry = tk.Entry(master=self.window, width=10, bg='black', fg='white')
        self.ninjaBridgeEntry.config(font=("Segoe UI", 12))
        self.ninjaBridgeEntry.grid(column=3, row=7, padx=20, pady=5)

        self.applyNinjaBridgeButton = tk.Button(master=self.window, width=10, bg='black', fg='white', text="Apply",
                                                command=self.applyNinjaBridge)
        self.applyNinjaBridgeButton.config(font=("Segoe UI", 12))
        self.applyNinjaBridgeButton.grid(column=3, row=8, padx=20, pady=5)

        self.readJSONData()
        self.window.mainloop()

    @staticmethod
    def mouseMacro(click_count, duration, bt):
        time.sleep(1)
        for x in range(duration):
            for y in range(click_count):
                mouse.click(bt, 1)
                time.sleep(1 / click_count)

    def applyMacro(self, variable, bindEntry, cpsEntry, timeEntry, nb):
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
        self.updateJSONData(nb, int(cpsEntry.get()), int(timeEntry.get()), bindEntry.get(), OptionList[index])

    def setClicks(self):
        control_mouse.on_middle_click(callback=lambda: self.startInfiniteMacroClicks(), args=())
        control_mouse.on_right_click(callback=lambda: self.stopInfiniteMacro(), args=())

    def startInfiniteMacroClicks(self):
        self.isInfiniteMacroEnable = 1
        self.startInfiniteMacro(int(self.infiniteCpsEntry1.get()))

    def startInfiniteMacro(self, cps):
        if self.isInfiniteMacroEnable == 1:
            control_mouse.click('left')
            threading.Timer(1 / cps, lambda: self.startInfiniteMacro(cps)).start()

    def stopInfiniteMacro(self):
        self.isInfiniteMacroEnable = 0

    def updateJSONData(self, index, cps, duration, bind, mouseButton):
        try:
            with open('macros.txt') as json_file:
                data = json.load(json_file)
        except:
            data = self.setInitialValues()

        data['bindMacros'][index] = {
            'cps': cps,
            'time': duration,
            'bind': bind,
            'buttonType': str(mouseButton)
        }
        with open('macros.txt', 'w') as outfile:
            json.dump(data, outfile)

    def readJSONData(self):
        cpsInputs = [self.cpsEntry1, self.cpsEntry2, self.cpsEntry3]
        timeInputs = [self.timeEntry1, self.timeEntry2, self.timeEntry3]
        bindInputs = [self.bindEntry1, self.bindEntry2, self.bindEntry3]
        mouseButtons = [self.buttonType1, self.buttonType2, self.buttonType3]

        try:
            with open('macros.txt') as json_file:
                data = json.load(json_file)
                macros = data['bindMacros']
                for x in range(0, len(macros)):
                    try:
                        cpsInputs[x].insert(0, macros[x]['cps'])
                        timeInputs[x].insert(0, macros[x]['time'])
                        bindInputs[x].insert(0, macros[x]['bind'])
                        if macros[x]['buttonType'] == 'Button.left':
                            mouseButtons[x].set(OptionList[0])
                        else:
                            mouseButtons[x].set(OptionList[1])

                    except:
                        cpsInputs[x].insert(0, "")
                        timeInputs[x].insert(0, "")
                        bindInputs[x].insert(0, "")

            self.applyMacro(self.buttonType1, self.bindEntry1, self.cpsEntry1,
                            self.timeEntry1, 0)
            self.applyMacro(self.buttonType2, self.bindEntry2, self.cpsEntry2,
                            self.timeEntry2, 1)
            self.applyMacro(self.buttonType3, self.bindEntry3, self.cpsEntry3,
                            self.timeEntry3, 2)
            self.infiniteCpsEntry1.insert(0, data['infiniteMacroCPS'])
        except:
            data = self.setInitialValues()
            with open('macros.txt', 'w') as outfile:
                json.dump(data, outfile)
            self.readJSONData()

    @staticmethod
    def setInitialValues():
        return {'bindMacros': [{
            'cps': 30,
            'time': 10,
            'bind': "ctrl+c",
            'buttonType': "Button.left"
        }, {
            'cps': 30,
            'time': 10,
            'bind': "v",
            'buttonType': "Button.right"
        }, {
            'cps': 30,
            'time': 10,
            'bind': "n",
            'buttonType': "Button.left"
        }], 'infiniteMacroCPS': 20}

    def applyInfiniteMacro(self):
        try:
            with open('macros.txt') as json_file:
                data = json.load(json_file)
        except:
            data = self.setInitialValues()

        data['infiniteMacroCPS'] = int(self.infiniteCpsEntry1.get())

        with open('macros.txt', 'w') as outfile:
            json.dump(data, outfile)

    def applyNinjaBridge(self):
        keyboard.add_hotkey(self.ninjaBridgeEntry.get(), callback=lambda: self.ninjaBridge())

    def ninjaBridge(self):
        keyboard.press('s')
        for i in range(1, 20):
            keyboard.press('shift')
            #mouse.click(Button.right, 1)
            time.sleep(0.30)
            keyboard.release('shift')
            time.sleep(0.165)
        keyboard.release('s')


app = App()
