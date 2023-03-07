import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    
thing = contents[0]

print(thing, "is at at index:", contents[1].find(thing))