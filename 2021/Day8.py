import common
import numpy as np
import functools
from datetime import datetime

from common import read_file

def sortletters(pattern):
    sort = sorted(pattern)

    return "".join(sort)


def interpret_input(input_text):
    signals = [x.split(' | ') for x in input_text]

    return signals

def count_unique_segments_in_output(signals):
    unique_segments = [segments[1], segments[4], segments[7], segments[8]]
    count = 0
    
    for line in signals:
        pattern = line[0]
        output = line[1]

        o = output.split(' ')
        lengths = [len(x) for x in o]
        filtered = [x for x in lengths if x in unique_segments]
        count += len(filtered)

    return count


    
def get_results(pattern):
    mappy = {}
    len6 = []
    len5 = []

    for p in pattern:
        length = len(p)
        if(length == 2):
            mappy[1] = p
        elif(length == 4):
            mappy[4] = p
        elif(length == 3):
            mappy[7] = p
        elif(length == 7):
            mappy[8] = p
        elif(length == 6):
            len6.append(p)
        elif(length == 5):
            len5.append(p)
            
    # deduce 9
    for p in len6:
        fours = [x for x in mappy[4] if x not in p]
        sevens = [x for x in mappy[7] if x not in p]
        if(len(fours) == 0 and len(sevens) == 0):
            mappy[9] = p
            len6.remove(p)
            break
    # deduce 5
    nine_not_seven = [x for x in mappy[9] if x not in mappy[7]]
    for p in len5:
        match = [x for x in p if x in nine_not_seven]
        if(len(match) == 3):
            mappy[5] = p
            len5.remove(p)
            break
    
    for p in len6:
        match = [x for x in p if x not in mappy[5]]
        if(len(match) == 1):
            mappy[6] = p
        elif(len(match) == 2):
            mappy[0] = p

    for p in len5:
        match = [x for x in p if x in mappy[9]]
        if(len(match) == 4):
            mappy[2] = p
        elif(len(match) == 5):
            mappy[3] = p

    final_map = {}
    for (num, pattern) in mappy.items():
        sorted_pattern = sortletters(pattern)

        final_map[sorted_pattern] = num

    return final_map
    
def part1_sample(signals):
    expected_outputs = [
        [7,4],
        [3,7,2],
        [2,2,3],
        [2],
        [4,7,3],
        [7,4,2,7],
        [4,4,7],
        [2],
        [7,3,2,3],
        [4,2]
    ]

    return count_unique_segments_in_output(signals)

def part1(signals):
    return count_unique_segments_in_output(signals)

def part2_sample(signals):
    final_sum = 0
    for signal in signals:
        pattern = signal[0].split(' ')
        codes = signal[1].split(' ')
        
        mappy = get_results(pattern)
        final_code = ''
        for code in codes:
            sort_code = sortletters(code)
            final_code += str(mappy[sort_code])
        final_sum += int(final_code)

    return final_sum

def part2(signals):
    final_sum = 0
    for signal in signals:
        pattern = signal[0].split(' ')
        codes = signal[1].split(' ')
        
        mappy = get_results(pattern)
        final_code = ''
        for code in codes:
            sort_code = sortletters(code)
            final_code += str(mappy[sort_code])
        final_sum += int(final_code)

    return final_sum

starttime = datetime.now()

day8_sample = read_file('input/day8_sample.txt')
day8_input = read_file('input/day8.txt')

sample = interpret_input(day8_sample)
day8 = interpret_input(day8_input)

p1s = part1_sample(sample)
print(p1s)
print(f"Time taken: {datetime.now() - starttime}")

p1 = part1(day8)
print(p1)
print(f"Time taken: {datetime.now() - starttime}")
# 
p2s = part2_sample(sample)
print(p2s)
print(f"Time taken: {datetime.now() - starttime}")

p2 = part2(day8)
print(p2)
print(f"Time taken: {datetime.now() - starttime}")
