#!/usr/bin/env python3

import os
import string

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
lines = list(map(str.rstrip, lines))

def part_one(lines):
    total = 0
    group = ''
    for i in range(len(lines)):  
        if i == (len(lines) - 1):
            group += lines[i]
            total += len(set(group)) 
        elif lines[i] == '':
            total += len(set(group))
            group = ''
        else:
            group += lines[i]
    return total

def part_two(lines):
    total = 0
    group = ''
    persons = 0
    for i in range(len(lines)):
        if lines[i] != '':
            group += lines[i]
            persons += 1
        if lines[i] == '' or i == (len(lines) - 1):
            for char in string.ascii_lowercase:
                count = group.count(char)
                if count == persons:
                    total += 1
            group = ''
            persons = 0
    return total

print('Solution Part 1: ', part_one(lines))
print('Solution Part 2: ', part_two(lines))
