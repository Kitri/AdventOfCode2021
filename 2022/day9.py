
import common.file_parser as fp
from itertools import pairwise

def follow_head2(h_row, h_col, n_row, n_col):
    col_diff = int(h_col - n_col)
    row_diff = (h_row - n_row)

    if abs(col_diff) == 2:
        n_col += int(col_diff/2)
        if abs(row_diff) == 1:
            n_row += row_diff
    if(abs(row_diff)) == 2:
        n_row += int(row_diff/2)
        if abs(col_diff) == 1:
            n_col += col_diff
    

    return (n_row,n_col)

def follow_head(h_row, h_col, n_row, n_col):
    move_horizontal = False
    move_vertical = False

    # to da right
    if h_col - n_col >= 2:
        n_col += 1
        move_horizontal = True
    # torra left
    elif n_col - h_col >= 2:
        n_col -= 1
        move_horizontal = True
    # up
    elif n_row - h_row >= 2:
        n_row -= 1
        move_vertical = True
    # down
    elif h_row - n_row >= 2:
        n_row += 1
        move_vertical = True
    
    if move_horizontal and h_row != n_row:
        n_row = h_row
    
    if move_vertical and h_col != n_col:
        n_col = h_col

    return (n_row, n_col)
            

def move_snake(dir, h_row, h_col):
    match dir:
        case 'R':
            h_col += 1
        case 'L':
            h_col -= 1
        case 'U':
            h_row -= 1
        case 'D':
            h_row += 1
    return (h_row, h_col)

def part1(input_list):
    visited = set([(4,0)])
    h_row, h_col, t_row, t_col = (4,0,4,0)
    for move in input_list:
        dir, num = move.split(' ')
        num = int(num)
        for _ in range(num):
            h_row, h_col = move_snake(dir, h_row, h_col)
            t_row, t_col = follow_head(h_row, h_col, t_row, t_col)
            visited.add((t_row, t_col))
            # print(move, '- Head:', h_row, h_col, ' Tail:', t_row, t_col)
        
    return len(visited)
def print_grid(snake_positions, grid_size):
    for i in range(grid_size):
        for j in range(grid_size):
            if (i,j) in snake_positions:
                print(snake_positions.index((i,j)), end='')
            else:
                print('.',end='')
        print('')
    print('')

def part2(input_list):
    tail_visited = set([(15,11)])
    snake_positions = [(15,11)] * 10

    for move in input_list:
        dir, num = move.split(' ')
        num = int(num)
        for _ in range(num):
            snake_positions[0] = move_snake(dir,*snake_positions[0])
            prev_tail = snake_positions[9]
            for idx in range(1,len(snake_positions)):
                h = snake_positions[idx-1]
                t = snake_positions[idx]
                snake_positions[idx] = follow_head2(h[0], h[1], t[0], t[1])
            if prev_tail != snake_positions[9]:
                tail_visited.add(snake_positions[9])
            # print(dir, snake_positions)
            # print_grid(snake_positions,30)
        # print(move, snake_positions)
        
    return len(tail_visited)

        


sample = fp.read_file_stripped('input/day9_sample2.txt')
full = fp.read_file_stripped('input/day9.txt')

# assert part1(full) == 5779
print(part2(full))

# print(follow_head(15,11,15,11))


"""   7, 16
      8, 16
      9, 16
      10, 16
      11, 16
      11, 15
      12, 14
      13, 13
      14, 12
      15, 11
"""

assert follow_head2(0,1,1,1) == (1,1)
assert follow_head2(0,0,1,1) == (1,1)
assert follow_head2(1,0,1,1) == (1,1)
assert follow_head2(2,0,1,1) == (1,1)
assert follow_head2(2,1,1,1) == (1,1)
assert follow_head2(2,2,1,1) == (1,1)
assert follow_head2(1,2,1,1) == (1,1)
assert follow_head2(0,2,1,1) == (1,1)
assert follow_head2(0,1,2,1) == (1,1)
assert follow_head2(1,0,2,2) == (1,1)
assert follow_head2(0,1,2,2) == (1,1)
assert follow_head2(2,0,2,2) == (2,1)
assert follow_head2(3,0,2,2) == (3,1)
assert follow_head2(4,3,2,2) == (3,3)
assert follow_head2(3,4,2,2) == (3,3)
assert follow_head2(1,4,2,2) == (1,3)
assert follow_head2(0,3,2,2) == (1,3)

# diagonal
assert follow_head2(0,0,2,2) == (1,1)
assert follow_head2(4,0,2,2) == (3,1)
assert follow_head2(0,4,2,2) == (1,3)
assert follow_head2(4,4,2,2) == (3,3)