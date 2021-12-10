import common
import numpy as np
import functools
from datetime import datetime
from collections import deque

from common import read_file

daynum = 9# set to number

def interpret_input(input_text):
    arr = []
    for line in input_text:
       arr.append([int(x) for x in line]) 

    return np.array(arr)

def is_min_to_adjacent(num, adj):
    # print(f'{num} {adj}')
    for x in adj:
        if(x <= num):
            return False
    return True

def get_the_mins(input_arr):
    y_len = len(input_arr)
    x_len = len(input_arr[0])
    all_the_mins = {} 
    for y, x in np.ndindex(input_arr.shape):
        num = input_arr[y,x]
        adj = []
        if(y != 0):
            adj.append(input_arr[y-1,x])
        if(x != 0):
            adj.append(input_arr[y,x-1])
        if(y != y_len-1):
            adj.append(input_arr[y+1,x])
        if(x != x_len-1):
            adj.append(input_arr[y,x+1])

        if(is_min_to_adjacent(num, adj)):
            all_the_mins[(y,x)] = num

    return all_the_mins
            

def calculate_final_sum(all_the_mins):
    min_nums = [y for (x,y) in all_the_mins.items()]
    return np.sum([(i + 1) for i in min_nums])

def still_in_grid(x,y, rows, cols):
    if(x < 0 or y < 0 or x > cols or y > rows):
        return False
    elif(x == -1 or y == -1 or x == cols or y == rows):
        return False
    else:
        return True
    

def get_basin(input_arr, x, y, basin):
    rows = input_arr.shape[0]
    cols = input_arr.shape[1]
    if(not still_in_grid(x,y, rows, cols)):
       return basin
    if(input_arr[y,x] == 9):
       return basin
    else:
       # print(f"b {basin}")
       basin.add((y,x))
       input_arr[y,x] = 9
       get_basin(input_arr, x+1, y, basin)
       get_basin(input_arr, x, y-1, basin)
       get_basin(input_arr, x-1, y, basin)
       get_basin(input_arr, y+1, x, basin)
       return basin
 
def get_basin_size(input_arr, ix, iy, rows, cols):
    positions = deque([(iy,ix)])
    count = 1
    basin_size = 0

    while(count > 0):
        y,x = positions.pop()
        count -= 1

        if(input_arr[y,x] < 9):
            input_arr[y,x] = 10 # mark as "visited"
            basin_size += 1

            # traverse
            if(y != 0):
                positions.appendleft((y-1,x))
                count += 1
            if(x != 0):
                positions.appendleft((y,x-1))
                count += 1
            if(y != rows-1):
                positions.appendleft((y+1,x))
                count += 1
            if(x != cols-1):
                positions.appendleft((y,x+1))
                count += 1
    return basin_size
    

    
def find_basin(input_arr, mins):
    rows = input_arr.shape[0]
    cols = input_arr.shape[1]
    # print(f"{rows} {cols}")
    # basin = get_basin(input_arr, 6, 4, set([]))
    # print(basin)
    product = 1
    basins = []
    for ((y,x),num) in mins.items():
         basin = get_basin_size(input_arr, x, y, rows, cols)
         basins.append(basin)

         print(basin)


    sorted_basins = sorted(basins)
    print(sorted_basins[-3:])
    
    return np.prod(sorted_basins[-3:]) 

def part1_sample(input_arr):
    x = get_the_mins(input_arr)
    print(x)
    y = calculate_final_sum(x)
    return y

def part1(input_arr):
    x = get_the_mins(input_arr)
    y = calculate_final_sum(x)
    print(x)
    return y

def part2_sample(input_arr):
    mins = get_the_mins(input_arr)
    y = find_basin(input_arr, mins)
    return y 

def part2(input_arr):
    mins = get_the_mins(input_arr)
    y = find_basin(input_arr, mins)
    return y 

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
day = interpret_input(day_input)

# p1s = part1_sample(sample)
# print(p1s)
# print(f"Time taken: {datetime.now() - starttime}")

#p1 = part1(day)
# print(p1)
# print(f"Time taken: {datetime.now() - starttime}")
# 
p2s= part2_sample(sample)
print(p2s)
print(f"Time taken: {datetime.now() - starttime}")
#     
p2 = part2(day)
print(p2)
print(f"Time taken: {datetime.now() - starttime}")
