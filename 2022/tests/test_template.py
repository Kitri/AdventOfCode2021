import pytest

testdata = [
    (1,1)
]
@pytest.mark.parametrize("item, expected", testdata)
def test(item, expected):
    result = item
    assert result == expected, f"Expected {expected}, but got {result}"