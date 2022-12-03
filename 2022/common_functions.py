import time
from itertools import pairwise

def run_with_timeprints(func: callable, func_description: str = ''):
    print(f"- Start: {func_description}")
    start_time = time.time()
    res = func()
    end_time = time.time()

    print(f"Time taken: {(end_time - start_time)*1000} ms")

    return res

def get_intersection(list_a: list, list_b: list) -> list:
    return sorted([item for item in set(list_a) if item in set(list_b)])

def get_intersections(*input_lists, **kwargs) -> list:
    recursive = kwargs.get('recursive',False)
    if len(input_lists) == 2:
        return get_intersection(input_lists[0], input_lists[1])

    if recursive:
        return recurse_intersections(input_lists[0], input_lists[1:])
    else:
        input_pairs = pairwise(input_lists)
        running_result = input_lists[0]
        for _, list_b in input_pairs:
            running_result = get_intersection(running_result, list_b)

        return sorted(running_result)


def recurse_intersections(running_result: list, input_list: list) -> list:
    if len(input_list) == 0:
        return sorted(running_result)
    else:
        result = get_intersection(running_result, input_list[0])
        return recurse_intersections(result, input_list[1:])

def parse_input(input_function: callable, input_list: list) -> list:
    return [input_function(item) for item in input_list]

def add_single_item_to_list_items(params: list, new_item: any):
    for param in params:
        param.append(new_item)

    return params

def add_list_to_list_items(params: list, new_list: list):
    for param in params:
        param += new_list

    return params

def add_different_items_to_list_items(params: list, new_list: list):
    if len(params) != len(new_list):
        raise Exception('lists have to match in length to use this function')

    for idx,param in enumerate(params):
        param.append(new_list[idx])

    return params
