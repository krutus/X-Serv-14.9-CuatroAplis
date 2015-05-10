#!/usr/bin/python

"""14.9 CuatroAplis
    Luis Haro """

import random
import webapp

class randomApp ():

    def parse(self, request, rest):
        return "Hecho"

    def process(self, parsedRequest):
        RandN = str (random.randint (0,1000000))
        RandURL = ("<html><a href= /aleat>Dame otra</a></html>" + str(RandN))
        return ("200 OK", RandURL)


