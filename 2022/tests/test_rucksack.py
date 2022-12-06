import pytest
import src.rucksack_utilities as rucksack

testdata = [
    ('a',1),
    ('A',27),
    ('z',26),
    ('Z',52)
]
@pytest.mark.parametrize("letter, expected", testdata)
def test(letter, expected):
    result = rucksack.get_priority(letter)
    assert result == expected, f"Expected {expected}, but got {result}"


testdata = [
    ('abcd',['ab','cd']),
    ('xyxxy',['xy','xy']), # not really intentional, leaving for visibility in case I need to cater for non-even strings
    ('yyyyyzzzzz',['yyyyy','zzzzz']),
]
@pytest.mark.parametrize("str_input, expected", testdata)
def test(str_input, expected):
    result = rucksack.split_rucksack_into_2_compartments(str_input)
    assert result == expected, f"Expected {expected}, but got {result}"