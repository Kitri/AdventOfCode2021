import jungle_navigation as jungle
import file_parser as fp
import common_functions as cf
from functools import partial

def generate_config(day: int, 
        func_part1_sample: callable, 
        func_part1_full: callable, 
        func_part2_sample: callable, 
        func_part2_full: callable):
    return [
        { 'description': f'Day{day} Part1 Sample', 'function': func_part1_sample},
        { 'description': f'Day{day} Part1 Full', 'function': func_part1_full},
        { 'description': f'Day{day} Part2 Sample', 'function': func_part2_sample},
        { 'description': f'Day{day} Part2 Full', 'function': func_part2_full}
    ]

def dummy_function(input: str):
    print(input)
    return input

# Expected_answers = [part1_sample, part1, part2_sample, part2]
def run_tests(day: int, expected_answers: list, *funcs):
    # functions = list(*funcs)
    # functions = funcs + [lambda: dummy_function('Dummy')] * (4 - len(*funcs))

    config = generate_config(
        day,
        *funcs
    )
    
    for idx, c in enumerate(config):
        answer = cf.run_with_timeprints(c['function'], c['description'])
        print("Answer", answer)
        assert answer == expected_answers[idx], f"Expected {expected_answers[idx]} but got {answer}"

def day1_tests():
    expected_answers = [24000, 67450, 45000, 199357]
    sample = fp.read_file('input/day1_sample.txt')
    full = fp.read_file('input/day1.txt')
    run_tests_partial = partial(run_tests, 1, expected_answers)

    print("Method 1")
    run_tests_partial(
            lambda: jungle.get_max_calories(sample, 1),
            lambda: jungle.get_max_calories(full, 1),
            lambda: jungle.get_max_calories(sample, 3),
            lambda: jungle.get_max_calories(full, 3))

    print("Method 2")
    run_tests_partial(
            lambda: jungle.get_max_calories_optimised_array_storage(sample, 1),
            lambda: jungle.get_max_calories_optimised_array_storage(full, 1),
            lambda: jungle.get_max_calories_optimised_array_storage(sample, 3),
            lambda: jungle.get_max_calories_optimised_array_storage(full, 3))

def compare_day1_optimisations():
    full = fp.read_file('input/day1.txt')
    print('Part 1')
    answer = cf.run_with_timeprints(lambda: jungle.get_max_calories_non_optimised(full,1),'Split into list, then sum')
    answer = cf.run_with_timeprints(lambda: jungle.get_max_calories(full,1),'Sum in original iteration')
    answer = cf.run_with_timeprints(lambda: jungle.get_max_calories_optimised_array_storage(full,1),'Optimised + keep only 4 items in array')

    print('Part 2')
    answer = cf.run_with_timeprints(lambda: jungle.get_max_calories_non_optimised(full,3),'Split into list, then sum')
    answer = cf.run_with_timeprints(lambda: jungle.get_max_calories(full,3),'Sum in original iteration')
    answer = cf.run_with_timeprints(lambda: jungle.get_max_calories_optimised_array_storage(full,3),'Optimised + keep only 4 items in array')

def template():
    day = 1
    expected_answers = [
        '',
        '',
        '',
        ''
    ]

    sample = fp.read_file(f'input/day{day}_sample.txt')
    full = fp.read_file(f'input/day{day}.txt')

    config = generate_config(
        day,
        lambda: dummy_function('Part 1 Sample Placeholder'),
        lambda: dummy_function('Part 1 Placeholder'),
        lambda: dummy_function('Part 2 Sample Placeholder'),
        lambda: dummy_function('Part 2 Placeholder')
    )
    for idx, c in enumerate(config):
        answer = cf.run_with_timeprints(c['function'], c['description'])
        print("Answer", answer)
        assert answer == expected_answers[idx], f"Expected {expected_answers[idx]} but got {answer}"



day1_tests()