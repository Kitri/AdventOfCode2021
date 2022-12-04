import file_parser as fp
import jungle_navigation as jungle
import games as g
import common_functions as cf
import temp_day4 as day4

descriptions = ['Part1 Sample', 'Part1 Full', 'Part2 Sample','Part2 Full']

# setup (optional) = setting up for next day
def read_inputs(day: int, setup: bool=False):
    sample =fp.read_file(f'input/day{day}_sample.txt') 
    full = fp.read_file(f'input/day{day}.txt') if setup == False else [] 
    return(sample, full)

def run_test(description: str, expected: list, func: callable):
    answer = cf.run_with_timeprints(func, description)
    print("Answer", answer)
    assert answer == expected, f"Expected {expected} but got {answer}"

def add_params_from_config(param_config: dict, params: list):
    config = param_config['config']

    match param_config['mode']: 
        case 'single':
            add_params_func = cf.add_single_item_to_list_items
        case 'list':
            add_params_func = cf.add_list_to_list_items
        case 'different':
            add_params_func = cf.add_different_items_to_list_items

    params = add_params_func(params, config)
    return params

def compare_day1_optimisations():
    full = fp.read_file('input/day1.txt')
    print('Part 1')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_non_optimised(1,full),'Split into list, then sum')
    cf.run_with_timeprints(lambda: jungle.get_max_calories(1,full),'Sum in original iteration')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_optimised_array_storage(1,full),'Optimised + keep only 4 items in array')

    print('Part 2')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_non_optimised(2,full),'Split into list, then sum')
    cf.run_with_timeprints(lambda: jungle.get_max_calories(2,full),'Sum in original iteration')
    cf.run_with_timeprints(lambda: jungle.get_max_calories_optimised_array_storage(2,full),'Optimised + keep only 4 items in array')

### Configuration for main
# expected: list[4] - expected values: p1_sample, p1, p2_sample, p2
# day: int - day number
# func: name of the function that runs this day
# params (optional):
#    mode:  single - add single item to all params
#           list - add a list to all params
#           different - add list to param by index
main_configuration = [
    {
        'expected': [24000, 67450, 45000, 199357],
        'day': 1,
        'func': jungle.get_max_calories 
    },
    {
        'expected': [15, 12156, 12, 10835],
        'day': 2,
        'func': g.rock_paper_scissors
    },
    {
        'expected': [157, 7766, 70, 2415],
        'day': 3,
        'func': jungle.calculate_priority_for_common_items_in_rucksack
    },
    {
        'expected': [2,459,4,1],
        'day': 4,
        'func': day4.day4_stuff
    }
]

def run_day(config, setup=False):
    day = config['day']
    print(f"###### Day {day}")
    sample, full = read_inputs(day, setup)
    params = [[1, sample], [1, full], [2, sample], [2, full]]
    if 'params' in config:
        params = add_params_from_config(config['params'])

    for i, _ in enumerate(config['expected']):
        run_test(descriptions[i], config['expected'][i], lambda: config['func'](*params[i]))


def run_all_days(all_config):
    for config in all_config:
        run_day(config)
        print()

# run_all_days(main_configuration)
run_day(main_configuration[3])
