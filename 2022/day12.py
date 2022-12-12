from common import file_parser as fp
import numpy as np
from collections import deque
import heapq
import sys



def find_distance(row, col, end_pos):
    end_r, end_c = end_pos
    return abs(end_r - row + end_c - col)

def find_valid_paths(current_pos, heightmap):
    row, col = current_pos
    up = (row-1, col)
    down = (row+1, col)
    left = (row, col-1)
    right = (row, col+1)
    len_row = len(heightmap)
    len_col = len(heightmap[0])
    current_height = heightmap[current_pos]['height']

    positions = []
    if row > 0 and heightmap[up]['visited'] == False and (current_height - heightmap[up]['height'] >= -1):
        positions.append(up)
    if row < len_row-1 and heightmap[down]['visited'] == False and (current_height - heightmap[down]['height'] >= -1):
        positions.append(down)
    
    if col > 0 and heightmap[left]['visited'] == False and (current_height - heightmap[left]['height'] >= -1):
        positions.append(left)
    if col < len_col-1 and heightmap[right]['visited'] == False and (current_height - heightmap[right]['height'] >= -1):
        positions.append(right)

    return positions

def find_valid_paths_reverse(current_pos, heightmap):
    row, col = current_pos
    up = (row-1, col)
    down = (row+1, col)
    left = (row, col-1)
    right = (row, col+1)
    len_row = len(heightmap)
    len_col = len(heightmap[0])
    current_height = heightmap[current_pos]['height']

    positions = []
    if row > 0 and heightmap[up]['visited'] == False and (heightmap[up]['height'] - current_height >= -1):
        positions.append(up)
    if row < len_row-1 and heightmap[down]['visited'] == False and (heightmap[down]['height'] - current_height >= -1):
        positions.append(down)
    
    if col > 0 and heightmap[left]['visited'] == False and (heightmap[left]['height']  - current_height>= -1):
        positions.append(left)
    if col < len_col-1 and heightmap[right]['visited'] == False and (heightmap[right]['height']  - current_height>= -1):
        positions.append(right)

    return positions

def get_final_path(heightmap, pos, acc, path):
    prev = heightmap[pos]['previous']
    if prev == None:
        return(acc, path)
    
    return get_final_path(heightmap, prev, acc + 1, path + '-' + heightmap[pos]['value'])

def get_final_path_reverse(heightmap, pos, acc, path):
    test = np.where(heightmap['previous'] == pos)
    print(test)
    all_next = [x for x in heightmap if x['previous'] == pos]
    print(all_next)
    if len(all_next) == 0:
        return(acc, path)
    
    return get_final_path_reverse(heightmap, all_next[0], acc + 1, path + '-' + heightmap[pos]['value'])

def part1(input_list, reverse=False):
    # heightmap = np.array([list(c) for c in input_list])

    start_pos = (0,0)
    end_pos = (0,0)

    not_visited = []
    heightmap = []
    for row, line in enumerate(input_list):
        rows = []
        for col, c in enumerate(line):
            priority = sys.maxsize
            height = ord(c)
            vis = False
            if c == 'S':
                if not reverse:
                    vis = True
                    priority = 0
                start_pos = (row, col)
                height = ord('a')
            elif c == 'E':
                if reverse:
                    vis = True
                    priority = 0
                end_pos = (row, col)
                height = ord('z')

            rows.append({'height': height, 'value': c, 'previous': None, 'visited': vis}) 
            heapq.heappush(not_visited, (priority, (row,col)))
        heightmap.append(rows)

    heightmap = np.array(heightmap)


    # heapq.heappush(not_visited, (0, start_pos))
    end_char = 'E' if not reverse else 'a'

    while(not_visited):
        current = heapq.heappop(not_visited)
        heightmap[current[1]]['visited'] = True
        if current[0] == sys.maxsize or heightmap[current[1]]['value'] == end_char:
            break
        new_distance = current[0] + 1
        neighbours = find_valid_paths(current[1], heightmap) if not reverse else find_valid_paths_reverse(current[1], heightmap)
        for n_pos in neighbours:
            neighbour = heightmap[n_pos]
            neighbour['previous'] = current[1]

            #least optimal way to update distance
            temp = deque()
            while(not_visited):
                p, (x,y) = heapq.heappop(not_visited)
                if n_pos == (x,y):
                    if p < new_distance:
                        new_distance = p
                    heapq.heappush(not_visited, (new_distance, n_pos))
                    break
                else: # put it back
                    temp.append((p, (x,y)))
            
            for t in temp:
                heapq.heappush(not_visited, t)

    # print(heightmap)


    if reverse:
        all_as = []
        min = sys.maxsize
        for iy, ix in np.ndindex(heightmap.shape):
            if heightmap[iy,ix]['value'] == 'a':
                all_as.append((iy,ix))
        for a in all_as:
            (cnt, path) = get_final_path(heightmap, a, 0,'')
            if cnt != 0:
                print(cnt, path)
                if cnt < min:
                    min = cnt
        return min

    # (cnt, path) = get_final_path(heightmap, end_pos, 0,'')
    # print(cnt, path)

    return cnt



sample = fp.read_file_stripped('input/day12_sample.txt')
full = fp.read_file_stripped('input/day12.txt')

# print(part1(sample))
print(part1(full, True))
