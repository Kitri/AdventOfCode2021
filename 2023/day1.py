import common as c
import re

def part1(calibration_document):
    sum_of_calibration_values = 0
    for line in calibration_document:
        digits = [c for c in line if c.isnumeric()]
        calibration_value = int(digits[0] + digits[-1])
        sum_of_calibration_values += calibration_value
    
    return sum_of_calibration_values

def part2(calibration_document):
    mapping = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, }

    sum_of_calibration_values = 0

    for line in calibration_document:
        line_digits = [] # (index, num)
        
        for text_number in mapping.keys():
            all_indexes = [m.start() for m in re.finditer(f'(?={text_number})', line)]

            if len(all_indexes) > 0:
                for i in all_indexes:
                    line_digits.append((i, mapping[text_number]))


        line_digits += [(idx, c) for idx, c in enumerate(line) if c.isnumeric()]
        
        line_digits = sorted(line_digits)
        num = str(line_digits[0][1]) + str(line_digits[-1][1])
        sum_of_calibration_values += int(num)
        
    return sum_of_calibration_values

day1_sample = c.read_input('input/day1_sample.txt')
day1_sample2 = c.read_input('input/day1_sample_part2.txt')
day1_full = c.read_input('input/day1.txt')

# print(part1(day1_sample))
# print(part1(day1_full))
# print(part2(day1_sample2))
print(part2(day1_full))




