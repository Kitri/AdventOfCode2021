import temp_day4 as d
import pytest

testdata = [
    (2,4,6,8,False),
    (2,8,3,7,True),
    (6,6,4,6,True),
    (23,72,23,72,True),
    (7,30,8,60,False),
    (6,6,6,6,True),
]
@pytest.mark.parametrize("minA,maxA,minB,maxB, expected", testdata)
def test(minA,maxA,minB,maxB, expected):
    result = d.contains_all(minA,maxA,minB,maxB)
    assert result == expected, f"Expected {expected}, but got {result}"