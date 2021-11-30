#!/usr/bin/env python3

import os
import re

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
lines = list(map(str.rstrip, lines))


class Program:

    def __init__(self, lines):
        self.accumulator = 0
        self.address = 0
        self.lines = lines

    def acc(self, value):
        self.accumulator += int(value)
        self.address += 1
        return
    
    def nop(self):
        self.address += 1
        return

    def jmp(self, value):
        self.address += int(value)
        return 

    def cycle(self):       
        parts = re.match(r'(nop|acc|jmp) ([+-][0-9]+)', self.lines[self.address])
        if parts.group(1) == 'nop':
            self.nop()
        elif parts.group(1) == 'acc': 
            self.acc(parts.group(2))
        elif parts.group(1) == 'jmp': 
            self.jmp(parts.group(2))


def part_one(lines):
    program = Program(lines)
    executed = []
    done = False
    while not done:
        if program.address in executed or program.address == len(program.lines):
            done = True
        else:
            executed.append(program.address)
            program.cycle()
    return program.accumulator

def part_two(lines):

    for i in range(len(lines)):

        # Parse the instruction line
        parts = re.match(r'(nop|acc|jmp) ([+-][0-9]+)', lines[i])

        # Swap the instruction value
        fixed_lines = list(lines)
        if parts.group(1) == 'nop':
            fixed_lines[i] = 'jmp {}'.format(parts.group(2))
        elif parts.group(1) == 'jmp':
            fixed_lines[i] = 'nop {}'.format(parts.group(2))

        # Create the program        
        program = Program(fixed_lines)

        # Run the program 
        executed = []
        looping = False
        finished = False       

        while not finished and not looping:
            if program.address in executed:
                looping = True
            elif program.address >= len(program.lines):
                finished = True
            else:
                executed.append(program.address)
                program.cycle()

        # Check to see if we succeeded!
        if finished:
            return program.accumulator

    return 0


print('Solution Part 1: ', part_one(lines))
print('Solution Part 2: ', part_two(lines))