def parse_input(item):
    return item

def part1(some_input):
    return some_input
    
def part2(some_input):
    return some_input

def do_day5(mode, input_list):
    func = part1 if mode == 1 else part2
    result = 0
    for item in input_list:
        parsed = parse_input(item)
        func_result = func(parsed)
        print(func_result)
        result += func_result
    
    return result