import pytest
import common_functions as common


testdata = [
    (['A','B'], ['B','C'], ['B']),
    (['A','C','B'], ['B','C'], ['B','C'])
]
@pytest.mark.parametrize("listA, listB, expected", testdata)
def test_get_intersections(listA, listB, expected):
    result = common.get_intersection(listA, listB) 
    assert result == expected, f"Expected {expected} but got {result}"

testdata_multiple = [
    ([['A','B'], ['B','C']], ['B']),
    ([['A','B'], ['B','C'], ['B', 'A']], ['B']),
    ([['A','B','C'], ['B','C'], ['B', 'A','C'],['Z','B','C','X']], ['B','C'])
]
@pytest.mark.parametrize("input_lists, expected", testdata_multiple)
def test_get_multiple_intersections(input_lists, expected):
    result = common.get_intersections(*input_lists)
    assert result == expected, f"Expected {expected} but got {result}"

@pytest.mark.parametrize("input_lists, expected", testdata_multiple)
def test_get_multiple_intersections_recursive(input_lists, expected):
    recurse_result = common.get_intersections(*input_lists, recursive=True)
    assert recurse_result == expected, f"Expected {expected} but got {recurse_result}"

def input_funct(item):
    return item*2

def test_input_parser():
    input_list = [1,2,3]
    new_list = common.parse_input(input_funct, input_list)
    assert new_list == [2,4,6]

def test_add_single_item_to_list_items():
    result = common.add_single_item_to_list_items([['a','b'],['x','y']], 1)
    assert result == [['a','b',1],['x','y',1]]

def test_add_list_to_list_items():
     result = common.add_list_to_list_items([['a','b'],['x','y']], [1,2])
     assert result == [['a','b',1,2],['x','y',1,2]]

def test_add_different_items_to_list_items():
     result = common.add_different_items_to_list_items([['a','b'],['x','y']], [1,2])
     assert result == [['a','b',1],['x','y',2]]

def test_add_different_items_to_list_items():
    with pytest.raises(Exception) as e_info:
        common.add_different_items_to_list_items([['a','b'],['x','y']], [1])