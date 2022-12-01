import common
import numpy as np
import functools
import sys
from datetime import datetime

from common import read_file

daynum = 17 # set to number


class Target:
    def __init__(self, x0, x1, y0, y1):
        self.x_from = x0
        self.x_to = x1
        self.y_from = y0
        self.y_to = y1

    def __str__(self):
        return f' ({self.x_from, self.y_to} -> {self.x_to, self.y_to}; {self.x_from, self.y_from} -> {self.x_to, self.y_from}'

    def check_in_target(self, pos):
        x_valid = self.x_from <= pos[0] <= self.x_to
        y_valid = self.y_from <= pos[1] <= self.y_to

        return x_valid and y_valid


# Rules to cater for:
# If velocity X has reached 0 and it's still left of target - trajectory fails
# If falling and pos goes below y_from - trajectory fails
# If pos.x > x_to - trajectory fails
# If first velocity.x > x_to - End iteration
class ProbeMover:
    def __init__(self, velocity, direction, pos, target):
        self.velocity = velocity
        self.direction = direction
        self.position = pos
        self.target = target
        self.failed_trajectory = False

    def __str__(self):
        return f'Pos: {self.position}, vel: {self.velocity}, dir: {self.direction}'

    # def is_out_of_range(self):
    #     return self.position[0] > self.target.x_to or \
    #         (self.direction == -1 and self.position[1] < self.target.y_from) or \
    #         (self.direction == -1 and self.position[0] < self.target.x_from and self.position[1] < self.target.y_from) or (self.velocity[0] == 0 and self.direction == -1)

    def move_by_x(self):
        self.position += (self.velocity[0],0)
        if(self.position[0] > self.target.x_to):
            self.failed_trajectory = True
        return self.target.check_in_target(self.position)

    def move_by_y(self):
        prev_y = self.position[1]
        self.position += (0, self.velocity[1])
        if(self.position[1] < prev_y and self.direction != -1):
            self.direction = -1
        if(self.direction == -1 and self.position[1] < self.target.y_from):
            self.failed_trajectory = True
        
        return self.target.check_in_target(self.position)

    def decrease_velocity(self):
        x_change = 1 if self.velocity[0] < 0 else -1
        x_change = 0 if self.velocity[0] == 0 else x_change
        self.velocity += (x_change, 0)
        if(self.velocity[0] == 0 and self.position[0] < self.target.x_from):
            self.failed_trajectory = True

    def increase_gravity(self):
        self.velocity += (0,-1)

        

def interpret_input(input_text):
    split_text = input_text[0].split(' ')
    x = split_text[2].split('..') #x=nn..nn,
    y = split_text[3].split('..') #y=nn..nn
    x_from = int(x[0][2:]) # [x=]nn
    x_to = int(x[1][:-1]) # nn[,]

    y_from = int(y[0][2:]) # [y=]nn
    y_to = int(y[1]) # nn

    return Target(x_from, x_to, y_from, y_to)


def send_probe(target, start_velocity):
    start_pos = np.array([0,0])
    move = ProbeMover(start_velocity, 1, start_pos, target)
                    

    reached_target = False
    failed_trajectory = False
    highest_y = 0
    
    # counter = 0
    while(not reached_target and not failed_trajectory): 
        reached_target = move.move_by_x()
        reached_target = move.move_by_y()
        if(move.position[1] > highest_y):
            highest_y = move.position[1]
        move.decrease_velocity()
        move.increase_gravity()
        failed_trajectory= move.failed_trajectory
        # counter += 1
        print(move)

    return (highest_y, reached_target, failed_trajectory, move)

#  velocity bounds: yfrom, -yfrom-1
def part1(target):
    # test = np.array([6,9])
    # highest_y, reached_target, failed_trajectory, move = send_probe(target, test)
    # print(highest_y)
    
    # velocity = np.array([0,1])
    velocity = (0,1)
    velocity = {
        'x': 0,
        'y': 1
    }
    
    highest_y = 0
    highest_velocity = (0,0)
    count_valids = 0

    end_condition = False
    while(not end_condition):
    # for i in range(20):
        # print(velocity)
        h_y, reached_target, failed_trajectory, move = send_probe(target, np.array([velocity['x'], velocity['y']]))
        velocity['y'] += 1
        if velocity['x'] > target.x_to+1:
            print('Initial Velocity goes too far')
            end_condition = True
        # print(move)
        if(reached_target):
            # print(f'higher: {highest_y} {move.position[1]}')
            highest_y = h_y
            highest_velocity = (velocity['x'],velocity['y']-1)
            count_valids += 1
        elif(failed_trajectory):
            velocity['x'] += 1
            # velocity['y'] = 0
    print(count_valids)

    return (highest_y, highest_velocity)


def part2_sample(input_arr):
    return input_arr

def part2(input_arr):
    return len(input_arr)

starttime = datetime.now()

day_sample = read_file(f'input/day{daynum}_sample.txt')
day_input = read_file(f'input/day{daynum}.txt')

sample = interpret_input(day_sample)
day = interpret_input(day_input)

# p1s = part1(sample)
# print(f'y = {p1s[0]}; velocity = {p1s[1]}')
# print(f"Time taken: {datetime.now() - starttime}")

# p1 = part1(day)
# print(f'y = {p1[0]}; velocity = {p1[1]}')
# print(f"Time taken: {datetime.now() - starttime}")

p2s = part1(sample)
print(p2s)
print(f"Time taken: {datetime.now() - starttime}")
    
# p2 = part2(day)
# print(p2)
# print(f"Time taken: {datetime.now() - starttime}")
