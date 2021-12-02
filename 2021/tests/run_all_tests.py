import tests.unittests
import tests.maintests
import common

#from tests.unittests import UnitTests
#from tests.maintests import MainTests
from common import get_df_from_file, read_file

import importlib
importlib.reload(common)
importlib.reload(tests.unittests)
importlib.reload(tests.maintests)

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
    day3_input = read_file('input/day3_sample.txt')
    # day3_input = read_file('input/day3.txt')
    MainTests.day3_part1(day3_input)
    MainTests.day3_part2(day3_input)

#run_day1_tests()
#run_day2_tests()
run_day3_tests()
