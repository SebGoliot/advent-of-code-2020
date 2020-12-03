
def parse_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

input = parse_input()

def toboggan_trees(input, right, down):
    h_pos, trees = 0, 0
    for v_pos in range(0, len(input), down):
        line = input[v_pos]
        if line[h_pos] == '#':
            trees += 1
        h_pos = (h_pos + right) % len(line)
    return trees

x = 1
x *= toboggan_trees(input, right=1, down=1)
x *= toboggan_trees(input, right=3, down=1)
x *= toboggan_trees(input, right=5, down=1)
x *= toboggan_trees(input, right=7, down=1)
x *= toboggan_trees(input, right=1, down=2)

print(x)
