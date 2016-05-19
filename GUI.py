import tkinter as tk
from tkinter import ttk
import time

LARGE_FONT= ("Verdana", 20)


class SeaOfBTCApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TutorialOne, TutorialTwo, TutorialThree, TutorialFour):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)


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
        time.sleep(2)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Based on those desicions, the bee population will decline / rise in number\n\n'
                                    'Lets Begin!!!!', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Start Game", command=lambda: controller.show_frame(TutorialFour))
        button1.pack()

app = SeaOfBTCApp()
app.mainloop()