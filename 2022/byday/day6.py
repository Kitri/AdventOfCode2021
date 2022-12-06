def find_marker(input_str,num_letters):
    tracker = []
    counter = 0
    idx = 0

    for idx in range(len(input_str)):
        c = input_str[idx]

        if c in tracker:
            counter = 0
            c_index = tracker.index(c)
            tracker = tracker[c_index+1:]
        else:
            counter += 1

        tracker.append(c)

        if num_letters == len(tracker):
            return idx+1

sample = [x.strip() for x in open('input/day6_sample.txt').readlines()]
full = [x.strip() for x in open('input/day6.txt').readlines()]

assert find_marker(sample[0],4) == 7
assert find_marker(sample[1],4) == 5
assert find_marker(sample[2],4) == 6
assert find_marker(sample[3],4) == 10
assert find_marker(sample[4],4) == 11

print('Part1 ', find_marker(full[0],4))

assert find_marker(sample[0],14) == 19
assert find_marker(sample[1],14) == 23
assert find_marker(sample[2],14) == 23
assert find_marker(sample[3],14) == 29
assert find_marker(sample[4],14) == 26

print('Part2 ', find_marker(full[0],14))