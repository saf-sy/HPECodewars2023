import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    contents.pop()

for line in contents:
    line = line.split("-")
    if len(line) == 3:
        print(f"xxx-xx-{line[2]}")
    else:
        print(f"xxxx-xxxx-xxxx-{line[3]}")