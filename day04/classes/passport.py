#!/usr/bin/env python3

class Passport:
    
    def __init__(self, fields):
        self.fields = fields
        self.required = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

    def add(self, field):
        self.fields.append(field)
        
    def hasRequiredFields(self):
        check = 0
        for field in self.fields:
            if field.key in self.required:
                check += 1
        return (check == len(self.required))

    def hasValidValues(self):
        check = 0
        for field in self.fields:
            if field.isValid():
                check += 1
        return (check == len(self.fields))

    def toString(self):
        string = ''
        for field in self.fields:
            string += field.toString() + ' '
        return string