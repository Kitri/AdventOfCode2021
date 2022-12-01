
import common
import numpy as np
import functools
from datetime import datetime
from collections import Counter
from collections import defaultdict

from common import read_file

daynum = 14 # set to number

def interpret_input(input_text):
    polymer_template = input_text[0]
    pair_insertion_rules ={} 

    for line in input_text[2:]:
        x,y = line.split(' -> ')
        pair_insertion_rules[x.rstrip()] = y
    

    return polymer_template, pair_insertion_rules

def step_insertion(template, insertion_rules):
    new_template = ''

    for i in range(len(template) - 1):
        pair = template[i:i+2]
        new_template += template[i] + insertion_rules[pair]
            
    new_template += template[-1]

    return new_template

def setup_counter(template, insertion_rules):
    insertion_counts = {x:0 for x,y in insertion_rules.items()}

    for i in range(len(template) - 1):
        pair = template[i:i+2]
        insertion_counts[pair] += 1

    return insertion_counts

def get_unique_letters(insertion_rules):
    ul = set()
    for i,j in insertion_rules.items():
        ul.add(i[0])
        ul.add(i[1])
        ul.add(j)

    return ul

def count_letters(first_letter, last_letter, unique_letters, current_counts):
    letters = { x:0 for x in unique_letters }
    
    counts_lg_0 = {x:y for x,y in current_counts.items() if y > 0}
    for a,b in counts_lg_0.items():
        letters[a[0]] += b
        letters[a[1]] += b

    count_halves = { i:int(j/2) for i,j in letters.items() }
    count_halves[last_letter] += 1
    count_halves[first_letter] += 1

    return count_halves 

def get_overlaping_letters(counts, unique_letters):
    ab = []
    overlap_differences = { x:0 for x in unique_letters } 
    for x,y in counts.items():
        a,b = x
        for i in range(y):
            ab.append([a,b])

    np_ab = np.array(ab)
    x_counts = Counter(np_ab[:,0])
    y_counts = Counter(np_ab[:,1])

    for letter in unique_letters:
        if(letter in x_counts and letter in y_counts):
            overlap_differences[letter]= abs(x_counts[letter] - y_counts[letter])
   
    print(f'overlaps {overlap_differences}')


def step_insertion_p2(template, insertion_rules, iterations):
    unique_letters = get_unique_letters(insertion_rules)
    new_pairs = {}
    for a,b in insertion_rules.items():
        p = [a[0] + b, b + a[1]]
        new_pairs[a] = p

    insertion_counts = setup_counter(template, insertion_rules)

    # {'N': 2, 'C': 2, 'B': 2, 'H': 1}
    # expected = []
    # expected.append({'B': 2, 'C': 2,   'N': 2 , 'H': 1})
    # expected.append({'B': 6, 'C': 4,   'N': 2 , 'H': 1})
    # expected.append({'B': 11, 'C': 5,  'N': 5 , 'H': 4})
    # expected.append({'B': 23, 'C': 10, 'N': 11, 'H': 5})
    counts = {}
    for i in range(iterations):
        current_counts = insertion_counts.copy()
        counts_lg_0 = {x:y for x,y in current_counts.items() if y > 0}
        for x,y in counts_lg_0.items():
            current_counts[x] -= y # decrease split
            split_pairs = new_pairs[x]
            for p in split_pairs:
                # print(f'{p} {y}')
                current_counts[p] += y
        insertion_counts = current_counts.copy()
        current_counts.clear()
        # print(','.join([f'{x} {y}' for x,y in insertion_counts.items() if y > 0]))
        counts = count_letters(template[0], template[-1], unique_letters, insertion_counts)
        # print(f'Expected {expected[i]}')

    return counts

def calculate_result(template):
    cnts = Counter(template).values()
    return max(cnts) - min(cnts)
    
def part1_sample(input_arr):
    template, insertion_rules = input_arr

    for i in range(10):
        template = step_insertion(template, insertion_rules)

    return calculate_result(template)


def part1(input_arr):
    template, insertion_rules = input_arr

    for i in range(10):
        template = step_insertion(template, insertion_rules)

    return calculate_result(template)

def part2_sample(input_arr):
    template, insertion_rules = input_arr

    counts = step_insertion_p2(template, insertion_rules, 40)
    # print(counts)
    cnt_vals = counts.values()
 
    diffs =  max(cnt_vals) - min(cnt_vals)
    return diffs

def part2(input_arr):
    template, insertion_rules = input_arr

    counts = step_insertion_p2(template, insertion_rules, 40)
    # print(counts)
    cnt_vals = counts.values()
 
    diffs =  max(cnt_vals) - min(cnt_vals)
    return diffs

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
day = interpret_input(day_input)

# p1s = part1_sample(sample)
# print(p1s)
# print(f"Time taken: {datetime.now() - starttime}")

# p1 = part1(day)
# print(p1)
# print(f"Time taken: {datetime.now() - starttime}")

# p2s = part2_sample(sample)
# print(p2s)
# print(f"Time taken: {datetime.now() - starttime}")
    
print('Part 2')
p2 = part2(day)
# print(p2)
print(f"Time taken: {datetime.now() - starttime}")
