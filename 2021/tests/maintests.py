import submarine
from submarine import Submarine
import importlib
importlib.reload(submarine)


class MainTests:
    def day1_part1(df):
        df_sweep = submarine.sonar_sweep_basic(df)
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
        result = submarine.calculate_power_consumptions(x) 
        expected_result = 4160394 
        assert result == expected_result, f"Expected {expected_result}, but found {result}"

    def day3_part2(x):
        result = submarine.get_life_support_rating(x)
        expected_result = 4125600
        assert result == expected_result, f"Expected {expected_result}, but found {result}"

    def test_template(x):
        result = 1
        expected_result = 1
        assert result == expected_result, f"Expected {expected_result}, but found {result}"



