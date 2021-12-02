
import tests.test
import importlib
#importlib.reload(tests)
#importlib.reload(common)

def day1():
    day1_input = get_df_from_file('input/Day1.txt', None, ['depth'])


    test.given_day1_input_increases_should_be_1482(day1_input)
    test.given_day1_input_sliding_window_sum_increases_should_be_1518(day1_input)


def day2():
    day2_input = read_file('input/Day2.txt')
    test.given_day2_part1_input_dive_calculation_should_be_x(day2_input)
    test.given_day2_part2_input_dive_calculatpyion_should_be_x(day2_input)

def main():
    day1()
    day2()
    

if __name__ == '__main__':
    main()
