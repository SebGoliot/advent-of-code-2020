
def parse_input():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    return [(
            x[:7].replace('F', '0').replace('B', '1'),
            x[7:].replace('L', '0').replace('R', '1')
        ) for x in data]

def get_seat_id(seat):
    row = int(seat[0], 2)
    col = int(seat[1], 2)
    return (row * 8) + col

print(max([get_seat_id(x) for x in parse_input()]))
