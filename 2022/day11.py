from common import file_parser as fp

def part1(x):
    print(x)
    return 1

sample = fp.read_file_stripped('input/day10_sample.txt')
full = fp.read_file_stripped('input/day10.txt')

assert part1(sample) == 1