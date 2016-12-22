#!/usr/bin/env python

import sys
from os import remove, removedirs
from os.path import dirname, join, isfile
from time import time

def rates(ratings):
    # tmp = open('books.csv','r')
    # for i,src in enumerate(tmp.readlines()[1:11]):
    #     if i == 0:topBooks = src
    #     else: 
    #         topBooks = topBooks+src
    topBooks=["9$$Hand in Glove", 
    "15$$Celebremos Su Gloria",
    "19$$One, Two, Guess Who?" ,
    "21$$Who on Earth is Tom Baker?",
    "22$$Mog's Kittens",
    "25$$Chess for Children",
    "30$$Misty of Chincoteague",
    "33$$Suddenly One Was Taken!",
    "36$$Chess for Young Beginners",
    "37$$The Little Engine That Could: Pop-up Book"]
    now = int(time())
    n = 0

    f = open("personalRatings.txt",'w')
    for line,rStr in zip(topBooks,ratings.split(",")):
        ls = line.split("$$")
        valid = False
        while not valid:
            if ls[0]!='':
                r = int(rStr) if rStr.isdigit() else -1
                valid = True
                if r > 0:
                    f.write("0$$%s$$%d$$%d\n" % (ls[0], r, now))
                    n += 1
            else :break
    f.close()
    return "personalRatings.txt"

