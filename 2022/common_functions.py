import time
from itertools import pairwise

def run_with_timeprints(func: callable, func_description = ''):
    print(f"---- Start: {func_description}")
    start_time = time.time()
    res = func()
    end_time = time.time()

    print(f"Time taken: {(end_time - start_time)*1000} ms")

    return res

def get_intersection(list_a: list, list_b: list):
    return sorted([item for item in set(list_a) if item in set(list_b)])

def get_intersections(*input_lists, **kwargs):
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


def recurse_intersections(running_result: list, input_list: list):
    if len(input_list) == 0:
        return sorted(running_result)
    else:
        result = get_intersection(running_result, input_list[0])
        return recurse_intersections(result, input_list[1:])
