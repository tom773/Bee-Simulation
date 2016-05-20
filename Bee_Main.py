#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

class Algorithms():

    rate = 1

    def __init__(self):
        with open('BeePopNumbers.txt', 'r') as pop:
            pop = pop.read()
            self.beePop = int(pop)
        rate = self.rate

    def tick(self):
        self.beePop = self.beePop * self.rate

        save()
    def pesticde1(self, amountofpesticide):

        if amountofpesticide is 0:

            self.rate = self.rate + 0.02
        elif amountofpesticide is 3:

            self.rate = self.rate - 0.03

        else:
            self.rate1 = amountofpesticide * .02212332
            self.rate = self.rate - self.rate1

        print(self.rate)

        return self.rate

    def fundingVirus(self):

        pass
def save():
    pass



