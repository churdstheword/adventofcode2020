#!/usr/bin/env python3

import os

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
input = list(map(int, lines))

def solve_triple(input, total):
    solutions = []
    for current in input:
        diff = total - int(current)
        values = solve_double(input, diff)
        if len(values) > 0:
            for value in values:
                solutions.append([int(current), value[0], value[1]])
    return solutions

def solve_double(input, total):
    solutions = []
    values = []
    for current in input:
        diff = total - int(current)
        if current in values:
            solutions.append([int(current), diff])
        else:
            values.append(diff)
    return solutions


# Part 1 Solutions
answers = solve_double(input, 2020)
print('Part 1: {' + ','.join(str(e) for e in answers) + '}')

# Part2 Solutions
answers = solve_triple(input, 2020)
print('Part 2: {' + ','.join(str(e) for e in answers) + '}')
