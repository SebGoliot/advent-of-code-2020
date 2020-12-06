
def parse_input():
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

input = parse_input()

def get_sum_of_distinct_yes(input):
    i, groups = 0, ['']
    for line in input:
        if line == '':
            i += 1
            groups.append('')
        else:
            groups[i] += line
    sum = 0
    for answer in groups:
        sum += len(set(answer))
    return sum

print(get_sum_of_distinct_yes(input))
