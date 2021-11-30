#!/usr/bin/env python3

import os

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
lines = list(map(str.rstrip, lines))
lines = [int(i) for i in lines]

def part_one(joltages):
    
    joltages.sort()
    deviceJoltage = joltages[-1] + 3
    
    oneJoltDiffs = 1
    threeJoltDiffs = 0
    
    for i in range(0, len(joltages)):
        if i == len(joltages) - 1:
            diff = deviceJoltage - joltages[i]
        else: 
            diff = joltages[i+1] - joltages[i]

        if diff == 3:
            threeJoltDiffs = threeJoltDiffs + 1
        else:
            oneJoltDiffs = oneJoltDiffs + 1

    return oneJoltDiffs * threeJoltDiffs

def part_two(joltages):

    joltages.sort()
    deviceJoltage = joltages[-1] + 3
    
    joltages.append(0)
    joltages.append(deviceJoltage)
    joltages.sort(reverse=True)

    solutions = {}   
    for currentJoltage in joltages:
        total = 0
        if currentJoltage == deviceJoltage:
            total = 1            
        else:
            for nextJoltage in joltages:
                diff = nextJoltage - currentJoltage
                if diff > 0 and diff <= 3:
                    total = total + solutions[nextJoltage]
        
        solutions[currentJoltage] = total

    return solutions[0]

print('Solution Part 1: ', part_one(lines))
print('Solution Part 2: ', part_two(lines))