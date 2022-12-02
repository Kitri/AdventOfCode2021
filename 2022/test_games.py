import pytest
from games import Shape, Outcome
import games as g

testdata = [
    ('A', Shape.ROCK),
    ('B', Shape.PAPER),
    ('C', Shape.SCISSORS),
    ('X', Shape.ROCK),
    ('Y', Shape.PAPER),
    ('Z', Shape.SCISSORS),
]
@pytest.mark.parametrize("letter,expected", testdata)
def test_shape_convert(letter, expected):
    converted = g.convert_to_shape(letter) 
    assert converted == expected, f"Expected {expected}, got {converted}"

def test_parse_input_part_1():
    input_list = ['A Y', 'B X', 'C Z']
    expected_output = [
        (Shape.ROCK, Shape.PAPER),
        (Shape.PAPER, Shape.ROCK),
        (Shape.SCISSORS, Shape.SCISSORS)
    ]
    parsed = g.parse_input(1, input_list)
    assert parsed == expected_output, f"Expected {expected_output}, got {parsed}"

def test_parse_input_part_2():
    input_list = ['A Y', 'B X', 'C Z']
    expected_output = [
        (Shape.ROCK, Outcome.DRAW),
        (Shape.PAPER, Outcome.LOSE),
        (Shape.SCISSORS, Outcome.WIN)
    ]
    parsed = g.parse_input(2, input_list)
    assert parsed == expected_output, f"Expected {expected_output}, got {parsed}"


testdata_winning = [
    (Shape.ROCK, Shape.ROCK, Outcome.DRAW),
    (Shape.PAPER, Shape.ROCK, Outcome.LOSE),
    (Shape.SCISSORS, Shape.ROCK, Outcome.WIN),
    (Shape.ROCK, Shape.PAPER, Outcome.WIN),
    (Shape.PAPER, Shape.PAPER, Outcome.DRAW),
    (Shape.SCISSORS, Shape.PAPER, Outcome.LOSE),
    (Shape.ROCK, Shape.SCISSORS, Outcome.LOSE),
    (Shape.PAPER, Shape.SCISSORS, Outcome.WIN),
    (Shape.SCISSORS, Shape.SCISSORS, Outcome.DRAW),
]
@pytest.mark.parametrize("opponent, player, outcome", testdata_winning)
def test_player_win(opponent, player, outcome):
    out = g.determine_player_outcome(opponent, player)
    assert out == outcome, f"Expected {outcome}, got {out}"


testdata_nextmove = [
    (Shape.ROCK, Outcome.WIN, Shape.PAPER),
    (Shape.PAPER, Outcome.WIN, Shape.SCISSORS),
    (Shape.SCISSORS, Outcome.WIN, Shape.ROCK),
    (Shape.ROCK, Outcome.DRAW, Shape.ROCK),
    (Shape.PAPER, Outcome.DRAW, Shape.PAPER),
    (Shape.SCISSORS, Outcome.DRAW, Shape.SCISSORS),
    (Shape.ROCK, Outcome.LOSE, Shape.SCISSORS),
    (Shape.PAPER, Outcome.LOSE, Shape.ROCK),
    (Shape.SCISSORS, Outcome.LOSE, Shape.PAPER)
]
@pytest.mark.parametrize("opponent, outcome, player", testdata_nextmove)
def test_player_next_move(opponent, outcome, player):
    play = g.determine_player_move(opponent, outcome)
    assert play == player, f"Expected {player}, got {play}"
