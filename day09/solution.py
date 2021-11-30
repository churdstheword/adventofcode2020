#!/usr/bin/env python3

import os
import re

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
lines = list(map(str.rstrip, lines))


def part_one(lines):
    preamble = 25
    for i in range(preamble, len(lines)):
        found = False
        for j in range(i - preamble, i):
            if int(lines[j]) > int(lines[i]):
                continue
            for k in range(j + 1, i):
                if (int(lines[j]) + int(lines[k])) == int(lines[i]):
                    found = True
                    break
            if found:
                break
        if not found:
            return int(lines[i])
    return 0

def part_two(lines):

    target = part_one(lines)
    for i in range(len(lines)):
        if (i + 1) < len(lines):
            sum = int(lines[i])
            for j in range(i + 1, len(lines)):
                sum += int(lines[j])
                if sum == target:
                    final = lines[i : j + 1]
                    final.sort(key = int)
                    return int(final[0]) + int(final[-1])
                elif sum > target:
                    break

    return 0

print('Solution Part 1: ', part_one(lines))
print('Solution Part 2: ', part_two(lines))