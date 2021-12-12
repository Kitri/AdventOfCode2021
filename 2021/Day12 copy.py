import common
import numpy as np
import functools
from datetime import datetime
from common import read_file
from enum import Enum
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
        return f"Cave {self.name} : {self.cave_type}. Children: {[x.name for x in self.children]}"

    def add_child(self, cave):
        self.children.append(cave)

    def has_children(self):
        return len(self.children) > 0

    def visit(self):
        if(self.cave_type != CaveType.BIG):
            self.visited = True


def interpret_input(input_text):
    caves = {}
    for line in input_text:
        path = line.split('-')
        a = path[0]
        b = path[1]
        a_type = CaveType.determine_type(a)
        b_type = CaveType.determine_type(b)
        a_cave = Cave(a, a_type)
        b_cave = Cave(b, b_type)
        if(a not in caves):
            caves[a] = a_cave 
            
        caves[a].add_child(b_cave)
        if(b not in caves):
            caves[b] = b_cave 
        if(a_type == CaveType.BIG and b_type != CaveType.END):
            caves[b].add_child(a_cave)
        

    return [y for x,y in caves.items()]
        
    # big = CaveType.SMALL
    # canrevisit = CaveType.can_revisit(big)
    # print(canrevisit)

def build_path(cave, paths, index):
    if(cave.visited):
        return paths
    else:
        print(cave.name)
        if(cave.cave_type == CaveType.END):
            index += 1
            paths[index] = []
        cave.visit()
        paths[index].append(cave)
        for child in cave.children:
            paths[index].append(child)
            build_path(child, paths, index)
        return paths
        
def traverse(cave, route, index):
    if(cave.visited):
        return route
    else:
        cave.visit()
        print(cave.name)
        if(index not in route and index > 0):
            route[index] = route[index-1]
        route[index].append(cave.name)
        for (i, child) in enumerate(cave.children):
           traverse(child, route, index + i)
           route[index].append(child.name)
        return route

def copy_whole_cave(cave):
    new_cave = Cave(cave.name, cave.cave_type)
    for child in cave.children:
        c_c = Cave(child.name, child.cave_type)
        if(child.visited):
            c_c.visit()
        new_cave.add_child(c_c)
    return new_cave

def test_sm(input_arr):
    [print(x) for x in input_arr]
    start_filter = [x for x in input_arr if x.cave_type == CaveType.START]
    start_cave = start_filter[0]

    routes = {}
    last_index = 0
    for i, child in enumerate(start_cave.children):
        if(i not in routes):
            routes[i] = []
        start_cave.visit()
        routes[i].append(start_cave)
        child.visit()
        routes[i].append(child)
        last_index = i
    
    for j in range(2):
        counter = 0
        for key in list(routes):
            last_route = routes[key][-1]
            end_index = len(routes[key])
            # print(f'please no change {end_index}')
            if(last_route.cave_type != CaveType.END):
                print(f'route {last_route.name} - {last_route.has_children()}')
                unvisited_children = [x for x in last_route.children if not x.visited]
                # print(f'route {last_route.name}')
                # print(','.join([x.name for x in unvisited_children]))
                # print('new start')
                # print(','.join([x.name for x in new_start]))
                for (i,c) in enumerate(unvisited_children):
                    c.visit()
                    if(i == 0):
                        routes[key].append(c)
                    else:
                        last_index += 1
                        new_start = []
                        for ns in range(end_index):
                            new_start.append(copy_whole_cave(routes[key][ns]))
                        print('new start')
                        print(','.join([f'{x.name} {len(x.children)}' for x in new_start]))
                        routes[last_index] = new_start
                        routes[last_index].append(c)
                counter += 1
        print(f'count {counter}')
        

    for x,y in routes.items():
        print(x)
        for i in y:
            print(f'{i.name} {i.visited}')
            # for c in i.children:
            #     print(f'child {c.name} {c.visited}')
        
    return input_arr 

def part1_sample(input_arr):
    return input_arr

def part1(input_arr):
    return len(input_arr)

def part2_sample(input_arr):
    return input_arr

def part2(input_arr):
    return len(input_arr)

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_sample_med = read_file(f'input/day{daynum}_sample_med.txt')
day_sample_lg = read_file(f'input/day{daynum}_sample_lg.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
sample_med = interpret_input(day_sample_med)
sample_lg = interpret_input(day_sample_lg)
# day = interpret_input(day_input)

sm = test_sm(sample)
# [print(x) for x in sm]
#print(sm)

# med = test_sm(sample_med)
# print(med)

# lg = test_sm(sample_lg)
# print(lg)
# meta - ; to comment
# p1s = part1_sample(sample)
# print(p1s)
# print(f"Time taken: {datetime.now() - starttime}")

# p1 = part1(day)
# print(p1)
# print(f"Time taken: {datetime.now() - starttime}")

# p2s = part2_sample(sample)
# print(p2s)
# print(f"Time taken: {datetime.now() - starttime}")
    
# p2 = part2(day)
# print(p2)
# print(f"Time taken: {datetime.now() - starttime}")
