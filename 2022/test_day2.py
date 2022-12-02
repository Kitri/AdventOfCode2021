
import common_functions as cf
import file_parser as fp
import jungle_navigation as jungle

day = 2
parts = {'1s': 'Part1 Sample', '1f': 'Part1 Full', '2s': 'Part2 Sample', '2f': 'Part2 Full'}

def run_test(func, description, expected):
    answer = cf.run_with_timeprints(func, description)
    print("Answer", answer)
    assert answer == expected, f"Expected {expected} but got {answer}"

def day2_test_sample():
    sample = fp.read_file(f'input/day{day}_sample.txt')
    full = fp.read_file(f'input/day{day}.txt')

    run_test(lambda: jungle.dummy_day2(sample), parts['1s'], 15)
    run_test(lambda: jungle.dummy_day2(full), parts['1f'], 15)

day2_test_sample()