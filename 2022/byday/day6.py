def find_marker(input_str,num_letters):
    x = []
    counter = 0
    idx = 0
    for c in input_str:
        idx += 1
        if c not in x:
            counter += 1
            x.append(c)
        else:
            counter = 0
            c_index = x.index(c)
            
            x = x[c_index+1:]
            x.append(c)

        if len(x) == num_letters:
            return idx

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

print('Part1 ', find_marker(full[0],14))