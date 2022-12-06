def part1():
    input_list = [x.strip() for x in open('input/day4.txt').readlines()]

    line_split = map(lambda line: line.split(','), input_list)
    mapped = map(lambda x: list(map(int,x[0].split("-"))) + list(map(int,x[1].split("-"))), line_split)
    contains_all = map(lambda x: ((x[0] <= x[2] <= x[3] <= x[1]) or (x[2] <= x[0] <= x[1] <= x[3])), mapped)
    return len([x for x in contains_all if x == True])

def part2():
    input_list = [x.strip() for x in open('input/day4.txt').readlines()]

    line_split = map(lambda line: line.split(','), input_list)
    mapped = map(lambda x: list(map(int,x[0].split("-"))) + list(map(int,x[1].split("-"))), line_split)
    overlaps = map(lambda x: (x[1] >= x[2] and x[3] >= x[0]), mapped)
    return len([x for x in overlaps if x == True])

# 'expected': [2,459,4,779],
print(part1())
print(part2())