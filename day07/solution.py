#!/usr/bin/env python3

import os
import re

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")
lines = file.readlines()
lines = list(map(str.rstrip, lines))


class Bag:

    def __init__(self, name, contains):
        self.name = name
        self.contains = contains

    def canContain(self, qty, name):
        if len(self.contains) > 0:
            for data in self.contains:
                if data['bag'].name == name and int(qty) <= int(data['qty']):
                    return True
                elif data['bag'].canContain(qty, name):
                    return True
        return False

    def countContents(self):
        count = 0
        if len(self.contains) > 0:
            for data in self.contains:
                count += int(data['qty']) + (int(data['qty']) * int(data['bag'].countContents()))
        return count

    def toString(self):
        bags = []
        for data in self.contains:
            bags.append('{ "qty": "' + data['qty'] + '", "bag": ' + data['bag'].toString() + ' }')
        return '{"' + self.name + '": { "contains": [' + ', '.join(bags) + '] } }' 


def parseLine(line):
    line_matches = re.match(r'^(.*) bags contain (.*)\.$', line)
    bag_name = line_matches.group(1)
    
    if(re.match(r'no other bags', line_matches.group(2))): 
        return Bag(bag_name, [])
    
    bag_contains = []
    for line_match in line_matches.group(2).split(', '):
        
        bag_matches = re.match(r'([0-9]+|no) (\w+ \w+) (?:bag|bags)', line_match)
        bag_object = parseLine(getLine(bag_matches.group(2)))
        
        bag_contains.append({
            'bag': bag_object,
            'qty': bag_matches.group(1)
        })

    return Bag(bag_name, bag_contains)


def getLine(name):
    global lines
    for line in lines:
        line_matches = re.match(r'^(.*) bags contain (.*)\.$', line)
        bag_name = line_matches.group(1)
        if(name == bag_name):
            return line
    return ''


def part_one(lines):
    can_contain = 0
    for line in lines:
        bag = parseLine(line)
        if bag.canContain(1, 'shiny gold'):
            can_contain += 1
    return can_contain


def part_two(lines):
    line = getLine('shiny gold')
    bag = parseLine(line)
    count = bag.countContents()
    return count


print('Solution Part 1: ', part_one(lines))
print('Solution Part 2: ', part_two(lines))