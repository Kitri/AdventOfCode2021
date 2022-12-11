import common.file_parser as fp
import numpy as np

# get length of row and column, add to sum (outer edge)
# start at [1][1]
# keep track of highest number to the left as you go
# traverse up to first higher number up, down, right
# store that number
# next time compare to highest number instead
# if current num == highest num, search right again
def parse_input(input_list):
    return np.array([[int(y) for y in x] for x in input_list])

def investigate_tree_house(input_list,mode):
    visible_counter = 0
    input_ints = parse_input(input_list)
    len_row,len_col = input_ints.shape

    visible_counter += (len_row*2) + (len_col*2) - 4 # corners
    max_scene = 0

    for (row_idx,col_idx), x in np.ndenumerate(input_ints):
        scenic_score = 0
        if row_idx > 0 and col_idx > 0 and row_idx < len_row-1 and col_idx < len_col-1:
            visible_right, dir_right = is_visible(x, input_ints[row_idx,col_idx+1:]) 
            visible_up, dir_up = is_visible(x,input_ints[:row_idx,col_idx][::-1]) 
            visible_left, dir_left = is_visible(x, input_ints[row_idx,:col_idx][::-1]) 
            visible_down, dir_down = is_visible(x,input_ints[row_idx+1:,col_idx]) 

            scenic_score = dir_right * dir_up * dir_left * dir_down
            if visible_right or visible_left or visible_down or visible_up:
                visible_counter += 1

        if scenic_score > max_scene:
            max_scene = scenic_score

    return visible_counter if mode == 1 else max_scene

def is_visible(num, line):
    max_view = len(line) # if direction == -1 else len(line)
    for idx,_ in enumerate(line):
        # print('comparing', num, line[idx])
        if num <= line[idx]:
            # print('B',num, line, idx+1)
            return (False, idx+1)
    
    # print('V',num,line, max_view)
    return (True, max_view)

sample = fp.read_file_stripped('input/day8_sample.txt')
full = fp.read_file_stripped('input/day8.txt')

print('part1', investigate_tree_house(full,1))
print('part2', investigate_tree_house(full,2))