
import common.file_parser as fp

def part1(instructions):
    signal_strengths = {}
    cycles = [20,60,100,140,180,220]

    cycle_count = 1
    x = 1
    for instruction in instructions:
        checks = [cycle_count-1, cycle_count, cycle_count+1]
        found_item = [x for x in checks if x in cycles]
        #print(instruction, x, cycle_count)

        if len(found_item) > 0:
            if found_item[0] not in signal_strengths:
                strength = x * found_item[0]
                signal_strengths[found_item[0]] = strength
        # if cycle_count in cycles:
        #     signal_strengths[cycle_count] = x * cycle_count

        if instruction == 'noop': 
            cycle_count += 1
        else: 
            _, num = instruction.split(' ')
            print(cycle_count, x, num)
            # if (cycle_count+1) in cycles:
            #     signal_strengths[cycle_count+1] = x * cycle_count
            x += int(num)
            cycle_count += 2


    print(signal_strengths)
    return sum(signal_strengths.values())

def print_pixel(sprite, print_len):
    if print_len in sprite:
        print('#',end='')
    else:
        print('.',end='')
    if print_len == 39:
        print()
        return 0
    
    return print_len + 1


def part2(instructions):
    cycles = [20,60,100,140,180,220]
    signal_strength = {}
    x = 1
    cycle_count = 1
    x_start = 1
    x_end = 1
    sprite = range(3)
    print_len = 0

    for instruction in instructions:
        if instruction == 'noop': 
            cycle_count += 1
            print_len = print_pixel(sprite, print_len)
        else: 
            _, num = instruction.split(' ')
            if cycle_count in cycles:
                signal_strength[cycle_count] = x * cycle_count

            cycle_count += 1
            print_len = print_pixel(sprite, print_len)

            if cycle_count in cycles:
                signal_strength[cycle_count] = x * cycle_count

            cycle_count += 1
            print_len = print_pixel(sprite, print_len)

            x += int(num)
            if cycle_count in cycles:
                signal_strength[cycle_count] = x * cycle_count
            sprite = range(x-1, x+2)
            

    # print(signal_strength)
    return sum(signal_strength.values())

sample = fp.read_file_stripped('input/day10_sample.txt')
full = fp.read_file_stripped('input/day10.txt')

"""
 20th, 60th, 100th, 140th, 180th, and 220th
"""

# t = 20
# print(20%20)
# print(19%20)
# print(21%20)

# print(int(60/20)%3)
# print(int(61/20)%3)
# print(int(59/20)%3)
# print(int(40/20)%3)



# assert part1(sample) == 13140
# print(part1(full))

part2(full)
# assert part2(sample) == 13140
