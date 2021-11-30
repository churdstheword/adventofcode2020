#!/usr/bin/env python3

import os
import re

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()

def part_one():
    count = 0
    for line in lines:

        # Parse the line into parts using regex
        pattern = re.compile('(\d+)\-(\d+) (\w): (\w+)')
        result = pattern.match(line)

        # Determine the number of ocurrences of the letter in the password
        n = 0
        for char in result.group(4):
            if(char == result.group(3)):
                n += 1
        
        # Check to see if the frequency of the letter is in bounds
        if( int(result.group(1)) <= n <= int(result.group(2))):
            count += 1
    return count

def part_two():
    count = 0
    for line in lines:
        
        # Parse the line into parts using regex
        pattern = re.compile('(\d+)\-(\d+) (\w): (\w+)')
        result = pattern.match(line)
        password = result.group(4)
        letter = result.group(3)
        
        # If the password is too short, consider it to have failed
        if(int(result.group(2)) > len(password)):
            break

        # Check both positions and xor the results
        pos1_check = (password[int(result.group(1)) - 1] == letter)
        pos2_check = (password[int(result.group(2)) - 1] == letter)
        if  pos1_check != pos2_check:
            count += 1

    return count


print('Solution Part 1: ', part_one())
print('Solution Part 2: ', part_two())
