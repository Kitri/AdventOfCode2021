import common_functions as common
import pytest

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