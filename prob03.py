import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    
i = int(contents[0])
p = int(contents[1])
r = float(contents[2])
t = int(contents[3])

ptotal = i*(1+r)*t
if ptotal > p:
    print(f"At the current rate of growth there will be {int(ptotal)} ponies in {t} years.")
    print(f"Celestia will need to add space for at least {int(ptotal - p)} ponies!")
else:
    print(f"At the current rate of growth there will be {int(ptotal)} ponies in {t} years.")
    print("Celestia won't need to add space yet!")
        