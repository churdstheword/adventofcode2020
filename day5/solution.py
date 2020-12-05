#!/usr/bin/env python3

import os
import math

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
lines = list(map(str.rstrip, lines))

def partition(array, left, right):
    for char in array:
        if char == 'F' or char == 'L':
            right = right - math.ceil((right - left) / 2)
        elif char == 'B' or char == 'R':
            left = left + math.ceil((right - left) / 2)
    return left

def part_one(lines):
    highest = 0   
    for line in lines:
        row = partition(line[0:7], 0, 127)
        column = partition(line[7:10], 0, 7)
        seatID = (row * 8) + column
        if seatID > highest:
            highest = seatID
    return highest

def part_two(lines):
    seatID = 0
    seats = []   
    for line in lines:
        row = partition(line[0:7], 0, 127)
        column = partition(line[7:10], 0, 7)
        seats.append((row * 8) + column)
    seats.sort()
    for i in range(len(seats)):
        if i < (len(seats) - 1) and (seats[i + 1] - seats[i]) > 1:
            seatID = seats[i] + 1
    return seatID

print('Solution Part 1: ', part_one(lines))
print('Solution Part 2: ', part_two(lines))