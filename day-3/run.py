
def parse_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

input = parse_input()

def toboggan_trees(input):
    h_pos, trees = 0, 0
    for line in input:
        if line[h_pos] == '#':
            trees += 1
        h_pos = (h_pos + 3) % len(line)
    return trees

print(toboggan_trees(input))
