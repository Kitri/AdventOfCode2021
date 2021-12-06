import tests.maintests
import tests.unittests
from tests.unittests import UnitTests
import common

#from tests.unittests import UnitTests
#from tests.maintests import MainTests
from common import get_df_from_file, read_file

import importlib
importlib.reload(common)
importlib.reload(tests.maintests)
importlib.reload(tests.unittests)

# Run All
def run_day1_tests():
    day1_input = get_df_from_file('input/day1.txt', None, ['depth'])
    day1_sample_input = get_df_from_file('input/day1_sample.txt', None, ['depth'])
    UnitTests.test_main_sweep(day1_sample_input)
    UnitTests.test_sliding_window_sweep(day1_sample_input)
    MainTests.day1_part1(day1_input)
    MainTests.day1_part2(day1_input)

def run_day2_tests():
    day2_input = read_file('input/day2.txt')
    UnitTests.test_dive_forward()
    UnitTests.test_dive_up()
    UnitTests.test_dive_down()
    MainTests.day2_part1(day2_input)
    MainTests.day2_part2(day2_input)

def run_day3_tests():
    day3_sample = read_file('input/day3_sample.txt')
    day3_input = read_file('input/day3.txt')
    #UnitTests.test_power_consumption(day3_input)
    MainTests.day3_part1(day3_input)
    MainTests.day3_part2(day3_input)

#run_day1_tests()
#run_day2_tests()
#run_day3_tests()


import collections

def get_min_max_binary(bin_array):
    counts = collections.Counter(bin_array)
    ones = counts['1']
    zeros = counts['0']

    if ones < zeros: # less 1s than 0s, means gamma = 0, epsilon = 1
        return ('1','0') # 
    else: # more 1s than 0s = gamma = 1, epsilon 0; equal means gamma = 1 and epsilon 0
        return('0','1')
    
    print(f"{epsilon}, {gamma}")
    
    return (epsilon, gamma)

def test_min_max_with_more_zeros():
    bin_arr = ['0','1','0','0','1']
    result = get_min_max_binary(bin_arr)
    expected_result = ('1','0') # (min,max)

    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_min_max_with_equal_count():
    bin_arr = ['0','1','0','0','1','1']
    result = get_min_max_binary(bin_arr)
    expected_result = ('0','1') # (min,max)

    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_min_and_max_with_more_ones():
    bin_arr = ['0','1','0','1','1']
    result = get_min_max_binary(bin_arr)
    expected_result = ('0','1') # (min,max)

    assert result == expected_result, f"Expected {expected_result}, but got {result}"

day3_sample = read_file('input/day3_sample.txt')
test_min_max_with_more_zeros()
test_min_max_with_equal_count()
test_min_and_max_with_more_ones()
