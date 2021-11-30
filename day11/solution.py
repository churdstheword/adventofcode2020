#!/usr/bin/env python3

import os

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
lines = list(map(str.rstrip, lines))

class GameOfLife:

    def __init__(self, lines):
        self.height = len(lines)
        self.width = len(lines[0])
        self.lines = lines

    def getValue(self, row, col):
        return self.lines[row][col]

    def step(self):
        self.newLines = self.lines.copy()
        for row in range(len(self.lines)):
            for col in range(len(self.lines[row])):
                occupied = 0
                for seat in self.getAdjacentSeats(row, col):
                    if self.getValue(seat[0], seat[1]) == chr(35):
                        occupied = occupied + 1
                if self.lines[row][col] == 'L' and occupied == 0:
                    r = list(self.newLines[row])
                    r[col] = chr(35)
                    self.newLines[row] = "".join(r)
                elif self.lines[row][col] == chr(35) and occupied >= 4:
                    r = list(self.newLines[row])
                    r[col] = 'L'
                    self.newLines[row] = "".join(r)
        self.lines = self.newLines.copy()

    def getAdjacentSeats(self, row, col):
        seats = []
        for r,c in [(row + i, col + j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
            if r >= 0 and r < self.height and c >= 0 and c < self.width:
                seats.append([r,c])
        return seats

    def countOccupiedSeats(self):
        count = 0
        for row in range(len(self.lines)):
            for col in range(len(self.lines[row])):
                if self.lines[row][col] == chr(35):
                    count = count + 1
        return count

    def print(self):
        for row in range(len(self.lines)):
            print(self.lines[row])


def part_one(lines):
    game = GameOfLife(lines)
    for i in range(0,150):
        game.step()
    return game.countOccupiedSeats()

print('Solution Part 1: ', part_one(lines))
# print('Solution Part 2: ', part_two(lines))