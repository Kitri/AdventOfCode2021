from common import file_parser as fp
import bisect

def create_cave_from_input(input_list):
    cave = {}
    for line in input_list:
        coord_list = [x for x in line.split(' -> ')]

        splits = [c.split(',') for c in coord_list]
        coords = [(int(x), int(y)) for x,y in splits]
        for i in range(1,len(coords)):
            y1, x1 = coords[i-1]
            y2, x2 = coords[i]
            if y1 == y2:
                if y1 not in cave:
                    cave[y1] = []
                x_range = range(x1, x2+1) if x2 > x1 else range(x2, x1+1)
                for x_i in x_range:
                    if x_i not in cave[y1]:
                        bisect.insort_right(cave[y1], x_i)
            elif x1 == x2:
                y_range = range(y1, y2+1) if y2 > y1 else range(y2, y1+1)
                for y_i in y_range:
                    if y_i not in cave:
                        cave[y_i] = []
                    if x1 not in cave[y_i]:
                        bisect.insort_right(cave[y_i], x1)
    
    x_max = 0
    x_min = 9999
    for _, x in cave.items():
        if len(x) > 0:
            if x[0] < x_min:
                x_min = x[0]
            if x[-1] > x_max:
                x_max = x[-1]

    return (cave,x_min,x_max)

def next_blocked_down(x: int,y: int, cave: dict):
    row = cave.setdefault(y, [])
    if len(row) == 1:
        if x < row[0]:
            return row[0]
    for col in row:
        if col > x:
            return col

    return -1

def is_blocked(x,y,cave):
    row = cave.setdefault(y, [])
    return x in row

def print_cave(walls, cave):
    y_min = min(cave.keys())
    y_max = max(cave.keys())
    x_max = 0
    x_min = 9999
    for _, x in cave.items():
        if len(x) > 0:
            if x[0] < x_min:
                x_min = x[0]
            if x[-1] > x_max:
                x_max = x[-1]

    for j in range(x_min-2, x_max+3):
        for i in range(y_min-1, y_max+2):
            if i in walls and j in walls[i]:
                print('#', end='')
            elif i in cave and j in cave[i]:
                print('o',end='')
            else:
                print('.', end='')
        print('')

def move_sand(cave: dict, has_floor: bool = False, max_x: int = 0):
    rest_counter = 0
    start_x = 0
    start_y = 500

    pos_x = start_x
    pos_y = start_y

    # for i in range(0,10000):
    while(True):
        pos_x = next_blocked_down(pos_x, pos_y, cave)
        is_floor = False
        # print('Next D', pos_x)
        if pos_x == -1:
            if has_floor:
                pos_x = max_x + 2
                is_floor = True
            else: 
                break
        
        if is_blocked(pos_x, pos_y-1, cave) or is_floor:
            if is_blocked(pos_x, pos_y+1, cave) or is_floor:
                pos_x -= 1 #rest one level above blocked
                # print('come to rest', pos_x, pos_y)
                bisect.insort_right(cave[pos_y], pos_x)
                rest_counter += 1
                if (pos_x == start_x) and (pos_y == start_y):
                    # print('ending')
                    break
                # go to next sand
                pos_x = start_x
                pos_y = start_y
                # print_cave(cave)
            else:
                # print('right not blocked')
                pos_y += 1
        else:
            # print('left not blocked')
            pos_y -= 1
    
    return cave,rest_counter

def part1(input_list):
    cave,min_x,max_x = create_cave_from_input(input_list)
    print(min_x, max_x)
    new_cave, rest_counter = move_sand(cave)

    walls = create_cave_from_input(input_list)
    print_cave(walls, new_cave)
    return rest_counter

def part2(input_list):
    cave,min_x,max_x = create_cave_from_input(input_list)
    new_cave, rest_counter = move_sand(cave, True, max_x)

    walls = create_cave_from_input(input_list)
    # print_cave(walls, new_cave)
    print(rest_counter)

    return rest_counter


sample = fp.read_file_stripped('input/day14_sample.txt')
full = fp.read_file_stripped('input/day14.txt')

# print(part1(full)) #625
part2(full)

# two plus the highest y coordinate