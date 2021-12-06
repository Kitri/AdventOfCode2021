
from common import get_df_from_file, read_file
import numpy as np

import importlib
importlib.reload(common)

def split_arr_into_boards(arr):
    boards = []
    index = 0
    inner_arr = []
    for (i,nums) in enumerate(arr):
        if(i == len(arr) -1):
            inner_arr.append(nums)  
            boards.append(inner_arr)
        elif(nums == ''):
            boards.append(inner_arr)
            inner_arr = []
        else:
          inner_arr.append(nums)  

    return boards

def create_board(board_strings):
    new_board = []
    for board in board_strings:
        new_row = []
        for row in board:
            x = row.strip().replace('  ',' ').split(' ')
            x = [int(i) for i in x]
            new_row.append(x)
        new_board.append(new_row)
    return new_board
        
    
    
def create_index_of_board():
    board = [[0 for col in range(5)] for row in range(5)]
    return board

def test_for_bingo(indexes):
    rows = len(indexes)
    cols = len(indexes[0])
    bingo = False
    np_arr = np.array(indexes)

    # Check rows
    for i in range(0,5):
        row = np_arr[:,i]
        if(0 not in row):
            bingo = True

    # Check columns
    for i in range(0,5):
        row = np_arr[i,:]
        if(0 not in row):
            bingo = True
    
  #  if(indexes[0][0] == 1 and indexes[1][1] == 1 and indexes[2][2] == 1 and indexes[3][3] == 1 and indexes[4][4] ==1):
   #     bingo = True

    #if(indexes[4][0] == 1 and indexes[3][1] == 1 and indexes[2][2] == 1 and indexes[1][3] == 1 and indexes[0][4] ==1):
     #   bingo = True

    return bingo
        
def read_bingo_for_board(numbers, board):
    indexes = create_index_of_board()
    num_called_when_bingo = -1

    for num in numbers:
        for i in range(0,5):
            if(num_called_when_bingo != -1):
                break
            for j in range(0,5):
                item = board[i][j]
                if(item == num):
                    indexes[i][j] = 1
                    bingo = test_for_bingo(indexes)
                    if(bingo):
                        num_called_when_bingo = num
                        print(f'bingo! num {num_called_when_bingo}')
                        break

    if(num_called_when_bingo != -1):
        [print(i) for i in indexes]
        sum = 0
        for i in range(0,5):
            for j in range(0,5):
                if(indexes[i][j] == 0):
                    sum += board[i][j]

        return sum * num_called_when_bingo

    return -1
        

def read_bingo_for_boards(numbers, boards):
    print(len(boards))
    index_list = []
    for i in range(0,len(boards)):
        index_list.append(create_index_of_board())
        
    num_called_when_bingo = -1
    board_num = -1

    for num in numbers:
        if(num_called_when_bingo != -1):
            break
        
        for (board_i, board) in enumerate(boards):
            if(num_called_when_bingo != -1):
                break
            indexes = index_list[board_i]
            for i in range(0,5):
                if(num_called_when_bingo != -1):
                    break
                for j in range(0,5):
                    item = board[i][j]
                    if(item == num):
                        indexes[i][j] = 1
                        bingo = test_for_bingo(indexes)
                        if(bingo):
                            num_called_when_bingo = num
                            board_num = board_i
                            print(f'bingo! board {board_i} num {num_called_when_bingo}')
                            break

    if(num_called_when_bingo != -1):
        indexes = index_list[board_num]
        board = boards[board_num]
        [print(i) for i in indexes]
        sum = 0
        for i in range(0,5):
            for j in range(0,5):
                if(indexes[i][j] == 0):
                    sum += board[i][j]

        print(f"sum {sum}")
        return sum * num_called_when_bingo

    return -1

def get_last_winning_board(numbers, boards):
    print(len(boards))
    index_list = []
    for i in range(0,len(boards)):
        index_list.append(create_index_of_board())
        
    num_called_when_bingo = -1
    board_num = -1
    winning_boards = []
    expected_winning_boards = list(range(0,len(boards)))

    for num in numbers:
        for (board_i, board) in enumerate(boards):
            has_won = [x for x in expected_winning_boards if x not in winning_boards]
            if(len(has_won) == 0):
                break
            indexes = index_list[board_i]
            for i in range(0,5):
                for j in range(0,5):
                    item = board[i][j]
                    if(item == num):
                        indexes[i][j] = 1
                        bingo = test_for_bingo(indexes)
                        if(bingo):
                            num_called_when_bingo = num
                            board_num = board_i
                            winning_boards.append(board_num)
                            print(f'bingo! board {board_i} num {num_called_when_bingo}')

    if(num_called_when_bingo != -1):
        return winning_boards

    return -1


def test1(bingo_in):
    numbers_chosen = bingo_in[0]
    rest = bingo_in[2:]
    boards = split_arr_into_boards(rest)

    result = len(boards)
    expected = 3
    assert result == expected, f"1. Expected {expected} but found {result}"

def test2(bingo_in):
    numbers_chosen = bingo_in[0]
    rest = bingo_in[2:]
    board_strings = split_arr_into_boards(rest)
    boards = create_board(board_strings)

    [print(x) for x in boards]

    # print(board_strings[0][0].replace(' ',',').replace(',,',',').split(','))
    
    result = 1
    expected = 1
    assert 1 == 1, f"2. Expected {expected} but found {result}"

def test3(bingo_in):
    indexes = create_index_of_board()
    board1 = [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]]
    nums = 1,10,14,4,0

    for num in nums:
        for i in range(0,5):
            for j in range(0,5):
                item = board1[i][j]
                if(item == num):
                    indexes[i][j] = 1

    # print(indexes)
                
        
    print(bingo)


    result = 1
    expected = 1
    assert 1 == 1, f"3. Expected {expected} but found {result}"

def test4(bingo_in):
    numbers_chosen = [int(x) for x in bingo_in[0].split(',')]
    rest = bingo_in[2:]
    board_strings = split_arr_into_boards(rest)
    boards = create_board(board_strings)
    print(len(boards))

    bingo = read_bingo_for_boards(numbers_chosen, boards)
    print(bingo)
    result = 1
    expected = 1
    assert 1 == 1, f"4. Expected {expected} but found {result}"

def test5(bingo_in):
    numbers_chosen = [int(x) for x in bingo_in[0].split(',')]
    rest = bingo_in[2:]
    board_strings = split_arr_into_boards(rest)
    boards = create_board(board_strings)
    print(len(boards))

    bingo = get_last_winning_board(numbers_chosen, boards)
    last_win = bingo[-1]
    print(bingo)
    print(last_win)
    bingo_rerun = read_bingo_for_board(numbers_chosen, boards[last_win])
    print(bingo_rerun)
    result = 1
    expected = 1
    assert 1 == 1, f"5. Expected {expected} but found {result}"

day4_input = read_file('input/day4.txt')
day4_sample = read_file('input/day4_sample.txt')


#test1(day4_sample)
#test2(day4_sample)
# test3(day4_sample)
# test4(day4_input)
test5(day4_input)
