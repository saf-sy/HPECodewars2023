import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split('\n')
    contents.pop()
    
for num in contents:
    if int(num) % 5 == 0:
        if int(num) % 9 == 0:
            print(f"{num} FIZZ FUZZ!")
            continue
        else:
            print(f"{num} FIZZ")
            continue
    if int(num) % 9 == 0:
        print(f"{num} FUZZ")
