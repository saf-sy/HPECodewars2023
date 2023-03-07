import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().split("\n")
    contents.pop()

listFib = [0, 1, 1]
for line in contents:
    line = line.split(" ")
    while len(listFib) < int(line[0])+1:
        listFib.append(int(listFib[-1])+int(listFib[-2])+int(listFib[-3]))
    print(listFib[int(line[0])]-listFib[int(line[1])])