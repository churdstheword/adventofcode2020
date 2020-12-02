#!/usr/bin/env python3

import os

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()

final = 2020
solutions = []
for line in lines:
    current = int(line)
    diff = final - current
    # Check to see if current is already a solution to a previous entry
    if current in solutions: 
        # Find the product of the entries and output the answer
        product = current * (diff)
        print('(' + str(current) + ', ' + str(diff) + ') Product: ' + str(product))
    else:
        # Add diff to the list of possible solutions
        solutions.append(diff)
