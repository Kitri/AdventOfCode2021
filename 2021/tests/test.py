import submarine
import common
from common import get_df_from_file, read_file
import importlib
importlib.reload(submarine)
importlib.reload(common)


class MainTests:
    def day1_part1(df):
        df_sweep = sonar_sweep_basic(df)
        increases_basic = calculate_number_of_sea_floor_depth_increases(df_sweep)
        expected_basic_increases = 1482
    
        assert increases_basic == expected_basic_increases, f"Basic Increases should be {expected_basic_increases}, found {increases_basic}" 

    def day1_part2(df):
        df_sw_sweep = sonar_sweep_sliding_window(df)
        increases_window = calculate_number_of_sea_floor_depth_increases(df_sw_sweep)
        expected_window_increases = 1518
    
        assert increases_window == expected_window_increases, f"Window Increases should be {expected_window_increases}, found {increases_window}" 
    
    
    def day2_part1(instructions):
        submarine = Submarine(0,0,0)
    
        for instruction in instructions:
            submarine.dive_deprecated(instruction)
    
        calculation = submarine.depth * submarine.horizontal_position

        expected_result = 1561344
    
        assert calculation == expected_result, f"Depth * position expected to be {expected_result}, but found {calculation}"
    
    def day2_part2(instructions):
        submarine = Submarine(0,0,0)
    
        for instruction in instructions:
            submarine.dive(instruction)
    
        calculation = submarine.depth * submarine.horizontal_position

        expected_result = 1848454425
    
        assert calculation == expected_result, f"Depth * position expected to be {expected_result}, but found {calculation}"

    
    def day3_part1(x):
        result = 1
        expected_result = 1
        assert result == expected_result, f"Expected {expected_result}, but found {result}"

    def day3_part2(x):
        result = 1
        expected_result = 1
        assert result == expected_result, f"Expected {expected_result}, but found {result}"

    def test_template(x):
        result = 1
        expected_result = 1
        assert result == expected_result, f"Expected {expected_result}, but found {result}"




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

# run_day1_tests()
# run_day2_tests()
run_day3_tests()

