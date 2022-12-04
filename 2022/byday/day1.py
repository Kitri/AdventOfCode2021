import file_parser

sample = file_parser.read_file(f'input/day1_sample.txt') 
full =  file_parser.read_file(f'input/day1.txt')

def get_max_calories(mode: int, calories_input: list):
    number_max_elements = 1 if mode == 1 else 3
    calories_input_len = len(calories_input)
    calories_per_elf = []
    calorie_counter = 0

    for idx,calorie in enumerate(calories_input):
        calorie_counter += int(calorie or 0)
        if calorie == '' or idx == calories_input_len - 1:
            calories_per_elf.append(calorie_counter)
            calorie_counter = 0
    
    calories_sorted = sorted(calories_per_elf, reverse=True)

    return calories_sorted[0] if number_max_elements == 1 else sum(calories_sorted[:3])


print(get_max_calories(1,full))
print(get_max_calories(2,full))
