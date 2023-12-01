from collections import deque
from common import file_parser as fp


def move_right(stack, board, height, shape_idx):
    default_width = 7
    can_move = True
    shape_widths = [4,3,3,1,2]
    shape_heights = [1,3,3,4,2]
    current_width = shape_widths[shape_idx]
    current_height = shape_heights[shape_idx]

    # Reached right end
    if (stack + current_width) == default_width:
        can_move = False
    elif shape_idx == 0: # horizontal line
        for h in range(current_height):
            if height in board[stack + current_width]:
                can_move = False
    elif shape_idx == 1: # cross
        for h in range(current_height):
            if height + h in board[stack + current_width + (h%2-1)]:
                can_move = False
    elif shape_idx == 2: #L
        for h in range(current_height):
            if height + h in board[stack + current_width]:
                can_move = False
    elif shape_idx == 3 or shape_idx == 4: # | 
        for h in range(current_height):
            if height+h in board[stack + current_width]:
                can_move = False

    return stack + 1 if can_move else stack

def move_left(stack, board, height, shape_idx):
    shape_widths = [4,3,3,1,2]
    shape_heights = [1,3,3,4,2]
    current_width = shape_widths[shape_idx]
    current_height = shape_heights[shape_idx]
    can_move = True
    # Reached left end
    if stack == 0:
        can_move = False
    elif shape_idx == 0: # - 
        for h in range(current_height):
            if height in board[stack-1]:
                can_move = False
    elif shape_idx == 1: # +
        for h in range(current_height):
            if height + h in board[stack - h%2]:
                can_move = False
    elif shape_idx == 2: # reverse L
        if height in board[stack-1] \
            or height+1 in board[stack+1] \
            or height+2 in board[stack+1]:
            can_move = False
    elif shape_idx == 3 or shape_idx == 4: # | or box 
        for h in range(current_height):
            if height+h in board[stack-1]:
                can_move = False

    return stack - 1 if can_move else stack

def move_down(stack, board, height, shape_idx):
    shape_widths = [4,3,3,1,2]
    shape_heights = [1,3,3,4,2]
    current_width = shape_widths[shape_idx]
    current_height = shape_heights[shape_idx]

    temp_height = height - 1
    if temp_height == -1:
        return (True, height)

    rest = False
    if shape_idx == 0 or shape_idx == 2 or shape_idx == 4:
        for i in range(current_width):
            if temp_height in board[stack+i]:
                rest = True
    elif shape_idx == 1:
        if height in board[stack] or height in board[stack+2] or temp_height in board[stack+1]:
            rest = True
    elif shape_idx == 3:
        if temp_height in board[stack]:
            rest = True

    if not rest:
        height -= 1
    return (rest, height)
def add_rock_to_board(board,height,stack,current_shape):
    highest_height = 0
    match current_shape:
        case 0: # ----
            for i in range(4):
                board[stack+i].add(height)
            highest_height = height
        case 1: # +
            board[stack].add(height+1)
            board[stack+1].add(height)
            board[stack+1].add(height+1)
            board[stack+1].add(height+2)
            board[stack+2].add(height+1)
            highest_height = height+2
        case 2: # reverse L
            board[stack].add(height)
            board[stack+1].add(height)
            board[stack+2].add(height)
            board[stack+2].add(height+1)
            board[stack+2].add(height+2)
            highest_height = height+2
        case 3: # |
            for i in range(4):
                board[stack].add(height+i)
            highest_height = height + 3
        case 4: # ::
            for i in range(2):
                board[stack+i].add(height)
                board[stack+i].add(height+1)

            highest_height = height+1

    return highest_height

def print_game(rocks):
    lengths = [len(rock) for rock in rocks]
    for i in range(max(lengths)+5,-1,-1):
        for j in range(7):
            if i in rocks[j]:
                print('#',end='')
            else:
                print('.',end='')
        print()

def run_game(jets_input, iter_num):
    board = [set() for _ in range(7)]
    shapes = deque([0,1,2,3,4])
    highest_point = -1
    height = highest_point + 4
    default_width = 7
    stack = 2
    stopped_rocks = 0
    jets_idx = 0

    current_shape = shapes.popleft()
    shapes.append(current_shape)

    while stopped_rocks < iter_num:
        current_jet = jets_input[jets_idx]
        if current_jet == '<':
            stack = move_left(stack, board, height, current_shape)
        elif current_jet == '>':
            stack = move_right(stack, board, height, current_shape)
        
        rest, height = move_down(stack, board, height, current_shape)
        # print(current_jet, stack, height, rest)
        if rest:
            highest_added = add_rock_to_board(board,height,stack,current_shape)
            if highest_added > highest_point:
                highest_point = highest_added
            stopped_rocks += 1
            current_shape = shapes.popleft()
            shapes.append(current_shape)
            stack = 2
            height = highest_point+4
            # print(current_shape, stack, height)
        

        jets_idx = jets_idx + 1 if jets_idx + 1 < len(jets_input) else 0
    # print_game(board)
    # print(board)
    print(highest_point+1)




# Tests
# assert move_left(2,[set(),set(),set(),set(),set(),set(),set()], 3, 0) == 1
# assert move_left(2,[set(),set([3]),set(),set(),set(),set(),set()], 3, 0) == 2
# assert move_left(0,[set(),set(),set(),set(),set(),set(),set()], 3, 0) == 0

# assert move_left(0,[set(),set(),set(),set(),set(),set(),set()], 3, 1) == 0
# assert move_left(2,[set(),set(),set([3]),set(),set(),set(),set()], 3, 1) == 2
# assert move_left(3,[set(),set([3]),set([2]),set(),set(),set(),set()], 3, 1) == 2
# assert move_left(2,[set(),set(),set([5]),set(),set(),set(),set()], 3, 1) == 2
# assert move_left(2,[set(),set([5]),set(),set(),set(),set(),set()], 3, 1) == 1

# assert move_left(0,[set(),set(),set(),set(),set(),set(),set()], 3, 2) == 0
# assert move_left(2,[set(),set([3]),set(),set(),set(),set(),set()], 3, 2) == 2
# assert move_left(2,[set(),set(),set(),set([4]),set(),set(),set()], 3, 2) == 2
# assert move_left(2,[set(),set(),set(),set([5]),set(),set(),set()], 3, 2) == 2
# assert move_left(2,[set([3]),set(),set(),set(),set(),set(),set()], 3, 2) == 1
# assert move_left(2,[set(),set(),set([4]),set(),set(),set(),set()], 3, 2) == 1
# assert move_left(2,[set(),set(),set([5]),set(),set(),set(),set()], 3, 2) == 1

# assert move_left(2,[set(),set(),set(),set(),set(),set(),set()], 3, 3) == 1
# assert move_left(2,[set(),set([3]),set(),set(),set(),set(),set()], 3, 3) == 2
# assert move_left(2,[set(),set([4]),set(),set(),set(),set(),set()], 3, 3) == 2
# assert move_left(2,[set(),set([5]),set(),set(),set(),set(),set()], 3, 3) == 2
# assert move_left(2,[set(),set([6]),set(),set(),set(),set(),set()], 3, 3) == 2
# assert move_left(3,[set(),set([5]),set(),set(),set(),set(),set()], 3, 3) == 2

# assert move_left(2,[set(),set(),set(),set(),set(),set(),set()], 3, 4) == 1
# assert move_left(2,[set(),set([3]),set(),set(),set(),set(),set()], 3, 4) == 2
# assert move_left(2,[set(),set([4]),set(),set(),set(),set(),set()], 3, 4) == 2

# assert move_right(2,[set(),set(),set(),set(),set(),set(),set()], 3, 0) == 3
# assert move_right(2,[set(),set(),set(),set(),set(),set(),set([3])], 3, 0) == 2
# assert move_right(3,[set(),set(),set(),set(),set(),set(),set()], 3, 0) == 3

# assert move_right(2,[set(),set(),set(),set(),set(),set(),set()], 3, 1) == 3
# assert move_right(2,[set(),set(),set(),set(),set([3]),set(),set()], 3, 1) == 2
# assert move_right(2,[set(),set(),set(),set(),set([4]),set(),set()], 3, 1) == 3
# assert move_right(2,[set(),set(),set(),set(),set(),set([4]),set()], 3, 1) == 2
# assert move_right(2,[set(),set(),set(),set(),set(),set([5]),set()], 3, 1) == 3
# assert move_right(2,[set(),set(),set(),set(),set([5]),set(),set()], 3, 1) == 2
# assert move_right(2,[set(),set(),set(),set(),set([6]),set(),set()], 3, 1) == 3

# assert move_right(2,[set(),set(),set(),set(),set(),set(),set()], 3, 2) == 3
# assert move_right(1,[set(),set(),set(),set(),set([3]),set(),set()], 3, 2) == 1
# assert move_right(1,[set(),set(),set(),set(),set([4]),set(),set()], 3, 2) == 1
# assert move_right(1,[set(),set(),set(),set(),set([5]),set(),set()], 3, 2) == 1
# assert move_right(1,[set(),set(),set(),set(),set(),set([3,4,5]),set()], 3, 2) == 2

# assert move_right(2,[set(),set(),set(),set(),set(),set(),set()], 3, 3) == 3
# assert move_right(2,[set(),set(),set(),set([3]),set(),set(),set()], 3, 3) == 2
# assert move_right(2,[set(),set(),set(),set([4]),set(),set(),set()], 3, 3) == 2
# assert move_right(2,[set(),set(),set(),set([5]),set(),set(),set()], 3, 3) == 2
# assert move_right(2,[set(),set(),set(),set([6]),set(),set(),set()], 3, 3) == 2
# assert move_right(3,[set(),set(),set(),set([5]),set(),set(),set()], 3, 3) == 4

# assert move_right(2,[set(),set(),set(),set(),set(),set(),set()], 3, 4) == 3
# assert move_right(2,[set(),set(),set(),set(),set([3]),set(),set()], 3, 4) == 2
# assert move_right(2,[set(),set(),set(),set(),set([4]),set(),set()], 3, 4) == 2
# assert move_right(2,[set(),set(),set(),set(),set([5]),set(),set()], 3, 4) == 3
# assert move_right(2,[set(),set(),set(),set(),set(),set([3]),set()], 3, 4) == 3

# assert move_down(2,[set(),set(),set(),set(),set(),set(),set()], 3, 0) == (False,2)
# assert move_down(3,[set(),set(),set(),set(),set(),set(),set([3])], 4, 0) == (True,4)
# assert move_down(3,[set(),set(),set(),set(),set(),set(),set()], 0, 0) == (True,0)

# assert move_down(2,[set(),set(),set(),set(),set(),set(),set()], 3, 1) == (False,2)
# assert move_down(3,[set(),set(),set(),set(),set([3]),set(),set()], 4, 1) == (True,4)
# assert move_down(3,[set(),set(),set(),set([4]),set(),set(),set()], 4, 1) == (True,4)
# assert move_down(3,[set(),set(),set(),set(),set(),set([4]),set()], 4, 1) == (True,4)
# assert move_down(3,[set(),set(),set(),set(),set([2]),set(),set()], 4, 1) == (False,3)
# assert move_down(3,[set(),set(),set(),set([3]),set(),set(),set()], 4, 1) == (False,3)
# assert move_down(3,[set(),set(),set(),set(),set(),set([3]),set()], 4, 1) == (False,3)

# assert move_down(2,[set(),set(),set(),set(),set(),set(),set()], 3, 2) == (False,2)
# assert move_down(2,[set(),set(),set(),set(),set(),set(),set()], 0, 2) == (True,0)
# assert move_down(2,[set(),set(),set([2]),set(),set(),set(),set()], 3, 2) == (True,3)
# assert move_down(2,[set(),set(),set(),set([2]),set(),set(),set()], 3, 2) == (True,3)
# assert move_down(2,[set(),set(),set(),set(),set([2]),set(),set()], 3, 2) == (True,3)
# assert move_down(2,[set(),set(),set([1]),set(),set(),set(),set()], 3, 2) == (False,2)
# assert move_down(2,[set(),set(),set(),set([1]),set(),set(),set()], 3, 2) == (False,2)
# assert move_down(2,[set(),set(),set(),set(),set([1]),set(),set()], 3, 2) == (False,2)

# assert move_down(2,[set(),set(),set([2]),set(),set(),set(),set()], 3, 3) == (True,3)
# assert move_down(2,[set(),set(),set(),set(),set(),set(),set()], 3, 3) == (False,2)

# assert move_down(2,[set(),set(),set(),set(),set(),set(),set()], 3, 4) == (False,2)
# assert move_down(2,[set(),set(),set([2]),set(),set(),set(),set()], 3, 4) == (True,3)
# assert move_down(2,[set(),set(),set(),set([2]),set(),set(),set()], 3, 4) == (True,3)
# assert move_down(2,[set(),set(),set([1]),set([1]),set(),set(),set()], 3, 4) == (False,2)
sample = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
full = fp.read_file_stripped('input/day17.txt')[0]

run_game(sample,1000000000000)