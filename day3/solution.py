#!/usr/bin/env python3

import os

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()

# Gets the tile value located at the position vector
def getPositionValue(position, lines):
    line = lines[position[1]].rstrip()
    return line[position[0] % len(line)]

# Returns the sum of two vectors
def translate(vector1, vector2):
    sum = []
    for i in range(len(vector1)):
        sum.append(vector1[i] + vector2[i])
    return sum

# Calculates the number of trees over a projected path. 
# Assumes a fixed starting postion and a constant velocity vector
def calculate(lines, velocity):
    position = [0, 0]
    count = 0
    while position[1] < len(lines):      
        # Check the tile value based on the current position
        if getPositionValue(position, lines) == '#':
            count += 1
        # Traverse according to our movement vector
        position = translate(position, velocity)
    return count


def part_one(lines):
    velocity = [3,1]
    # Calculate the number of trees for the projected path
    trees = calculate(lines, velocity)
    print('Solution Part 1: ', trees)


def part_two(lines):
    velocities = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    value = 0
    # Calculate the number of trees for each projected path and get a total product
    for velocity in velocities:
        trees = calculate(lines, velocity)
        if value == 0:
            value = trees
        else:
            value = value * trees
    print('Solution Part 2: ', value)
   

part_one(lines)
part_two(lines)
