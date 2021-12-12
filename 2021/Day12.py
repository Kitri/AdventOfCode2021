import common
import numpy as np
import functools
from datetime import datetime
from common import read_file
from enum import Enum
import collections
import copy

daynum = 12 # set to number

class CaveType(Enum):
     START = 1
     END = 2
     BIG = 3
     SMALL = 4

     @classmethod
     def can_revisit(cls, cavetype):
         return cavetype == cls.BIG
 
     @classmethod
     def determine_type(cls, cavetype):
         if(cavetype == "start"):
             return cls.START
         elif(cavetype == "end"):
             return cls.END
         elif(cavetype.isupper()):
             return cls.BIG
         else:
             return cls.SMALL

class Cave:
    def __init__(self, name, cave_type):
        self.name = name
        self.cave_type = cave_type
        self.children = []
        self.visited = False

    def __str__(self):
        return f"Cave {self.name} : {self.cave_type}"

    def __eq__(self, obj):
        return self.name == obj.name and self.cave_type == obj.cave_type

    def __hash__(self):
        return hash(self.name)

    def add_child(self, cave):
        self.children.append(cave)

    def has_children(self):
        return len(self.children) > 0

    def visit(self):
        if(self.cave_type != CaveType.BIG):
            self.visited = True


def interpret_input(input_text):
    caves = []
    paths = {}

    cave_index = 1
    start_cave = Cave('start', CaveType.START)
    caves.append(start_cave)
    for line in input_text:
        a,b = line.split('-')
        if(a == "end" or b == "start"):
             x = a
             a = b
             b = x
        a_type = CaveType.determine_type(a)
        b_type = CaveType.determine_type(b)

        a_cave = Cave(a, a_type)
        b_cave = Cave(b, b_type)

        if(a_cave not in caves):
            caves.append(a_cave)
        if(b_cave not in caves):
            caves.append(b_cave)

        if(a_cave not in paths):
            paths[a_cave] = []

        if(b_cave not in paths and b_type != CaveType.END):
            paths[b_cave] = []

        if(b_type != CaveType.END and a_type != CaveType.START):
            paths[b_cave].append(a_cave)

        paths[a_cave].append(b_cave)

    return (caves, paths)
        
def str_caves(listy):
    names = [x.name for x in listy]
    return ','.join(names)

def str_map_caves(mappy):
    names = [str_caves(x) for y, x in mappy.items()]
    return names
    
def print_caves_and_paths(mappy):
    (caves, paths) = mappy
    print(str_caves(caves))
        
    for x,y in paths.items():
        path = str_caves(y)
        print(f'{x} - {path}')

def build_path(input_map):
    (caves, paths) = input_map
    start = caves[0]
    starting_path = paths[start]
    # print(f'starting at: {str_caves(starting_path)}')
    all_the_paths = {}  
    # initialise
    for i, cave in enumerate(starting_path):
        all_the_paths[i] = []
        all_the_paths[i].append(start)
        all_the_paths[i].append(cave)

    last_index = len(all_the_paths) - 1

    # iterate
    counter = 0
    # for loop in range(6):
    while(counter != len(all_the_paths)):
        counter = 0
        for i in list(all_the_paths):
            last_path = all_the_paths[i][-1]
            if(last_path.cave_type != CaveType.END):
                if(last_path in paths):
                    children = [x for x in paths[last_path] if (x not in all_the_paths[i] or x.cave_type == CaveType.BIG)]
                    if(len(children) == 0):
                         all_the_paths.pop(i)

                    for j, child in enumerate(children):
                        # print(f'{i} {j} {child}')
                        if(j == 0):
                            # if(child.cave_type == CaveType.BIG or child not in all_the_paths[i]):
                            all_the_paths[i].append(child)
                        else:
                            copy_path = all_the_paths[i][:-1]
                            if(child.cave_type == CaveType.BIG or child not in copy_path):
                                last_index += 1
                                all_the_paths[last_index] = copy_path
                                all_the_paths[last_index].append(child)
                else:
                    all_the_paths.pop(i)
            else:
                counter +=1
        # print(f'count {counter}')

    # [print(x) for x in str_map_caves(all_the_paths)]

    
    return counter

def has_2_small_cave_visits(visited, cave):
     small_caves = [x.name for x in visited if x.cave_type == CaveType.SMALL]
     set_sc = set(small_caves)
     return len(small_caves) != len(set_sc)

     
def may_I_visit(visited, cave):
     if(cave.cave_type == CaveType.SMALL):
          if(cave in visited and has_2_small_cave_visits(visited, cave)):
               return False
          else:
               return True

     else:
          return True
     
def build_path_visit_small_caves(input_map):
    (caves, paths) = input_map
    start = caves[0]
    starting_path = paths[start]
    # print(f'starting at: {str_caves(starting_path)}')
    all_the_paths = {}  
    # initialise
    for i, cave in enumerate(starting_path):
        all_the_paths[i] = []
        all_the_paths[i].append(start)
        all_the_paths[i].append(cave)

    last_index = len(all_the_paths) - 1

    # iterate
    counter = 0
    # for loop in range(9):
    while(counter != len(all_the_paths)):
        counter = 0
        for i in list(all_the_paths):
            last_path = all_the_paths[i][-1]
            if(last_path.cave_type != CaveType.END):
                if(last_path in paths):
                    children = [x for x in paths[last_path] if may_I_visit(all_the_paths[i], x)]
                    if(len(children) == 0):
                         all_the_paths.pop(i)

                    for j, child in enumerate(children):
                        # print(f'{i} {j} {child}')
                        if(j == 0):
                            # if(child.cave_type == CaveType.BIG or child not in all_the_paths[i]):
                            all_the_paths[i].append(child)
                        else:
                            copy_path = all_the_paths[i][:-1]
                            # if(child.cave_type == CaveType.BIG or child not in copy_path):
                            if(may_I_visit(copy_path, child)):
                                last_index += 1
                                all_the_paths[last_index] = copy_path
                                all_the_paths[last_index].append(child)
                else:
                    all_the_paths.pop(i)
            else:
                counter +=1
        # print(f'count {counter}')

    # [print(x) for x in str_map_caves(all_the_paths)]

    return counter

def part1_sample(input_arr):
    # print_caves_and_paths(input_arr)
    num_rows = build_path(input_arr)
    return num_rows

def part1(input_arr):
    # print_caves_and_paths(input_arr)
    num_rows = build_path(input_arr)
    return num_rows

def part2_sample(input_arr):
    # print_caves_and_paths(input_arr)
    num_rows = build_path_visit_small_caves(input_arr)
    return num_rows

def part2(input_arr):
    # print_caves_and_paths(input_arr)
    num_rows = build_path_visit_small_caves(input_arr)
    return num_rows

     
     
starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_sample_med = read_file(f'input/day{daynum}_sample_med.txt')
day_sample_lg = read_file(f'input/day{daynum}_sample_lg.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
sample_med = interpret_input(day_sample_med)
sample_lg = interpret_input(day_sample_lg)
day = interpret_input(day_input)

sm = part1_sample(sample)
print(f'sm: {sm}')

med = part1_sample(sample_med)
print(f'med: {med}')

lg = part1_sample(sample_lg)
print(f'lg: {lg}')

p1 = part1(day)
print(f"full: {p1}")
print(f"Time taken: {datetime.now() - starttime}")

p2_sm = part2_sample(sample)
print(f'sm: {p2_sm}')

p2_med = part2_sample(sample_med)
print(f'med: {p2_med}')

p2_lg = part2_sample(sample_lg)
print(f'lg: {p2_lg}')
    
p2 = part2(day)
print(f"full: {p2}")
print(f"Time taken: {datetime.now() - starttime}")
