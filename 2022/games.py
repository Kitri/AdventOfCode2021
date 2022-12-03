from enum import Enum

Shape = Enum('Shape', ['ROCK', 'PAPER', 'SCISSORS'])
class Outcome(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

def convert_to_shape(letter):
    mappings = {
        Shape.ROCK : ['A','X'],
        Shape.PAPER : ['B','Y'],
        Shape.SCISSORS : ['C', 'Z']
    }

    return [shape for shape in mappings if letter in mappings[shape]][0]

def convert_to_outcome(letter):
    mappings = {
        Outcome.LOSE : 'X',
        Outcome.DRAW : 'Y',
        Outcome.WIN :  'Z'
    }

    return [outcome for outcome in mappings if letter == mappings[outcome]][0]

# A B
# A,B
def parse_input(mode: int, input_list: list):
    convert_func_b = convert_to_shape if mode == 1 else convert_to_outcome
    return [(convert_to_shape(a), convert_func_b(b)) for a,b in (x.split() for x in input_list)]

def determine_player_outcome(opponent, player):
    if player.value == opponent.value:
        return Outcome.DRAW
    
    return Outcome.WIN if player.value - opponent.value in [1,-2] else Outcome.LOSE

def determine_player_move(opponent, outcome):
    if outcome == Outcome.DRAW:
        return opponent

    win = opponent.value + 1 if opponent.value < 3 else 1
    lose = opponent.value - 1 if opponent.value > 1 else 3

    return Shape(win) if outcome == Outcome.WIN else Shape(lose)

def rock_paper_scissors(mode, input_list):
    game_input = parse_input(mode, input_list)
    player_points = 0
    
    function_by_mode = determine_player_outcome if mode == 1 else determine_player_move

    for opponent, input2 in game_input:
        result = function_by_mode(opponent, input2)
        player_points += result.value + input2.value

    return player_points