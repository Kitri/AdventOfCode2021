import file_parser as c
import numpy as np
import common_functions as common
import rucksack_utilities as rucksack

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


def calculate_priority_for_common_items_in_rucksack(mode, rucksacks):
    priority_sum = 0
    rucksacks_by_mode = np.array_split(rucksacks, len(rucksacks)/3) if mode == 2 \
        else [rucksack.split_rucksack_into_2_compartments(item) for item in rucksacks]

    for item in rucksacks_by_mode:
        common_item = common.get_intersections(*item)[0]
        letter_priority = rucksack.get_priority(common_item) 
        priority_sum += letter_priority

    return priority_sum