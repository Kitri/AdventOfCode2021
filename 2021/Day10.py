import common
import numpy as np
import functools
from collections import deque
from datetime import datetime

from common import read_file

daynum = 10 # set to number

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

valid_open_brackets = ['(','[','{','<'] 

valid_bracket_pairs = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

def interpret_input(input_text):

    return input_text

def is_open_bracket(bracket):
    return bracket in valid_bracket_pairs.keys()


def get_closing_bracket(bracket):
    for vb in valid_bracket_pairs.keys():
        if(bracket == vb):
            return valid_bracket_pairs[vb]
    return 'e'
    
def closing_matches_opening(bracket, pbracket):
    closing_bracket = get_closing_bracket(pbracket)
    if(closing_bracket != 'e'):
        return bracket == closing_bracket
    else:
        return False
    

def get_breaking_bracket(brackets):
    bracket_stack = deque()

    for x in brackets:
        if(is_open_bracket(x)):
            bracket_stack.append(x)
        else:
            if(not bracket_stack):
                return scores[x]
            prev_bracket = bracket_stack.pop()
            brackets_match = closing_matches_opening(x, prev_bracket)
            if(not brackets_match):
                return scores[x]

    return 0 

def validate_brackets(brackets):
    bracket_stack = deque()
    closing_brackets = []
    is_error = False

    for x in brackets:
        if(is_open_bracket(x)):
            bracket_stack.append(x)
        else:
            if(not bracket_stack):
                closing_brackets.append(get_closing_bracket(prev_bracket))
            prev_bracket = bracket_stack.pop()
            closing_bracket = get_closing_bracket(prev_bracket)
            brackets_match = closing_matches_opening(x, prev_bracket)
            if(x != closing_bracket):
                is_error = True
                #print('does not match')
                #closing_brackets.append(closing_bracket)

    if(not is_error):
        while(bracket_stack):
            b = bracket_stack.pop()
            c = get_closing_bracket(b)
            closing_brackets.append(c)

    return closing_brackets

def calculate_score(closing_brackets):
    new_scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    final_sum = 0
    for cb in closing_brackets:
        final_sum *= 5
        final_sum += new_scores[cb]

    return final_sum
        
    
def part1_sample(input_arr):
    final_sum = 0
    for brackets in input_arr:
        error_code = get_breaking_bracket(brackets)
        final_sum +=  error_code
        print(error_code)
    
    return final_sum

def part1(input_arr):
    final_sum = 0
    for brackets in input_arr:
        error_code = get_breaking_bracket(brackets)
        final_sum +=  error_code
        print(error_code)
    
    return final_sum

def test_part2():
    error_code = validate_brackets('[({(<(())[]>[[{[]{<()<>>')
    expected_out = ['}','}',']',']',')','}',')',']']
    print(error_code)
    return error_code == expected_out

def test_valid_part2():
    error_code = validate_brackets('{([(<{}[<>[]}>{[]{[(<()>')
    print(error_code)
    return ''

def part2_sample(input_arr):
    sums = []
    for brackets in input_arr:
        closing_brackets = validate_brackets(brackets)
        if(closing_brackets):
            sums.append(calculate_score(closing_brackets))

    sorted_sums = sorted(sums)
    print(sorted_sums)
    mid_el = int(len(sorted_sums)/2)
    return sorted_sums[mid_el]

def part2(input_arr):
    sums = []
    for brackets in input_arr:
        closing_brackets = validate_brackets(brackets)
        if(closing_brackets):
            sums.append(calculate_score(closing_brackets))

    sorted_sums = sorted(sums)
    mid_el = int(len(sorted_sums)/2)
    print(sorted_sums)
    return sorted_sums[mid_el]

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
day = interpret_input(day_input)

# p1s = part1_sample(sample)
# print(p1s)
# print(f"Time taken: {datetime.now() - starttime}")
# 
#p1 = part1(day)
#print(p1)
#print(f"Time taken: {datetime.now() - starttime}")
 
#t2 = test_valid_part2()
#print(t2)
#print(f"Time taken: {datetime.now() - starttime}")

#p2s = part2_sample(sample)
#print(p2s)
#print(f"Time taken: {datetime.now() - starttime}")
     
p2 = part2(day)
print(p2)
print(f"Time taken: {datetime.now() - starttime}")

