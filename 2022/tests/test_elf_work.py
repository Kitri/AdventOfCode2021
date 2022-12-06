import src.elf_work as elf_work
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
def test_contains(minA,maxA,minB,maxB, expected):
    result = elf_work.contains_all(minA,maxA,minB,maxB)
    assert result == expected, f"Expected {expected}, but got {result}"

testdata2 = [
    (2,4,6,8,False),
    (6,8,2,4,False),
    (2,6,4,8,True),
    (5,7,7,9,True),
    (2,8,3,7,True),
    (6,6,4,6,True),
    (23,72,23,72,True),
    (7,30,8,60,True),
    (6,6,6,6,True),
]
@pytest.mark.parametrize("minA,maxA,minB,maxB, expected", testdata2)
def test_overlap(minA,maxA,minB,maxB, expected):
    result = elf_work.overlaps(minA,maxA,minB,maxB)
    assert result == expected, f"Expected {expected}, but got {result}"