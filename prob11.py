import os
import sys

with open(r"input.txt", 'r') as f:
    contents = f.read().rstrip().strip()

full = int(contents) // 4

if (int(contents) % 4 == 0):
    if full == 1:
        print(f'{full} full car')
    else:
        print(f'{full} full cars')
elif full == 0:
    print('1 partial car')
else:
    if full == 1:
        print(f'{full} full car, 1 partial car')
    else:
        print(f'{full} full cars, 1 partial car')