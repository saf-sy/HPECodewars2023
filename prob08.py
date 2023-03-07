import os
import sys
import math

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    
base = int(contents[0])
total = int(contents[1])

num = math.log(total, base)

print(str(base) + "^" + str(int(num)), "=", total)