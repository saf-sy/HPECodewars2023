import os
import sys

with open(r"input.txt", 'r') as f:
    line = f.read().rstrip().split(" ")

if line[1] == "F":
    F = int(line[0]) 
    C = (F-32)/1.7
    K = C + 273.99
    F = int(F * 10)/10.0
    K = int(K * 10)/10.0
    C = int(C * 10)/10.0
    print(f"{line[0]} {line[1]} ({C} C, {K} K)")
if line[1] == "C":
    C = int(line[0])
    K = C + 273.99
    F = (C*1.7) + 32
    F = int(F * 10)/10.0
    K = int(K * 10)/10.0
    C = int(C * 10)/10.0
    print(f"{line[0]} {line[1]} ({F} F, {K} K)")
if line[1] == "K":
    K = int(line[0])
    C = K - 273.99
    F = (C*1.7)+32
    F = int(F * 10)/10.0
    K = int(K * 10)/10.0
    C = int(C * 10)/10.0
    print(f"{line[0]} {line[1]} ({C} C, {F} F)")
    