#!/usr/bin/python3
"""
komentar
"""

from optparse import OptionParser


class Main:
    options = None
    __parser = None
    def __init__(self):
        self.__parser = OptionParser(usage="usage: %prog [options]",
                                     version="%prog 1.0")
        self.__parser.add_option("--neco",
                                 dest="neco",
                                 help="nejaka option",
                                 default="DEFAULTNIHODNOTA")

        (self.options, args) = self.__parser.parse_args()

    def jednaFunkce(self):
        print("jedna")

    def druhaFunkce(self):
        print("druha")

    def tretiFunkce(self):
        print(self.options.neco)


# READ Main class
getter = Main()
getter.jednaFunkce()
getter.druhaFunkce()
getter.tretiFunkce()
