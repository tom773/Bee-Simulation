import time
import tkinter as tk
from tkinter import ttk
import Bee_Main
from Bee_Main import *

LARGE_FONT= ("Verdana", 20)
MEDIUM= ("Verdana", 16)


class SeaOfBTCApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TutorialOne, TutorialTwo, TutorialThree, TutorialFour, FirstDay, SecondLabel):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BEE SIMULATION GAME!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Press to start!", command=lambda:controller.show_frame(TutorialOne))
        button1.pack()


class TutorialOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="##############################################\n      "
               "WELCOME TO THE BEE SIMULATION!!     \n"
               "##############################################", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Next", command=lambda:controller.show_frame(TutorialTwo))
        button1.pack()


class TutorialTwo(tk.Frame):
    def __init__(self, parent, controller):
        time.sleep(2)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Before we begin, lets have a quick tutorial! \n\n'
               'This simulation is designed to mimic that of the decline in real life, which is effecting us in ways '
               'we can\'t understand today...\n ', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Next", command=lambda:controller.show_frame(TutorialThree))
        button1.pack()

class TutorialThree(tk.Frame):
    def __init__(self, parent, controller):
        time.sleep(2)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='As each day passes the bee population decreases further and further.\n '
                                    'In our virtual world, '
               'you make decicions each passing day\nabout what you want to do and how you use the '
                                    'things you have'
               ' access to\n', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Next", command=lambda: controller.show_frame(TutorialFour))
        button1.pack()

class TutorialFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Based on those desicions, the bee population will decline / rise in number\n\n'
                                    'Lets Begin!!!!', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Start Game", command=lambda: controller.show_frame(FirstDay))
        button1.pack()

class FirstDay(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text='Welcome to your first day. At this early in the game you will have a limited amount of options you can'
              ' choose from...\n', font=LARGE_FONT)
        label1.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Okay, Got It", command=lambda: controller.show_frame(SecondLabel))
        button1.pack()


class SecondLabel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Well lay out some basic options first...', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text='Oh No! There are rats running rampant in your house. How many litres pesticide '
                                      'do you use?\n 1. To Kill all and have no problems 2. To Kill half and '
                                      'stomp on a few or 3. Kill all and have no problems\n', font=MEDIUM)
        label2.pack()
        amount = tk.Entry(self)
        amount.pack()
        button1 = ttk.Button(self, text="Enter", command=lambda: c.pesticde1(self, int(amount.get())))
        button1.pack()


c = Algorithms
app = SeaOfBTCApp()
app.mainloop()

