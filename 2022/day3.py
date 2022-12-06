import numpy as np

# ASCII a = 97; A = 65
# Priority a = 1; A = 27
# 97-1 = 96; 65 - 27 = 38
def get_priority(letter: chr) -> int:
    return (ord(letter) - 38) if letter.isupper() else (ord(letter) - 96)

def part1():
    input_list = [x.strip() for x in open('input/day3.txt').readlines()]
    intersections = map(lambda line: (set(line[:len(line)//2]) & set(line[-len(line)//2:])).pop(), input_list)
    priorities = map(lambda letter: get_priority(letter), intersections)
    return sum(priorities)

def part2():
    input_list = [x.strip() for x in open('input/day3.txt').readlines()]
    groups = np.array_split(input_list, len(input_list)/3)
    intersections = map(lambda group: (set(group[0]) & set(group[1]) & set(group[2])).pop(),groups)
    priorities = map(lambda letter: get_priority(letter), intersections)
    return sum(priorities)

# 'expected': [157, 7766, 70, 2415],
print('part1', part1())
print('part2', part2())
