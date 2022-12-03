import common_functions as common

def input_function(item):
    return item * 2

def day4_stuff(mode, input_list):
    parsed = common.parse_input(input_function, input_list)
    print(parsed)
    return mode

day4_stuff(1,[1,2,3])