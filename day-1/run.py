def parse_input() -> list:
    input = []
    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
    return [int(x) for x in input]

input = parse_input()

def find_sum(input):
    for x in input:
        for y in input:
            if x + y == 2020:
                print(f"{x} + {y} = 2020 !")
                print(f"{x} x {y} = {x*y} !")
                return

find_sum(input)
