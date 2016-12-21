#!/usr/bin/env python

import sys
from os import remove, removedirs
from os.path import dirname, join, isfile
from time import time

tmp = open('books.csv','r')
for i,src in enumerate(tmp.readlines()[0:10]):
    if i == 0:topBooks = src
    else: 
        topBooks = topBooks+src
tmp.close()
current_personalRating = "personalRatings.dat"
parentDir = dirname(dirname(__file__))
ratingsFile = join(parentDir, "personalRatings.txt")

if isfile(ratingsFile):
    r = input("Looks like you've already rated the Books. Overwrite ratings (y/N)? ")
    if r and r[0].lower() == "y":
        remove(ratingsFile)
    else:
        sys.exit()

prompt = "Please rate the following books (1-5 (best), or 0 if not read before): "
print (prompt)

now = int(time())
n = 0

f = open(ratingsFile, 'w')
for line in topBooks.split("\n"):
    ls = line.split(",")
    valid = False
    while not valid:
        if ls[0]!='':
            rStr = input(ls[1] + ": ")
            r = int(rStr) if rStr.isdigit() else -1
            if r < 0 or r > 5:
                print (prompt)
            else:
                valid = True
                if r > 0:
                    f.write("0,%s,%d,%d\n" % (ls[0], r, now))
                    n += 1
        else :break
f.close()

if n == 0:
    print ("No rating provided!")
