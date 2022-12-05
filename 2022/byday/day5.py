from collections import deque

def parse_input(input_list):
    break_index = input_list.index('\n')
    header, data = [input_list[:break_index-1], input_list[break_index+1:]]
    stripped_header = [h.replace('\n','').replace('[','').replace(']','').replace("    ",' ') for h in header]
    header_lists = [sh.split(' ') for sh in stripped_header]
    stack_length = len(header_lists[0])
    moves = [[int(x[1]),int(x[3])-1,int(x[5])-1] for x in (d.strip().split(' ') for d in data)]

    #initialise stacks
    crates = []
    for _ in range(stack_length):
        crates.append(deque([]))

    # queue stacks in reverse onto stack
    for idx in range(stack_length):
        for item in reversed([row[idx] for row in header_lists]):
            if item != '':
                crates[idx].append(item)

    return (crates, moves)


def part1(input_list):
    input_list = open('input/day5.txt').readlines()

    crates, moves = parse_input(input_list)
    
    # Apply moves (pop off stack, push onto other stack)
    for move in moves:
        move_qty, from_idx, to_idx = move
        for _ in range(move_qty):
            move_item = crates[from_idx].pop()
            crates[to_idx].append(move_item)

    #print final result
    for crate in crates:
        print(crate.pop(),end='')
    
    print()

def part2(input_list):

    crates, moves = parse_input(input_list)

    # Apply moves (move full crates - add to list and push in reverse)
    for move in moves:
        move_qty, from_idx, to_idx = move

        stack_moves = [crates[from_idx].pop() for _ in range(move_qty)]

        for item in reversed(stack_moves):
            crates[to_idx].append(item)

    #print final result
    for crate in crates:
        print(crate.pop(),end='')
    
    print()

sample = open('input/day5_sample.txt').readlines()
full = open('input/day5.txt').readlines()
part1(full) # MQTPGLLDN
part2(full) # LVZPSTTCZ