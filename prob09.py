import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    
contents.pop(0)
t = (int(contents.pop(0)))/60

for line in contents:
    line = line.split(" ")
    r = int(line[0])
    s = line[1]
    dist = int((r * t)*100)/100
    d = dist
    a = ""
    for i in range(int(d/5)):
        a += "-"
    d %= 5
    for i in range(int(d/1)):
        a += "~"
    d %= 1
    for i in range(int(d/.25)):
        a += "{}"
    
    
    print("({0:.2f})".format(dist) + a +s)
    