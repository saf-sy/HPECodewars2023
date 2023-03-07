import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    
operator = contents.pop(0)

if len(contents) > 2:
    last = contents.pop()
    a = ""

    for i in contents:
        a += (i + ", ")
    
    a += (operator.lower() + " " + last)

    print(a)
elif len(contents) == 2:
    print(contents[0] + " " + operator.lower() + " " + contents[1])
else:
    print(contents[0])