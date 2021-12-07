import common
import numpy as np
import functools

from common import read_file

def interpret_input(input_text):
    if(len(input_text) != 1):
        print('Error, more than one line')
    nums = input_text[0].split(',')
    num_ints = [int(x) for x in nums]
    np_arr = np.array(num_ints)

    return np.sort(np_arr)

def determine_fuel(numbers, chosen_one):
    fuel = 0
    for num in numbers:
        fuel += abs(num-chosen_one)

    return fuel

@functools.lru_cache(2048)
def triangular_number(n):
    return n * (n + 1) // 2 

def determine_fuel_part2(numbers, chosen_one):
    fuel = 0
    for num in numbers:
        diffs = abs(num-chosen_one)
        summy = triangular_number(diffs)
        fuel += summy

    return fuel

def get_middle_min_max(numbers, firstelem, lastelem):
    min_fuel = determine_fuel(numbers, firstelem) 
    max_fuel = determine_fuel(numbers, lastelem) 

    return (min_fuel + max_fuel) / 2

def get_min_fuel(numbers):
    unique_numbers = np.unique(numbers)
    current_min = (-1, 99999999) #num, fuel

    avg_fuel = get_middle_min_max(numbers, unique_numbers[0], unique_numbers[-1])
    
    counter = 0
    for num in unique_numbers:
        fuel = determine_fuel(numbers, num)
        if(fuel < current_min[1]):
            current_min = (num, fuel)

        if(fuel > avg_fuel):
            break

        # print(f"{num}: {fuel}")

    return current_min
# 1981

def get_min_fuel_part2(numbers):
    unique_numbers = np.unique(numbers)
    current_min = (-1, 1255853683) #num, fuel
    
    for num in unique_numbers:
        fuel = determine_fuel_part2(numbers, num)
        if(fuel < current_min[1]):
            current_min = (num, fuel)
        # print(f"{num}: {fuel}")

    return current_min
        

def part1(numbers):
    min_fuel = get_min_fuel(numbers)

    return min_fuel

def part2(numbers):
    min_fuel = get_min_fuel_part2(numbers)

    return min_fuel

day7_sample = read_file('input/day7_sample.txt')
day7_input = read_file('input/day7.txt')

sample = interpret_input(day7_sample)
day7 = interpret_input(day7_input)

min_fuel_sample = get_min_fuel(sample)
# print(min_fuel_sample)

min_fuel_sample_2 = get_min_fuel_part2(sample)
#print(fuel)

import datetime
print(datetime.datetime.now())
result = part1(day7)
print(result)
# 356958
print(datetime.datetime.now())

result2 = part2(day7)
print(result2)
# 105461913
print(datetime.datetime.now())
