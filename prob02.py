import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    contents.pop()
    
for num in contents:
    if int(num) % 4 == 0:
        print(f"{num}/4 = {int(int(num)/4)}")