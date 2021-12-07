import common
import numpy as np
import functools
from datetime import datetime

from common import read_file

daynum = 0 # set to number

def interpret_input(input_text):
    if(len(input_text) != 1):
        print('Error, more than one line')
    nums = input_text[0].split(',')
    num_ints = [int(x) for x in nums]

    return num_ints

def part1_sample(input_arr):
    return input_arr

def part1(input_arr):
    return len(input_arr)

def part2_sample(input_arr):
    return input_arr

def part2(input_arr):
    return len(input_arr)

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day8_sample)
day = interpret_input(day8_input)

p1s = part1_sample(sample)
print(p1s)
print(f"Time taken: {datetime.now() - starttime}")

p1 = part2(day)
print(p1)
print(f"Time taken: {datetime.now() - starttime}")

p2s = part2_sample(sample)
print(p2s)
print(f"Time taken: {datetime.now() - starttime}")
    
p2 = part2(day)
print(p2)
print(f"Time taken: {datetime.now() - starttime}")
