#!/usr/bin/env python3

import re

class Field:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def isValid(self):
        check = 0
        if self.key == 'byr':
            if re.match('^[0-9]{4}$', self.value) and 1920 <= int(self.value) <= 2002:
                check += 1
        elif self.key == 'iyr':
            if re.match('^[0-9]{4}$', self.value) and 2010 <= int(self.value) <= 2020:
                check += 1
        elif self.key == 'eyr':
            if re.match('^[0-9]{4}$', self.value) and 2020 <= int(self.value) <= 2030:
                check += 1
        elif self.key == 'hgt':
            result = re.match('^(\d+)(cm|in)$', self.value)
            if result:
                if result.group(2) == 'in' and 59 <= int(result.group(1)) <= 76:
                    check += 1
                if result.group(2) == 'cm' and 150 <= int(result.group(1)) <= 193:
                    check += 1
        elif self.key == 'hcl':
            if re.match('^#[0-9a-f]{6}$', self.value):
                check += 1
        elif self.key == 'ecl':
            if self.value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                check += 1
        elif self.key == 'pid':
            if re.match('^[0-9]{9}$', self.value):
                check += 1
        elif self.key == 'cid':
            check += 1
        
        return (check > 0)

    def toString(self):
        return self.key + ':' + self.value