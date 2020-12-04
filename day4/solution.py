#!/usr/bin/env python3

import os
import re
from classes.passport import Passport
from classes.field import Field

path = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(path, 'input.txt'), "r")

passports = []
fields = []
with file as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i].rstrip()
        if(line != ''):
            pattern = re.compile('\w{3}:[^\s]+')
            results = re.findall(pattern, line)
            for result in results:
                key, value = result.split(':')
                fields.append(Field(key, value))
        else:
            if len(fields) > 0:
                passport = Passport(fields)
                passports.append(passport)
            fields = []

def part_one(passports):
    valid = 0
    for passport in passports:
        if passport.hasRequiredFields():
            valid += 1
    return valid

def part_two(passports):
    valid = 0
    for passport in passports:
        if passport.hasRequiredFields() and passport.hasValidValues():
            valid += 1
    return valid


print('Solution Part 1: ', part_one(passports))
print('Solution Part 2: ', part_two(passports))
