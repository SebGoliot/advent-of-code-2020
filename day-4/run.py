import re

def parse_input() -> list:
    regex = r"(\S+):(\S+)"
    with open('input.txt', 'r') as f:
        passport, passports = {}, []
        for line in f.readlines():
            if line == '\n':
                passports.append(passport)
                passport = {}
            else:
                for data in re.findall(regex, line):
                    passport[data[0]] = data[1]

    return passports

input = parse_input()

def verify_passports(input):
    passport_needed_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']#, 'cid']
    valid_passports = 0
    for passport in input:
        missing_keys = [key for key in passport_needed_keys if key not in passport.keys()]
        if len(missing_keys) == 0:
            valid_passports += 1
    return valid_passports

print(verify_passports(input))
