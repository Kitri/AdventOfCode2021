
import common_functions as cf
import file_parser as fp
import jungle_navigation as jungle
import games as g

descriptions = ['Part1 Sample', 'Part1 Full', 'Part2 Sample','Part2 Full']

def run_test(description, expected, func):
    answer = cf.run_with_timeprints(func, description)
    print("Answer", answer)
    assert answer == expected, f"Expected {expected} but got {answer}"

def read_inputs(day):
    return(fp.read_file(f'input/day{day}_sample.txt'), fp.read_file(f'input/day{day}.txt'))

def dummy_function(input: str):
    print(input)
    return input

def day1_tests():
    expected = [24000, 67450, 45000, 199357]
    sample, full = read_inputs(1)
    params = [ [sample, 1], [full, 1], [sample, 3], [full, 3] ]

    print("Method 1")
    for i, _ in enumerate(expected):
        run_test(descriptions[i], expected[i], lambda: jungle.get_max_calories(*params[i]))

    print("Method 2")
    for i, _ in enumerate(expected):
        run_test(descriptions[i], expected[i], lambda: jungle.get_max_calories_optimised_array_storage(*params[i]))

def compare_day1_optimisations():
    full = fp.read_file('input/day1.txt')
    print('Part 1')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_non_optimised(full,1),'Split into list, then sum')
    cf.run_with_timeprints(lambda: jungle.get_max_calories(full,1),'Sum in original iteration')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_optimised_array_storage(full,1),'Optimised + keep only 4 items in array')

    print('Part 2')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_non_optimised(full,3),'Split into list, then sum')
    cf.run_with_timeprints(lambda: jungle.get_max_calories(full,3),'Sum in original iteration')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_optimised_array_storage(full,3),'Optimised + keep only 4 items in array')

def day2_tests():
    expected = [15, 12156, 12, 10835]
    sample, full = read_inputs(2)
    params = [ [1, sample], [1, full], [2, sample], [2, full] ]

    for i, _ in enumerate(expected):
        run_test(descriptions[i], expected[i], lambda: g.rock_paper_scissors(*params[i]))

def day3_tests():
    expected = []
    sample, full = read_inputs(2)
    params = [[sample], [full], [sample], [full]]

    for i, _ in enumerate(expected):
        run_test(descriptions[i], expected[i], lambda: dummy_function(*params[i]))
