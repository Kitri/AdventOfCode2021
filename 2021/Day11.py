import common
import numpy as np
import functools
from datetime import datetime

from common import read_file

daynum = 11 # set to number

def interpret_input(input_text):
    arr = []
    for line in input_text:
       arr.append([int(x) for x in line]) 

    return np.array(arr)

def index_out_of_bound(x,y,rows,cols):
    return x < 0 or x >= cols or y < 0 or y >= rows 
    

def fill_flashes(octopuses, x, y):
    rows = octopuses.shape[0]
    cols = octopuses.shape[1]
    print(f'{y} {x}')
    print(octopuses)
    if(index_out_of_bound(x, y, rows, cols) or octopuses[y,x] >= 20):
        return octopuses
    else:
        if(octopuses[y,x] >= 9 and octopuses[y,x] < 50):
            octopuses[y,x] = 0
            if(x > 0):
                octopuses[y, x - 1] += 1
            if(x < cols-1):
                octopuses[y, x + 1] += 1
            if(y > 0):
                octopuses[y - 1, x] += 1
            if(y < rows-1):
                octopuses[y + 1, x] += 1
            # diagonals

            if(y >0 and x > 0):
                octopuses[y - 1, x - 1] += 1
            if( y < rows - 1 and x < cols - 1):
                octopuses[y + 1, x + 1] += 1
            if(y < rows - 1 and x > 0):
                octopuses[y + 1, x - 1] += 1
            if(x < cols - 1 and y > 0):
                octopuses[y - 1, x + 1] += 1 
                
        octopuses[y,x] += 50
        if(octopuses[y,x] > 59):
            octopuses[y,x] -= 50
        
        fill_flashes(octopuses, y, x - 1)
        fill_flashes(octopuses, y, x + 1)
        fill_flashes(octopuses, y - 1, x)
        fill_flashes(octopuses, y + 1, x)
        return octopuses
    
def one_iteration(octopuses, flashed):
    rows = octopuses.shape[0]
    cols = octopuses.shape[1]
    for y, x in np.ndindex(octopuses.shape):
#        print(f'{y} {x}')
#        print(octopuses)
        if(octopuses[y,x] > 9):
            octopuses[y,x] = 0
            flashed.add((y,x))
            if(x > 0):
                octopuses[y, x - 1] += 1
            if(x < cols-1):
                octopuses[y, x + 1] += 1
            if(y > 0):
                octopuses[y - 1, x] += 1
            if(y < rows-1):
                octopuses[y + 1, x] += 1
            # diagonals

            if(y >0 and x > 0):
                octopuses[y - 1, x - 1] += 1
            if( y < rows - 1 and x < cols - 1):
                octopuses[y + 1, x + 1] += 1
            if(y < rows - 1 and x > 0):
                octopuses[y + 1, x - 1] += 1
            if(x < cols - 1 and y > 0):
                octopuses[y - 1, x + 1] += 1 

    # print(flashed)
    for i,j in flashed:
        octopuses[i,j] = 0
    
    return octopuses

def step(input_octopuses):
    flashed = set()
    flash_count = 0
    for y, x in np.ndindex(input_octopuses.shape):
        input_octopuses[y,x] +=1 
    while((input_octopuses > 9).sum() > 0):
        input_octopuses = one_iteration(input_octopuses, flashed)
        # print(input_octopuses)
    flash_count += len(flashed)
    flashed.clear()
    return flash_count
    

def test_sm():
    sm_sample = np.array([[1,1,1,1,1],
                       [1,9,9,9,1],
                       [1,9,1,9,1],
                       [1,9,9,9,1],
                       [1,1,1,1,1]])

    total_flashes = 0

    for i in range(2):
        total_flashes += step(sm_sample)

    print(total_flashes)
    return total_flashes

def part1_sample(input_arr):
    total_flashes = 0

    for i in range(100):
        total_flashes += step(input_arr)
    print(input_arr)

    return total_flashes

def part1(input_arr):
    total_flashes = 0

    for i in range(100):
        total_flashes += step(input_arr)

    return total_flashes

def part2_sample(input_arr):
    total_flashes = 0

    counter = 0
    while((input_arr == 0).sum() != input_arr.size):
        total_flashes += step(input_arr)
        counter += 1
    print(counter)
    print(input_arr)

    return counter

def part2(input_arr):
    total_flashes = 0

    counter = 0
    while((input_arr == 0).sum() != input_arr.size):
        total_flashes += step(input_arr)
        counter += 1
    print(counter)
    print(input_arr)

    return counter

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
day = interpret_input(day_input)

sm = test_sm()
print(sm)

p1s = part1_sample(sample)
print(p1s)
print(f"Time taken: {datetime.now() - starttime}")

p1 = part1(day)
print(p1)
print(f"Time taken: {datetime.now() - starttime}")

p2s = part2_sample(sample)
print(p2s)
print(f"Time taken: {datetime.now() - starttime}")
   
p2 = part2(day)
print(p2)
print(f"Time taken: {datetime.now() - starttime}")
