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

def find_sum_part_2(input):
    for x in input:
        for y in input:
            for z in input:
                if x + y + z == 2020:
                    print(f"{x} + {y} + {z} = 2020 !")
                    print(f"{x} x {y} x {z} = {x*y*z} !")
                    return

find_sum_part_2(input)
