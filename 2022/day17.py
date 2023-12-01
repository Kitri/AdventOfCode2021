from common import file_parser as fp
from collections import deque

def get_shapes():
    shapes = deque()
    shapes.append([list('####')])
    shapes.append([list('.#.'), list('###'), list('.#.')])
    shapes.append([list('..#'), list('..#'), list('###')])
    shapes.append([['#'], ['#'],['#'],['#']])
    shapes.append([list('##'), list('##')])

    return shapes
    
def get_shape_start(highest_rock):
    stack = 2
    height = 4 + highest_rock
    return (stack, height)

chamber_width = 7
# start = 2 from left, 3 above highest rock surface
start = (2,3)
"""
4  . . . .
3  . . x . 
2  . . . . 
1  . . . . 
0  . . . .
  0 1 2 3 4
"""
"""
|...@...|
|...@X..|
|.@@@XY.|
|..XXXYZ|
|...YYYZ|
|....ZZZ|
|..#.A#A|
|.###B#B|
|..####C|
|.####..|
-1,2,3,2,1,3,-1
"""
def run_game(input_jets):

    highest_points = [-1]*7
    shapes = get_shapes()
    stack, height = get_shape_start(max(highest_points))

    current_shape = shapes.popleft()
    current_shape =[list('..#'), list('..#'), list('###')]
    shape_width = len(current_shape[0])
    shapes.append(current_shape)
    stopped_rocks = 0
    # print(current_shape)
    # print(stack, height)
    highest_points = [-1,2,3,2,0,-1,-1]
    stack, height = get_shape_start(max(highest_points))

    jet_index = 0
    while stopped_rocks < 2:
        jet = input_jets[jet_index]
        rest = False


        if jet == '>' and (stack+shape_width) < 7:
            if highest_points[stack+shape_width] < height: # not higher or equal
                stack += 1
        elif jet == '<' and stack > 0:
            if highest_points[stack-1] < height: # not higher or equal
                stack -=1

        height -= 1

        print(jet, stack, height)
        for idx, rock in enumerate(current_shape[-1]):
            if rock == '#':
                point = highest_points[idx+stack]
                print(point, height)
                if point == height:
                    rest = True
        
        if rest:
            rest = False
            stopped_rocks += 1
            # print('rocks', stopped_rocks)
            #set highest points
            for row in reversed(current_shape):
                height += 1
                for idx, rock in enumerate(row):
                    if rock == '#':
                        highest_points[idx+stack] = height
            stack, height = get_shape_start(max(highest_points))
            current_shape = shapes.popleft()
            shape_width = len(current_shape[0])
            shapes.append(current_shape)
            print(current_shape)
            print(highest_points, stack, height)
                

        jet_index = jet_index + 1 if (jet_index+1) < len(input_jets) else 0
    print(stopped_rocks,'highest',max(highest_points))
def print_game(rocks):
    lengths = [len(rock) for rock in rocks]
    for i in range(max(lengths)+5,-1,-1):
        for j in range(7):
            if i in rocks[j]:
                print('#',end='')
            else:
                print('.',end='')
        print()

def run_game_lists(input_jets):
    rocks = [set() for _ in range(7)]
    highest_point = -1
    shapes = get_shapes()
    height = highest_point + 4
    stack = 2
    stopped_rocks = 0

    current_shape = shapes.popleft()
    shapes.append(current_shape)
    shape_width = len(current_shape[0])
    # print(current_shape, stack, height)

    jet_index = 0
    while stopped_rocks < 2023:
    # for i in range(50):
        jet = input_jets[jet_index]
        rest = False

        if jet == '>' and (stack+shape_width) < 7:
            can_move_right = True
            if shape_width == 3:
                if current_shape[1][0] == '#':
                    top_and_bot_idx = stack + 2
                    mid_idx = stack + 3
                    can_move_right = not ((height+2) in rocks[top_and_bot_idx] or (height+1) in rocks[mid_idx] or height in rocks[top_and_bot_idx])

                    # print('XR',can_move_right)
                elif current_shape[1][0] == '.':
                    right_idx = stack + 3
                    can_move_right = not ((height+2) in rocks[right_idx] or (height+1) in rocks[right_idx] or height in rocks[right_idx])
                    # print('LR',can_move_right)
            else:
                can_move_right = height not in rocks[stack+shape_width]
            if can_move_right:
                stack += 1
        elif jet == '<' and stack > 0:
            can_move_left = True
            if shape_width == 3:
                if current_shape[1][0] == '#':
                    top_and_bot_idx = stack
                    mid_idx = stack - 1 
                    can_move_left = not ((height+2) in rocks[top_and_bot_idx] or (height+1) in rocks[mid_idx] or height in rocks[top_and_bot_idx])

                    # print('XL',can_move_left)
                elif current_shape[1][0] == '.':
                    top_mid_idx = stack + 1
                    bot_idx = stack - 1 
                    can_move_left = not ((height+2) in rocks[top_mid_idx] or (height+1) in rocks[top_mid_idx] or height in rocks[bot_idx])
                    # print('LL',can_move_left)
            else:
                can_move_left = height not in rocks[stack-1]
            if can_move_left:
                stack -=1

        height -= 1

        # print(jet, stack, height)
        for s_idx,s in enumerate(reversed(current_shape)):
            for idx,rock in enumerate(s):
                if rock == '#':
                    if (height+s_idx) in rocks[idx+stack] or height == -1:
                        rest = True

        for idx, rock in enumerate(current_shape[-1]):
            if rock == '#':
                if height in rocks[idx+stack] or height == -1:
                    rest = True
        
        if rest:
            rest = False
            stopped_rocks += 1
            for row in reversed(current_shape):
                height += 1
                if height > highest_point:
                    highest_point = height
                for idx, rock in enumerate(row):
                    if rock == '#':
                        rocks[idx+stack].add(height)
            height = highest_point + 4
            stack = 2
            current_shape = shapes.popleft()
            shape_width = len(current_shape[0])
            shapes.append(current_shape)
            # print(current_shape)
            # print(rocks, stack, height)
                

        jet_index = 0 if (jet_index+1) == len(input_jets) else jet_index + 1
    # print_game(rocks)
    # max_heights = [max(r) for r in rocks]
    print('highest', highest_point)
    # print(rocks)


sample = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
full = fp.read_file_stripped('input/day17.txt')[0]


run_game_lists(sample)
