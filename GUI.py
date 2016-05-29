import time

rate = 1

with open('BeePopNumbers.txt', 'r') as pop:
    pop = pop.read()
    beePop = int(pop)


def tick(self):
    global beePop
    beePop = beePop * rate
    return beePop

def popupmsg(msg):

    popupwindow = tk.Tk()
    popupwindow.wm_title('!')
    label = ttk.Label(popupwindow, text=msg)
    label.pack(side='top', fill='x', pady=10)
    b1 = tk.Button(popupwindow, text='Okay', command=lambda: popupwindow.destroy())
    b1.pack()
    popupwindow.mainloop()


class Algorithms():

    global rate

    def __init__(self):

        pass

    def pesticde1(self, amountofpesticide):
        global rate

        if amountofpesticide is 0:

            rate = rate + 0.02
        elif amountofpesticide is 3:

            rate = rate - 0.03

        elif amountofpesticide is 1:

            rate = rate - 0.002334
        elif amountofpesticide is 2:

            rate = rate - 0.0146923

        else:
            return "Not a Valid Selection, Try Again"

        return rate

    def Charity(self, amountmoney):
        global rate
        rate1 = amountmoney * 0.000050092
        rate = rate + rate1
        return rate

    def typeHoney(self, ChosenHoney):
        global rate
        if ChosenHoney == str('Calipino'):
            rate1 = 0.00221
            rate = rate + rate1
        elif ChosenHoney == str('Coles Home Brand'):
            rate1 = 0.082237
            rate = rate - rate1
        elif ChosenHoney == str('Australian Honey Brand'):
            rate1 = 0.033323
            rate = rate - rate1
        elif ChosenHoney == str('Manuku Honey New Zealand'):
            rate1 = 0.011232
            rate = rate + rate1
        return rate
    def save(self):

        with open('BeePopNumbers.txt', 'w') as pop:
            pop = pop.write(beePop)

import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation

LARGE_FONT= ("Verdana", 20)
MEDIUM= ("Verdana", 16)
style.use('ggplot')

class BeeSimGui(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(3, weight=1)
        container.grid_columnconfigure(3, weight=1)

        self.frames = {}

        for F in (StartPage, TutorialOne, TutorialTwo, TutorialThree, TutorialFour, FirstDay, SecondLabel,
                  SecondDay, SecondDay1, ThirdDay1):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

            frame.configure(background='#00A3E0')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="THIS SIMULATION IS EARLY ALPHA 0.3.1. This is a stable stage "
                                    "of which you have 3 different days to work with...\n", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Agree", command=lambda:controller.show_frame(TutorialOne))
        button1.pack()
        button2 = tk.Button(self, text="Disagree", command=lambda: quit())
        button2.pack()


class TutorialOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="##############################################\n      "
               "WELCOME TO THE BEE SIMULATION!!     \n"
               "##############################################", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Next", command=lambda:controller.show_frame(TutorialTwo))
        button1.pack()


class TutorialTwo(tk.Frame):
    def __init__(self, parent, controller):
        time.sleep(2)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Before we begin, lets have a quick tutorial! \n\n'
               'This simulation is designed to mimic that of the decline in real life, which is effecting us in ways '
               'we can\'t understand today...\n ', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(10,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960,
                1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976,
                1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992,
                1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                2009, 2010],
               [5500000, 5500000, 5430000, 5420000, 5425032, 5433200, 5503020, 5500030,
                5435476, 5365343, 5322342, 5433454, 5762638, 5626379, 5533450, 5505032,
                5325374, 5229382, 5332534, 5442435, 5632436, 5225356, 5354252, 5543344,
                5544345, 5533453, 5433453, 5335344, 5345473, 5222223, 5199872, 5203002,
                5102293, 5100330, 5093929, 5022332, 4999221, 4922322, 4822828, 4789800,
                4733723, 4636364, 4444323, 4478779, 4422302, 4122321, 3999212, 4002293,
                3888182, 3772373, 3642069, 3444333, 3220032, 3002230, 2883292, 2992283,
                3322332, 3441422, 3322332, 2993828, 2777283, 2633543, 2339862, 2122039,
                2100293, 2003993], 'g')

        title = "Bee Population Decline Since 1945 (Bee Hives In Millions)"
        a.set_title(title)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        button1 = tk.Button(self, text="Next", command=lambda:controller.show_frame(TutorialThree))
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
        button1 = tk.Button(self, text="Next", command=lambda: controller.show_frame(TutorialFour))
        button1.pack()


class TutorialFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Based on those desicions, the bee population will decline / rise in number\n\n'
                                    'Lets Begin!!!!', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Start Game", command=lambda: controller.show_frame(FirstDay))
        button1.pack()


class FirstDay(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text='Welcome to your first day. At this early in the game you will have a limited '
                                     'amount of options you can'
              ' choose from...\n', font=LARGE_FONT)
        label1.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Okay, Got It", command=lambda: controller.show_frame(SecondLabel))
        button1.pack()


class SecondLabel(tk.Frame, Algorithms):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Algorithms.__init__(self)
        label = tk.Label(self, text='Well lay out some basic options first. The Decicions you make now will '
                                    'continue to impact the bee population each \'Tick\'', font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label2 = tk.Label(self, text='Oh No! There are snails everywhere in your garden!!. How many litres pesticide '
                                      'do you use?\n 0. To Kill none and have to stomp on them all 1. '
                                     'To Kill some and '
                                      'stomp on a most\n2. To Kill most and stomp on some'
                                     ' 3. Kill all and have no problems\n', font=MEDIUM)
        label2.pack()
        amount = tk.Entry(self)
        amount.pack()
        button1 = ttk.Button(self, text="Enter", command=lambda: self.showLabel(amount, button1, label,
                                                                                label2, controller))
        button1.pack()

    def showLabel(self, amount, button1, label, label2, controller):
        amount1 = int(amount.get())
        amount.destroy()
        button1.destroy()
        label.destroy()
        label2.destroy()
        rate3 = str(Algorithms.pesticde1(self, amountofpesticide=amount1)), '%'
        label4 = tk.Label(self, text='The current rate at which the bees are populating is:\n', font=LARGE_FONT)
        label4.pack()
        label3 = tk.Label(self, text=rate3, font=MEDIUM)
        label3.pack()
        button2 = ttk.Button(self, text="Next Day", command=lambda: controller.show_frame(SecondDay))
        button2.pack()


class SecondDay(tk.Frame, Algorithms):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Algorithms.__init__(self)
        button1 = tk.Button(self, text='Next', command=lambda: self.showPop(button1, controller))
        button1.pack()

    def showPop(self, button1, controller):
        button1.destroy()
        label = tk.Label(self, text='The Current Bee Population is:\n' + str(tick(self)), font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text='Next', command=lambda: self.nextDay(label, button1, controller))
        button1.pack()

    def nextDay(self, label, button1, controller):
        label.destroy()
        button1.destroy()
        label1 = tk.Label(self, text='Congratulations on completing your first day!\nToday will be a bit different to '
                                     'the first as You\'ll have a new options to input!\n'
                                     'Each day you will continue to be able to input', font=LARGE_FONT)
        label1.pack()
        button2 = tk.Button(self, text='Okay', command=lambda: controller.show_frame(SecondDay1))
        button2.pack()


class SecondDay1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Enter your donation to www.wheenbeefoundation.org.au. \n"
                                     "This website is a way you can contribute to the Colony Collapse Disorder Issue\n"
                                     "Min 0, Max 100,000. No dollar signs or commas", font=LARGE_FONT)
        label1.pack()
        donation = tk.Entry(self)
        donation.pack()
        button1 = tk.Button(self, text="Okay", command=lambda: self.showPop(controller, label1, donation, button1))
        button1.pack()

    def showPop(self, controller, label1, donation, button1):
        money = int(donation.get())
        label1.destroy()
        donation.destroy()
        button1.destroy()

        rate3 = Algorithms.Charity(self, amountmoney=int(money)), '%'
        label4 = tk.Label(self, text='The current rate at which the bees are populating is:\n', font=LARGE_FONT)
        label4.pack()
        label3 = tk.Label(self, text=rate3, font=LARGE_FONT)
        label3.pack()
        button2 = tk.Button(self, text='Okay', command=lambda: self.tickDay(label4, label3, button2, controller))
        button2.pack()

    def tickDay(self, label4, label3, button2, controller):

        label4.destroy()
        label3.destroy()
        button2.destroy()

        label5 = tk.Label(self, text=tick(self), font=LARGE_FONT)
        label5.pack()
        button3 = tk.Button(self, text="Next", command=lambda: controller.show_frame(ThirdDay1))
        button3.pack()


class ThirdDay1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="You're at coles and you have a choice on which brand of honey to buy:\n"
                                     "1. Calipino - $3.50 2. Coles Home Brand - $1.50\n"
                                     "3. Honey Australia Brand - $1.20 or 4. Manuku Honey New Zealand - $7.28",
                          font=LARGE_FONT)
        label1.pack()
        ChosenHoney = tk.Entry(self)
        ChosenHoney.pack()
        button1 = tk.Button(self, text="Okay", command=lambda: self.showPop(controller, label1, ChosenHoney, button1))
        button1.pack()

    def showPop(self, controller, label1, ChosenHoney, button1):
        ChosenBrand = str(ChosenHoney.get())
        label1.destroy()
        ChosenHoney.destroy()
        button1.destroy()

        rate3 = Algorithms.typeHoney(self, ChosenHoney=str(ChosenBrand)), '%'
        label4 = tk.Label(self, text='The current rate at which the bees are populating is:\n', font=LARGE_FONT)
        label4.pack()
        label3 = tk.Label(self, text=rate3, font=LARGE_FONT)
        label3.pack()
        button2 = tk.Button(self, text='Okay', command=lambda: self.tickDay(label4, label3, button2, controller))
        button2.pack()

    def tickDay(self, label4, label3, button2, controller):

        label4.destroy()
        label3.destroy()
        button2.destroy()

        label5 = tk.Label(self, text=tick(self), font=LARGE_FONT)
        label5.pack()
        button3 = tk.Button(self, text='Okay')
        button3.pack()


class FourthDay1NotDone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="You're at coles and you have a choice on which brand of honey to buy:\n"
                                     "1. Calipino - $3.50 2. Coles Home Brand - $1.50\n"
                                     "3. Honey Australia Brand - $1.20 or 4. Manuku Honey New Zealand - $7.28",
                          font=LARGE_FONT)
        label1.pack()
        ChosenHoney = tk.Entry(self)
        ChosenHoney.pack()
        button1 = tk.Button(self, text="Okay", command=lambda: self.showPop(controller, label1, ChosenHoney, button1))
        button1.pack()

    def showPop(self, controller, label1, ChosenHoney, button1):
        ChosenBrand = str(ChosenHoney.get())
        label1.destroy()
        ChosenHoney.destroy()
        button1.destroy()

        rate3 = Algorithms.typeHoney(self, ChosenHoney=str(ChosenBrand)), '%'
        label4 = tk.Label(self, text='The current rate at which the bees are populating is:\n', font=LARGE_FONT)
        label4.pack()
        label3 = tk.Label(self, text=rate3, font=LARGE_FONT)
        label3.pack()
        button2 = tk.Button(self, text='Okay', command=lambda: self.tickDay(label4, label3, button2, controller))
        button2.pack()

    def tickDay(self, label4, label3, button2, controller):

        label4.destroy()
        label3.destroy()
        button2.destroy()

        label5 = tk.Label(self, text=tick(self), font=LARGE_FONT)
        label5.pack()
        button3 = tk.Button(self, text='Okay')
        button3.pack()

app = BeeSimGui()
app.mainloop()

