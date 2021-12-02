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
            print(submarine.depth)
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

class UnitTests:
    def test_main_sweep(df):
        sonar_sweep = sonar_sweep_basic(df)
        sonar_sweep_shape = sonar_sweep.shape
        depth_calc = sonar_sweep["depth_calculation"].sum()

        expected_depth_calc = 64
        expected_df_shape_after_transform = (10,3)

        assert depth_calc == expected_depth_calc, f"Sum of depth differences expected to be {expected_depth_calc}, but found {depth_calc}"
        assert expected_df_shape_after_transform == sonar_sweep_shape, f"Expected df to be {expected_df_shape_after_transform} (rows, cols) but found {sonar_sweep_shape}" 

    def test_sliding_window_sweep(df):
        sonar_sweep = sonar_sweep_sliding_window(df)
        sonar_sweep_shape = sonar_sweep.shape
        depth_sum = sonar_sweep["depth_sum"].sum()
        depth_calc = sonar_sweep["depth_calculation"].sum()

        expected_depth_sum_sum = 5384 
        expected_depth_calc_sum = 185 
        expected_df_shape_after_transform = (10,6)

        # print(sonar_sweep.columns)

        assert depth_sum == expected_depth_sum_sum, f"Sum of depth sums expected to be {expected_depth_sum_sum}, but found {depth_sum}"
        assert depth_calc == expected_depth_calc_sum, f"Sum of depth differences expected to be {expected_depth_calc_sum}, but found {depth_calc}"
        assert expected_df_shape_after_transform == sonar_sweep_shape, f"Expected df to be {expected_df_shape_after_transform} (rows, cols) but found {sonar_sweep_shape}" 

    def test_dive_forward():
        sub = Submarine(depth=-3, horizontal_position=5, aim=2)
        sub.dive('forward 6')

        expected_result = (9, 11, 2)
        result = (sub.depth, sub.horizontal_position, sub.aim)

        assert result == expected_result, f"Forward: expected {expected_result}, got {result}"

    def test_dive_up():
        sub = Submarine(depth=3, horizontal_position=4, aim=5)
        sub.dive('up 3')

        expected_result = (3, 4, 2)
        result = (sub.depth, sub.horizontal_position, sub.aim)

        assert result == expected_result, f"Up: expected {expected_result}, got {result}"

    def test_dive_down():
        sub = Submarine(depth=3, horizontal_position=4, aim=5)
        sub.dive('down 3')

        expected_result = (3, 4, 8)
        result = (sub.depth, sub.horizontal_position, sub.aim)

        assert result == expected_result, f"Down: expected {expected_result}, got {result}"




# Run All
def run_day1_tests():
    day1_input = get_df_from_file('input/day1.txt', None, ['depth'])
    day1_sample_input = get_df_from_file('input/day1_sample.txt', None, ['depth'])
    UnitTests.test_main_sweep(day1_sample_input)
    UnitTests.test_sliding_window_sweep(day1_sample_input)
    MainTests.day1_part1(day1_input)
    MainTests.day1_part2(day1_input)

def run_day2_tests():
    day2_input = read_file('input/day2_sample.txt')
    UnitTests.test_dive_forward()
    UnitTests.test_dive_up()
    UnitTests.test_dive_down()

#run_day1_tests()
run_day2_tests()

