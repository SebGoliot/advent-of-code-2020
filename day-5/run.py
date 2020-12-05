
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
    return int((row * 8) + col)

def ordered_ids(input):
    ids = [get_seat_id(x) for x in parse_input()]
    ids.sort()
    return ids

ordered_seat_ids = ordered_ids(parse_input())

print("highest seat id:", max(ordered_seat_ids))

def get_missing_seat_id(ordered_seat_ids):
    for id in range(len(ordered_seat_ids)):
        try:
            if ordered_seat_ids[id+1] != ordered_seat_ids[id] + 1:
                return ordered_seat_ids[id] + 1
        except:
            pass

print("missing seat id:", get_missing_seat_id(ordered_seat_ids))
