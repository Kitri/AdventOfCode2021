import file_parser as c
import numpy as np

def process_round(elf, me):
    points = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    outcome_for_me = {
        ('A','X'): 3, 
        ('B','X'): 0,
        ('C','X'): 6,
        ('A','Y'): 6, 
        ('B','Y'): 3, 
        ('C','Y'): 0,
        ('A','Z'): 0, 
        ('B','Z'): 6, 
        ('C','Z'): 3,
    }

    return points[me] + outcome_for_me[(elf, me)]



def dummy_day2(input_list):
    # Opponent: A for Rock, B for Paper, and C for Scissors
    # You: X for Rock, Y for Paper, and Z for Scissors
    # Score per shape: 1 for Rock, 2 for Paper, and 3 for Scissors
    # Score per outcome: 0 if you lost, 3 if the round was a draw, and 6 if you won
    my_points = 0
    for x in input_list:
        elf, me = x.split()
        round_points = process_round(elf, me)
        print(round_points)
        my_points += round_points

    print(my_points)


    return my_points

sample = c.read_file(f'input/day2_sample.txt')
dummy_day2(sample)

def get_max_calories_optimised_array_storage(calories_input: list, number_max_elements: int):
    calories_input_len = len(calories_input)
    calories_per_elf = []
    calorie_counter = 0

    for idx,calorie in enumerate(calories_input):
        calorie_counter += int(calorie or 0)
        if calorie == '' or idx == calories_input_len - 1:
            calories_per_elf.append(calorie_counter)
            calorie_counter = 0

        # Continuously keep only the top 3 elements
        if(len(calories_per_elf) == 4):
            sorted_list = sorted(calories_per_elf, reverse=True)
            calories_per_elf = sorted_list[:3]

    return calories_per_elf[0] if number_max_elements == 1 else np.sum(calories_per_elf)


def get_max_calories(calories_input: list, number_max_elements: int):
    calories_input_len = len(calories_input)
    calories_per_elf = []
    calorie_counter = 0

    for idx,calorie in enumerate(calories_input):
        calorie_counter += int(calorie or 0)
        if calorie == '' or idx == calories_input_len - 1:
            calories_per_elf.append(calorie_counter)
            calorie_counter = 0
    
    calories_sorted = sorted(calories_per_elf, reverse=True)

    return calories_sorted[0] if number_max_elements == 1 else np.sum(calories_sorted[:3])

def get_max_calories_non_optimised(calories_input: list, number_max_elements: int):
    elves = []

    elf_index = 0
    current_elf = []
    for line in calories_input:
        if line == '':
            elves.append(current_elf)
            current_elf = []
            elf_index += 1
        else:
            current_elf.append(int(line))
    elves.append(current_elf)

    y = [np.sum(x) for x in elves]

    y_sorted = sorted(y, reverse=True)
    y_max_3 = y_sorted[:number_max_elements]

    return np.sum(y_max_3)