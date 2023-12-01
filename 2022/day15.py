import sys
from common import file_parser as fp
import time

def parse_input(input_list):
    ret_list = []
    stripped = [line.replace('Sensor at x=','').replace(' closest beacon is at x=','').replace(' y=','') for line in input_list]
    for s in stripped:
        inner_list = []
        x = s.split(':')
        sensor = x[0].split(',')
        beacon = x[1].split(',')
        inner_list.append((int(sensor[0]), int(sensor[1])))
        inner_list.append((int(beacon[0]), int(beacon[1])))
        ret_list.append(inner_list)
    return ret_list

        
def part1(sensor_beacons, row):
    sensor_distances = []
    for sensor, beacon in sensor_beacons:
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) 
        sensor_distances.append((sensor, distance))
    
    filtered = [(s,d) for s,d in sensor_distances if ((row == s[1]) or (row > s[1] and row <= (s[1] + d)) or (row < s[1] and row >= (s[1] - d)))]


    min_pos = sys.maxsize
    max_pos = 0
    for sens, dist in filtered:
        delta = dist - abs(sens[1] - row)
        num_blocked = delta*2 + 1 
        starting_x = sens[0] - delta 
        # print("Blocking", sens, ":", starting_x, starting_x + num_blocked)
        for i in range(starting_x, starting_x + num_blocked):
            if i < min_pos:
                min_pos = i
            if i > max_pos:
                max_pos = i
    
    # print("Min to Max", min_pos, max_pos)

    return (max_pos - min_pos)


#(15, 17) (15, 25)
# min1 >= min2 and min1 <= min2
# max1 <= max2
def merge_ranges(min1, min2, max1, max2):
    new_min = min1
    new_max = max1

    # print(min1, max1, '-', min2, max2)

    if (min2 <= min1) and (max2 >= (min1-1) and max2 <= max1):
        new_min = min2
    elif (max2 >= max1) and (min2 <= (max1+1) and min2 >= min1):
        new_max = max2
    elif min2 < min1 and max2 > max1:
        new_min = min2
        new_max = max2
    elif min2 >= min1 and max2 <= max1: #no change
        return True, min1, max1
    elif min1 == min2 and max1 == max2: #no change
        return True, min1, max1
    else:
        return False,min1, max1
    return True,new_min, new_max



    # if (min1 >= min2 and min1 <= max2 and max1 > max2) or (max2 + 1 == min1):
    #     new_max = max1
    #     # minmaxcoords[idx][1] = max1
    # elif (max1 >= max2 and max1 <= max2 and min1 < min2) or (max1 + 1 == min2):
    #     new_min = min1
    #     # minmaxcoords[idx][0] = min1
    # elif min1 <= min2 and max1 >= max2:
    #     new_min = min1
    #     new_max = max1
    #     # minmaxcoords[idx] = [min1, max1]
    # else:
    #     return (False,min1, max1)
    # return (True,new_min, new_max)

def part2(sensor_beacons, high):
    low = 0

    sensor_distances = []
    for sensor, beacon in sensor_beacons:
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) 
        # if (beacon[0] >= low and beacon[0] <= high) and (beacon[1] >= low and beacon[1] <= high):
        sensor_distances.append((sensor, distance))
    # print(sensor_distances)
    
    # tuning frequency x * 4000000 + y
    for row in range(low, high+1):
        # print('Row', row)
        filtered = [(s,d) for s,d in sensor_distances if ((row == s[1]) or (row > s[1] and row <= (s[1] + d)) or (row < s[1] and row >= (s[1] - d)))]
        coords = set()
        minmaxcoords = []
        start_time = time.time()
        for sens, dist in filtered:
            # current_min = sys.maxsize
            # current_max = 0
            delta = dist - abs(sens[1] - row)
            num_blocked = delta*2 + 1 
            starting_x = sens[0] - delta 
            # print("Blocking", sens, dist, ":", starting_x, starting_x + num_blocked)
            current_min = starting_x
            current_max = starting_x + num_blocked - 1
            if len(minmaxcoords)==0:
                minmaxcoords.append((current_min, current_max))

            # print('Current range', current_min, current_max)
            
            for idx,(minX,maxX) in enumerate(minmaxcoords):
                merged, new_min, new_max = merge_ranges(current_min, minX, current_max, maxX)
                if merged:
                    minmaxcoords[idx] = (new_min, new_max)
                elif not merged and (current_min, current_max) not in minmaxcoords:
                    minmaxcoords.append((current_min, current_max))
                # print(minmaxcoords)
            # print('pre-merge',minmaxcoords)

        counter = 0
        retries = 0
        # print('not sorted', minmaxcoords)
        minmaxcoords = sorted(minmaxcoords)
        # print('sorted', minmaxcoords)
        while True:
            if counter >= len(minmaxcoords)-1:
                if len(minmaxcoords) > 1 and retries < 5:
                    counter = 0
                    retries += 1
                else:
                    break
            current_min_max = minmaxcoords[counter]
            next_min_max = minmaxcoords[counter+1]
            # print(current_min_max, next_min_max, counter, len(minmaxcoords))
            merged, new_min, new_max= merge_ranges(current_min_max[0], next_min_max[0], current_min_max[1], next_min_max[1])
            if merged:
                minmaxcoords[counter] = (new_min, new_max)
                minmaxcoords.remove(next_min_max)
            counter += 1

        if len(minmaxcoords) > 1:
            print(row, minmaxcoords)
            break


        # mid_time = time.time()
        # print(f"add to set: {(mid_time - start_time)*1000} ms")
        # # do something to determine if the empty pos is here
        # for col in range(low, high+1):
        #     if col not in coords:
        #         print('beacon found!', col, row)
        #         return (col * 4000000) + row 
        # print(row, 'row scanned')
        # end_time = time.time()

        # print(f"row scanned: {(end_time - mid_time)*1000} ms")


    return 0

sample = fp.read_file_stripped('input/day15_sample.txt')
full = fp.read_file_stripped('input/day15.txt')

parsed_sample = parse_input(sample)
parsed_full = parse_input(full)
# assert part1(parsed_sample, 10) == 26
# assert part1(parsed_full, 2000000) == 4793062

# assert part2(parsed_sample, 20) == 56000011
#print(part2(parsed_full, 4000000))

print((2706598 * 4000000) + 3253551)
