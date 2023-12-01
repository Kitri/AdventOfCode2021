from common import file_parser as fp
import numpy as np
import ast
from itertools import zip_longest

def parse_input(input_list):
    pairs = []

    for i in range(0, len(input_list), 3):
        pairs.append((ast.literal_eval(input_list[i]), ast.literal_eval(input_list[i+1])))
    return pairs
def parse_input_part2(input_list):
    ret_list = []
    for line in input_list:
        if line != '':
            ret_list.append(ast.literal_eval(line))
    return ret_list

def compare(left_item, right_item, outer_loop=True):
    for (left, right) in zip_longest(left_item, right_item):

        # print(left,right, type(left), type(right))

        # int compare checks
        if isinstance(left, int) and isinstance(right, int):
            if int(left) > int(right):
                return False
            elif int(left) < int(right):
                return True
        # edge cases
        if right is None:
            return False
        if left is None:
            return True

        if isinstance(left, list) or isinstance(right, list):
            # Make both lists
            if isinstance(left, list) and isinstance(right, int):
                right = [right]
            if isinstance(right, list) and isinstance(left, int):
                left = [left]
            # print(left,right, type(left), type(right))

            compare_result  = compare(left, right, False)
            # print(compare_result)

            if compare_result is not None:
                return compare_result 
    if outer_loop:
        return True


def part1(input_list):
    pairs = parse_input(input_list)
    indexes = []
    for idx,p in enumerate(pairs):
        comparison = compare(p[0], p[1])
        if comparison:
            indexes.append(idx+1)
    print(indexes)
    # [print(type(p[1])) for p in pairs]

    return sum(indexes)

def part2(input_list):
    items = parse_input_part2(input_list)
    items.append([[2]])
    items.append([[6]])
    while(True):
        did_swap = False
        for idx in range(len(items)-1):
            in_order = compare(items[idx], items[idx+1])
            if not in_order:
                did_swap = True
                # print('swapping', idx, idx+1)
                temp = items[idx]
                items[idx] = items[idx+1]
                items[idx+1] = temp
        if did_swap == False:
            break
        
    
    decoder_key = 1
    for idx,x in enumerate(items):
        if x == [[2]] or x == [[6]]:
            decoder_key *= idx+1

    return decoder_key

sample = fp.read_file_stripped('input/day13_sample.txt')
full = fp.read_file_stripped('input/day13.txt')

# assert part1(sample) == 13
# print(part1(full)) #6240 vs 6251

assert part2(sample) == 140
print(part2(full))


assert compare([[4,4],4,4,4], [[4,4],4,4]) == False
# Simple list compare
assert compare([[1],[2,3,4]],[[1],4]) == True
assert compare([1,2,3], [1,2,3]) == True
assert compare([1,2,3], [1,2]) == False
assert compare([1,2], [1,2,3]) == True
assert compare([1,2], [2]) == True
assert compare([2,3], [4,1]) == True
assert compare([9], [8,7,6]) == False

assert compare([[1,2,3]], [[1,2,3]]) == True
assert compare([[1,2,3]], [[1,2]]) == False
assert compare([[1]], [1]) == True
assert compare([9], [[8,7,6]]) == False

assert compare([[4,4],4,4], [[4,4],4,4,4]) == True


assert compare([1,[2,[3,[4,[5,6,3]]]],8,9] , [1,[2,[3,[4,[5,6,4]]]],8,9]) == True
assert compare([1,[2,[3,[4,[5,6,7]]]],8,9] , [1,[2,[3,[4,[5,6,0]]]],8,9]) == False


assert compare([1,2,3],[1,1,1]) == False
assert compare([1,2,3],[1,3,1]) == True

assert compare([[1,1,1]],[[1,1,1]]) == True
assert compare([[1,2,3]],[[1,1,1]]) == False
assert compare([[1,2,3]],[[1,3,1]]) == True

assert compare([[1,1]],[[1,1,1]]) == True
assert compare([[1,1,1]],[[1,1]]) == False


assert compare([[1,2]],[[1,1,1]]) == False
assert compare([[1,1,1]],[[1,2]]) == True

assert compare([[1]],[1]) == True
assert compare([[0,0,0]],[1]) == True
assert compare([1],[[1,0,0]]) == True
assert compare([1],[[0,0,0]]) == False
"""
If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
"""