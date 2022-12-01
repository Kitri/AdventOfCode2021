import common
import sys
import numpy as np
import functools
from datetime import datetime
from collections import deque
import heapq

from common import read_file

daynum = 15 # set to number
def interpret_input(input_text):
    arr = []
    for line in input_text:
       arr.append([int(x) for x in line]) 

    return np.array(arr)

# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8


def increment_grid(grid):
    grid[grid == 9] = 0
    return grid + 1

def expand_input(grid):
    grids = []
    grids.append(grid)
    for i in range(1,9):
        grids.append(increment_grid(grids[i-1].copy()))

    rows = []
    for i in range(5):
        rows.append(np.concatenate([grids[i],
                                    grids[i+1],
                                    grids[i+2],
                                    grids[i+3],
                                    grids[i+4]], axis=1))

    expanded = np.concatenate([rows[0], rows[1], rows[2] ,rows[3] ,rows[4]])

    # print(expanded.shape)
    # print(expanded)

    return expanded
    

def index_out_of_bound(x,y,rows,cols):
    return x < 0 or x >= cols or y < 0 or y >= rows 

def get_neighbours(pos, max_rows, max_cols):
    row = pos[0]
    col = pos[1]
    neighbours = []
    if(row < max_rows-1):
        neighbours.append((row+1, col))
    if(col < max_cols-1):
        neighbours.append((row, col+1))
    if(row > 0):
        neighbours.append((row-1, col))
    if(col > 0):
        neighbours.append((row, col-1))

    return neighbours

    
# def find_paths(grid, pos, path):
#     max_rows = grid.shape[0]
#     max_cols = grid.shape[1]
#     row = pos[0]
#     col = pos[1]

#     grid[row, col, 1] = 1 # Set visited
#     path.append(grid[row,col,0])

#     if(pos == (max_rows-1, max_cols-1)):
#         print(path)
#     else:
#         for neighbour in get_neighbours(pos, max_rows, max_cols):
#             if(grid[neighbour[0], neighbour[1], 1] != 1): # not visited
#                 find_paths(grid, neighbour, path)

#     path.pop()
#     grid[row,col,1] = 0 # Set unvisited
        
def dfs(grid, currPos, destPos, visited, path, fullPath, currRisk):
    # get vertex, it is now visited and should be added to path
    node = grid[currPos]
    visited.append(currPos)
    path.append(node)

    # save current path if we found end
    if currPos == destPos:
        fullPath.append({"path": list(path), "risk": currRisk})

    for i in get_neighbours(currPos, grid.shape[0], grid.shape[1]):
        if i not in visited:
            dfs(grid, i, destPos, visited, path, fullPath, currRisk + node)

    # continue finding paths by popping path and visited to get accurate paths
    path.pop()
    visited.pop()

    if not path:
        return fullPath
def risks_copy(cost):
    rows = cost.shape[0]
    cols = cost.shape[1]
    tc = np.array([[0 for x in range(cols)] for x in range(rows)])
    
    tc[0][0] = cost[0][0]
    for i in range(1, cols):
        tc[i][0] = tc[i-1][0] + cost[i][0]
          
    # Initialize first row of tc array
    for j in range(1, rows):
        tc[0][j] = tc[0][j-1] + cost[0][j]
        
    # Construct rest of the tc array
    for i in range(1, cols):
        for j in range(1, rows):
            tc[i][j] = min(tc[i-1][j],
                           tc[i][j-1]) + cost[i][j]
    return tc[cols-1][rows-1]

def set_risks(grid):
    max_rows = grid.shape[0]
    max_cols = grid.shape[1]
    print(f'{max_cols} {max_rows}')
    # risks = np.zeros((max_rows, max_cols))
    risks = np.full((max_rows, max_cols), sys.maxsize)

    risks[0,0] = grid[0,0]

    for i, num in enumerate(grid[0,:]):
        if(i > 0):
            risks[0,i] = risks[0,i-1] + grid[0,i]

    for i, num in enumerate(grid[:,0]):
        if(i > 0):
            risks[i,0] = risks[i-1,0] + grid[i,0]

    for col in range(1,max_cols):
        for row in range(1,max_rows):
            old_val = risks[row,col]
            new_val = min(risks[row, col-1], risks[row-1, col]) + grid[row,col]
            if(new_val < old_val):
                risks[row, col] = new_val 
    return risks[max_rows-1, max_cols-1]
    
    
def dijkstra(grid):
    max_rows = grid.shape[0]
    max_cols = grid.shape[1]
    risks = np.full((max_rows, max_cols), 5000)
    risks[0,0] = grid[0,0]
    to_visit = deque()
    to_visit.appendleft((0, 0))
    paths = []

    visited = []

    while(len(to_visit) > 0):
    # for i in range(10):
        # print('---')
        pos = to_visit.pop()
        current = grid[pos]
        row = pos[0]
        col = pos[1]
        min = sys.maxsize

        visited.append(pos)

        neighbours = get_neighbours(pos, max_rows, max_cols)
        for neighbour in neighbours:
            # set neighbour risk
            risk_neighbour = risks[neighbour]
            new_risk = risks[pos] + grid[neighbour]
            if(new_risk < risk_neighbour):
                risks[neighbour] = new_risk
                if(neighbour in visited):
                    visited.remove(neighbour)
            if(neighbour not in visited and neighbour not in to_visit):
                to_visit.appendleft(neighbour)

    # print(risks)
    return risks[ max_rows-1, max_cols-1] - grid[0,0]

def dijkstra2(grid):
    max_rows = grid.shape[0]
    max_cols = grid.shape[1]
    to_visit = [(0,0,0)]

    risks = np.full((max_rows, max_cols), -1)

    while risks[-1, -1] == -1:
        risk, cur_row, cur_col = heapq.heappop(to_visit)

        for neighbour_row, neighbour_col in [(-1,0), (0,-1), (1,0),(0,1)]:
            next_row = cur_row + neighbour_row
            next_col = cur_col + neighbour_col

            if 0 <= next_row < max_rows and 0 <= next_col < max_cols and risks[next_row, next_col] == -1:
                new_value = grid[next_row, next_col] + risk
                risks[next_row, next_col] = new_value
                heapq.heappush(to_visit, (new_value, next_row, next_col))

    return risks[-1][-1]
        

def calculate_risks(grid):
    risks = dijkstra(grid)
    # risks = set_risks(grid)
    print(risks)
    
def expand_and_calculate(grid):
    new_grid = expand_input(grid)
    risks = dijkstra2(new_grid)
    print(risks)

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_sample2 = read_file(f'input/day{daynum}_sample_2.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
sample2 = interpret_input(day_sample2)
day = interpret_input(day_input)

# p1s = calculate_risks(sample)
# print(p1s)
# print(f"Time taken: {datetime.now() - starttime}")

# p1 = calculate_risks(day)
# print(p1)
# print(f"Time taken: {datetime.now() - starttime}")

# p2s = expand_and_calculate(sample)
# print(p2s)
# print(f"Time taken: {datetime.now() - starttime}")
    
p2 = expand_and_calculate(day)
print(p2)
print(f"Time taken: {datetime.now() - starttime}")
