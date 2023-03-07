import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split('\n')
birth = contents[0].split("-")
skull = contents[1].split("-")
name = contents[2]
    
years = int(skull[0]) - int(birth[0])
months = years * 12
months += int(skull[1]) - int(birth[1])
if int(skull[2]) - int(birth[2]) < 0:
    months -= 1

print(f"{name} is {months} months old")