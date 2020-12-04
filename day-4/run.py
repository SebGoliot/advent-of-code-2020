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
    passport_needed_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid_passports = 0
    for passport in input:
        missing_keys = [key for key in passport_needed_keys if key not in passport.keys()]
        if len(missing_keys) == 0:
            if (
                int(passport['byr']) in range(1920, 2002+1) and
                int(passport['iyr']) in range(2010, 2020+1) and
                int(passport['eyr']) in range(2020, 2030+1) and
                passport['ecl'] in eye_colors and
                len(passport['pid']) == 9 and
                int(passport['pid']) and
                passport['hgt'][-2:] in ['cm', 'in'] and
                int(passport['hgt'][:-2]) and
                passport['hcl'][0] == '#' and
                int(passport['hcl'][1:], 16)
            ):
                if (
                    (
                        passport['hgt'][-2:] == 'cm' and 
                        int(passport['hgt'][:-2]) in range(150, 193+1)
                    )
                    or
                    (
                        passport['hgt'][-2:] == 'in' and 
                        int(passport['hgt'][:-2]) in range(59, 76+1)
                    )
                ):
                    valid_passports += 1
    return valid_passports

print(verify_passports(input))
