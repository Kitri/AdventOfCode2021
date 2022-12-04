import pytest
import day5_temp as day5

testdata = [
    (1,1)
]
@pytest.mark.parametrize("item, expected", testdata)
def test_part1(item, expected):
    result = day5.part1(item)
    assert result == expected, f"Expected {expected}, but got {result}"

testdata2 = [
    (1,1)
]
@pytest.mark.parametrize("item, expected", testdata2)
def test_part2(item, expected):
    result = day5.part2(item)
    assert result == expected, f"Expected {expected}, but got {result}"