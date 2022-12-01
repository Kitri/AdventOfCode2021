import common
import numpy as np
import functools
from datetime import datetime

from collections import defaultdict

from common import read_file

daynum = 13 # set to number

def interpret_input(input_text):
    
    folds = []
    grid = []
    for line in input_text:
        if('fold' in line):
            # instr = line.split(' ')
            # pos, num = instr[2].split('=')
            # folds.append((pos,num))
            folds.append(line)
        elif(',' in line):
            grid.append(line)
            # print(line)
            # x, y = line.split(',')
            # coord = [y, x]
            # grid.append(coord)

    all_folds = []
    for fold in folds:
        instructions = fold.split(' ')
        x,y = instructions[2].split('=')
        all_folds.append((x,int(y)))
    
    all_coords = []
    for coord in grid:
        x,y = coord.split(',')
        all_coords.append((int(x),int(y)))
            
    return all_folds,all_coords

def fold_y(grid, fold_coord):
    above_line = [(x,y) for x,y in grid if y < fold_coord]
    below_line = [(x,y) for x,y in grid if y > fold_coord]

    new_grid = set(above_line)
    for x,y in below_line:
        distance_from_line = y - fold_coord
        new_y = fold_coord - distance_from_line 
        new_grid.add((x,new_y))

    return new_grid

def fold_x(grid, fold_coord):
    left_line = [(x,y) for x,y in grid if x < fold_coord]
    right_line = [(x,y) for x,y in grid if x > fold_coord]

    new_grid = set(left_line)
    for x,y in right_line:
        distance_from_line = x - fold_coord
        new_x = fold_coord - distance_from_line 
        new_grid.add((new_x,y))

    return new_grid

def iterate_folds(folds, grid):
    new_grid =[]
    new_grid.append(grid)
    for i, fold in enumerate(folds):
        if(fold[0] == 'y'):
            new_grid.append(fold_y(new_grid[i], fold[1]))
        else:
            new_grid.append(fold_x(new_grid[i], fold[1]))

    return new_grid
    # [print(len(g)) for g in new_grid]
    
def test(input_arr):
    folds = input_arr[0]
    grid = input_arr[1]

    new_grid = iterate_folds(folds, grid)

    [print(len(g)) for g in new_grid]

def print_grid(grid, max_x, max_y):
    for y in range(max_y): # get max x
        line = ''
        for x in range(max_x): # get max y
            if((x,y) in grid):
                line += '#'
            else:
                line += '.'
        print(line)
def find_maxes(grid):
    max_x = 0
    max_y = 0

    for x,y in grid:
        if(x > max_x):
            max_x = x
        if(y > max_y):
            max_y = y
    
    return (max_x, max_y)
    

def part1_sample(input_arr):
    folds = input_arr[0]
    grid = input_arr[1]

    new_grid = iterate_folds(folds, grid)

    [print(len(g)) for g in new_grid]
    return new_grid

def part1(input_arr):
    folds = input_arr[0]
    grid = input_arr[1]
    print(f'size: {len(grid)}')

    new_grid = iterate_folds(folds, grid)

    [print(len(g)) for g in new_grid]
    return new_grid

def part2_sample(input_arr):
    folds = input_arr[0]
    grid = input_arr[1]

    new_grid = iterate_folds(folds, grid)
    for g in new_grid:
        max_x, max_y = find_maxes(g)
        # print(f'{max_x} {max_y}')
        print(len(g))
        print_grid(g, max_x+1, max_y+1)
        print('-----')
            
    return new_grid

def part2(input_arr):
    folds = input_arr[0]
    grid = input_arr[1]

    new_grid = iterate_folds(folds, grid)
            
    max_x, max_y = find_maxes(new_grid[-1])
    print_grid(new_grid[-1], max_x+1, max_y+1)
    return new_grid

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
day = interpret_input(day_input)

# test(sample)

p1s = part1_sample(sample)
# print(p1s)
print(f"Time taken: {datetime.now() - starttime}")

p1 = part1(day)
# print(p1)
print(f"Time taken: {datetime.now() - starttime}")

p2s = part2_sample(sample)
print(p2s)
print(f"Time taken: {datetime.now() - starttime}")
    
p2 = part2(day)
# print(p2)
print(f"Time taken: {datetime.now() - starttime}")
