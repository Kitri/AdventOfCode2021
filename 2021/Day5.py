import common


day5_sample = read_file('input/day5_sample.txt')
day5_input = read_file('input/day5.txt')


def interpret_input(lines):
    all_coords = []

    for line in lines:
        points = line.split(' -> ')
        coords = [x.split(',') for x in points]
        all_coords.append(coords)

    return all_coords
    
def part1():
    coords = interpret_input(day5_input)
    
    coord_counts = {}
    
    for coord in coords:
        p1 = [int(x) for x in coord[0]]
        p2 = [int(x) for x in coord[1]]
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
    
        if(x1 == x2):
            print(f"vertical line {x1} : {y1} {y2}") 
            y_range = range(y1, y2+1) if y2 >= y1 else range(y2, y1+1)
            for y in y_range:
                if((x1,y) in coord_counts):
                    print(f"{x1,y}")
                    coord_counts[(x1,y)] += 1
                else:
                    coord_counts[(x1,y)] = 1
    
        elif(y1 == y2):
            print(f"horizontal line {y1}: {x1} {x2}") 
            x_range = range(x1, x2+1) if x2 >= x1 else range(x2, x1+1)
            for x in x_range:
                if( (x,y1) in coord_counts):
                    print(f"{x,y1}")
                    coord_counts[(x,y1)] += 1
                else:
                    coord_counts[(x,y1)] = 1
        # skip rest
        
    
    items = list(coord_counts.values())
    larger_than_1 = list(filter(lambda cnt: cnt > 1, items))
    
    print(len(larger_than_1))

def test(start, end):
#    start = [778,550]
#    end = [686,458]
    x_dir = "increase" if end[0] >= start[0] else "decrease"
    y_dir = "increase" if end[1] >= start[1] else "decrease"
    start_iter = start[0]
    end_iter = end[0]
    points = []
    points.append(start)
    if(x_dir == "increase"):
        for i in range(start_iter, end_iter):
            x = start[0] + 1
            y = start[1] + 1 if(y_dir == "increase") else start[1] - 1
            start = []
            start.append(x)
            start.append(y)
            points.append(start)
    elif(x_dir == "decrease"):
        for i in range(start_iter, end_iter, -1):
            x = start[0] - 1
            y = start[1] + 1 if(y_dir == "increase") else start[1] - 1
            start = []
            start.append(x)
            start.append(y)
            points.append(start)
    
    if(points[-1] != end):
        print(f"end points not the same! {points[-1]} vs {end}")

    return points


def get_new_list(start, end):
    #start = [8,0]
    #end = [0,8]
    
    x_dir = "increase" if end[0] >= start[0] else "decrease"
    y_dir = "increase" if end[1] >= start[1] else "decrease"
    
    diffs = abs(start[0] - end[0])
    diffs_y = abs(start[1] - end[0])
    print(diffs)
    print(diffs_y)
    iter_top = diffs if diffs > diffs_y else diffs_y
    
    points = []
    points.append(start)
    for i in range(0,iter_top):
        x = start[0] + 1 if(x_dir == "increase") else start[0] - 1
        y = start[1] + 1 if(y_dir == "increase") else start[1] - 1
        start = []
        start.append(x)
        start.append(y)
        points.append(start)
    return points

def part2():
    coords = interpret_input(day5_input)
    
    coord_counts = {}
    
    for coord in coords:
        p1 = [int(x) for x in coord[0]]
        p2 = [int(x) for x in coord[1]]
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
    
        if(x1 == x2):
          #  print(f"vertical line {x1} : {y1} {y2}") 
            y_range = range(y1, y2+1) if y2 >= y1 else range(y2, y1+1)
            for y in y_range:
                if((x1,y) in coord_counts):
                  #  print(f"{x1,y}")
                    coord_counts[(x1,y)] += 1
                else:
                    coord_counts[(x1,y)] = 1
    
        elif(y1 == y2):
          #  print(f"horizontal line {y1}: {x1} {x2}") 
            x_range = range(x1, x2+1) if x2 >= x1 else range(x2, x1+1)
            for x in x_range:
                if( (x,y1) in coord_counts):
                   # print(f"{x,y1}")
                    coord_counts[(x,y1)] += 1
                else:
                    coord_counts[(x,y1)] = 1
        else:
            print(f"Diagonal line {x1}, {y1} -> {x2}, {y2}")
            points = test(p1, p2)

            for point in points:
                x = point[0]
                y = point[1]
                if( (x,y) in coord_counts):
                    coord_counts[(x,y)] += 1
                else:
                    coord_counts[(x,y)] = 1
            # range x1 -> x2
            # range y1 -> y2
                
        
    
    items = list(coord_counts.values())
    larger_than_1 = list(filter(lambda cnt: cnt > 1, items))
    
    print(len(larger_than_1))
    
import numpy as np

def recurse(start, end, list_ret, x_dir, y_dir):
    if(start == end):
        return list_ret
    else:
        start[0] = start[0] + 1 if(x_dir == "increase") else start[0] - 1
        start[1] = start[1] + 1 if(y_dir == "increase") else start[0] - 1
        print(start)
        print(list_ret.append(start))
        recurse(start, end, list_ret, x_dir,y_dir)

    
                        
    
part2()

