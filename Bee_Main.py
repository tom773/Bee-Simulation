#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from urllib import request
import matplotlib
import threading


class MainMenu:

    def __init__(self):

        pass

    def turnloop(self, gameRunning):

        if gameRunning is True:

            b.begin()

        else:
            print('Game is not running')



    def menu(self):

        global b

        chosenOption = int(input(" 1. Start Game \n> "))

        if chosenOption is 1:

            gameRunning = True

            self.turnloop(gameRunning)


        else:
            print("Not a Valid selection")


class Algorithms():

    rate = 1

    def __init__(self):
        with open('BeePopNumbers.txt', 'r') as pop:
            pop = pop.read()
            self.beePop = int(pop)
        rate = self.rate

    def tick(self):
        self.beePop = self.beePop * self.rate

        b.save()
    def pesticde1(self, amountofpesticide):

        if amountofpesticide is 0:

            self.rate = self.rate + 0.02
        elif amountofpesticide is 3:

            self.rate = self.rate - 0.03

        else:
            self.rate1 = amountofpesticide * .02212332
            self.rate = self.rate - self.rate1

        return self.rate


class MainGame():

    def __init__(self):
        pass

    def save(self):

        pass

    def begin(self):

        # print("##############################################\n      "
        #       "WELCOME TO THE BEE SIMULATION!!     \n"
        #       "##############################################")
        # time.sleep(2)
        #
        # print('Before we begin, lets have a quick tutorial! \n\n'
        #       'This simulation is designed to mimic that of the decline in real life, which is effecting us in ways '
        #       'we can\'t understand today...\n ')
        # time.sleep(5)
        # print('As each day passes the bee population decreases further and further. In our virtual world, '
        #       'you make decicions each passing day\nabout what you want to do and how you use the things you have'
        #       ' access to\n')
        # time.sleep(7)
        # print('Based on those desicions, the bee population will decline / rise in number\n\nLets Begin!!!!')
        # time.sleep(3)
        self.firstday()
    def firstday(self):

        print('Welcome to your first day. At this early in the game you will have a limited amount of options you can'
              ' choose from\n')
        time.sleep(2)
        print('We\'ll lay out some basic options first: \n')
        time.sleep(3)
        amountofpesticide = int(input('Oh No! There are rats running rampant in your house. How many litres pesticide '
                                      'do you use? 1. To Kill all and have no problems 2. To Kill half and '
                                      'stomp on a few or 3. Kill all and have no problems\n> '))
        print(c.pesticde1(amountofpesticide))
        time.sleep(3)
        c.tick()
        print('The bee population is now: ', c.beePop)


a = MainMenu()
b = MainGame()
c = Algorithms()
a.menu()




