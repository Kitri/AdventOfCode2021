import common
import datetime
from common import read_file

def interpret_input(txt):
    nums = txt[0].split(',')
    if(len(txt) != 1):
        print(f'more than one line {len(nums)}')

    return [int(x) for x in nums]

# Leaving for bitter memories when I still tried to read in the whole array into memory
def create_verification_list():
    days = read_file('input/day6_sample_verification.txt')
    fish_per_day = []
    for day in days:
        fish = day.split(',')
        nums = [int(x) for x in fish]
        fish_per_day.append(nums)

    return fish_per_day


def calculate_for_num(num, iterations):
    counter = 0
    num_counts = {}
    for i in range(-1,9):
        num_counts[i] = 0

    num_counts[num] = 1
    for i in range(0, iterations):
        children_spawn = 0
        for j in range(-1,8):
            num_counts[j] += num_counts[j+1]
            num_counts[j+1] = 0
        num_counts[8] += num_counts[-1]
        num_counts[6] += num_counts[-1]
        num_counts[-1] = 0

    for (x,y) in num_counts.items():
        counter += y
        
    return counter

def precalculate_numbers(iterations):
    numbers = {} 

    for i in range(1,6):
        numbers[i] = calculate_for_num(i, iterations)

    return numbers

def test_with_sample(input_text):
    numbers = precalculate_numbers(80)  

    counter = 0
    for num in input_text:
        counter += numbers[num] 
    print(counter)

    assert counter == 5934, f"Error, got {counter}"
    
def part2(input_text):
    numbers = precalculate_numbers(256)  

    counter = 0
    for num in input_text:
        counter += numbers[num] 

    return counter
    
    
    
day6_sample = read_file('input/day6_sample.txt')
sample = interpret_input(day6_sample)

day6_input = read_file('input/day6.txt')
day6 = interpret_input(day6_input)

print(datetime.datetime.now())

test_with_sample(sample)

print(datetime.datetime.now())

result = part2(day6)
print(result)

print(datetime.datetime.now())
    

