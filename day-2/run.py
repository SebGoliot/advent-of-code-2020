import re

def parse_input() -> list:
    input = []
    with open('input.txt', 'r') as f:
        input = f.read()
    regex = r"(\d+)-(\d+) (\w): (\w+)"
    return re.findall(regex, input)

input = parse_input()

def get_valid_passwords(input):
    n = 0
    for pwd in input:
        i = pwd[3].count(pwd[2])
        if i >= int(pwd[0]) and i <= int(pwd[1]):
            n += 1
    return n

print(get_valid_passwords(input))