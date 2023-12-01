
import common.file_parser as fp

# dir_sizes = {
# }

# dir_hierarchy = {

# }

# """
# - / (dir)  | 23352670
#   - a (dir) | 94296
#     - e (dir) | 584
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir) | 24933642
#     - x (dir) | 100
#       - z (file, size=100)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)"""

# commands = []
# def part1(input_val):
#     print('Part 1')

#     iterating_dir = ''
#     current_dir = ''
#     for line in input_val:
#         if line.startswith('$'):
#             if 'cd' in line:
#                 _,_, name = line.split(' ')
#                 if name != '..' and name not in dir_sizes:
#                     dir_sizes[name] = []
#                     dir_hierarchy[name] = []
#                 current_dir = name
#                 iterating_dir = ''
#                 # print('cd', current_dir)
#                 commands.append(name)
#             elif 'ls' in line:
#                 iterating_dir = current_dir
#                 # print('setting iter', iterating_dir)
#         else:
#             if 'dir' not in line:
#                 size, _ = line.split(' ')
#                 # print('adding size', size)
#                 dir_sizes[iterating_dir].append(int(size))
#             else:
#                 _,dir_name = line.split(' ')
#                 dir_sizes[iterating_dir].insert(0,dir_name)
#                 dir_hierarchy[iterating_dir].append(dir_name)

#     for dir,sizes in dir_sizes.items():
#         x = 0
#         dirs = []
#         for s in sizes:
#             if isinstance(s,int):
#                 x += s
#             else:
#                 dirs.append(s)

#         dir_sizes[dir] = dirs + [x]

#     for dir,hierarchy in dir_hierarchy.items():
#         dir_hierarchy[dir] = {x: dir_sizes[x] for x in hierarchy}

#     print(dir_sizes)


#     print(walk(dir_sizes,'/'))





# def walk(dir_sizes,current_dir,acc):
#     for idx,x in enumerate(dir_sizes[current_dir]):
#         if not isinstance(x, int):
#             dir_sizes = walk(dir_sizes, x, 0)
#             numsum = 0
#             dirlist = []
#             for num in dir_sizes[current_dir]:
#                 if isinstance(num, int):
#                     numsum += num
#                 else:
#                     dirlist.append(num)
#             dir_sizes[current_dir] = dirlist + [numsum]
#         else:
#             return walk(dir_sizes, current_dir, x)
#         print('list',dir_sizes)


#     return dir_sizes


    
#     # for dir,hierarchy in dir_hierarchy.items():
#     #     if(len(hierarchy) != 0):
#     #         for d in hierarchy:


#     # print(dir_sizes)
#     # print(dir_hierarchy)
#     # print(dir_hierarchy.keys())
#     # print(commands)

#     # print(find_value(dir_sizes['a'],'a',dir_hierarchy, dir_sizes))
#     # print(find_value(dir_sizes['e'],'e',dir_hierarchy, dir_sizes))
#     # print(find_value(dir_sizes['d'],'d',dir_hierarchy, dir_sizes))
#     # print(find_value(dir_sizes['/'],'/',dir_hierarchy, dir_sizes))
#     # for x in get_all_keys(dir_hierarchy,dir_sizes,0):
#     #     print(x)

#     return 0       





# def find_value(acc, dir, dir_hierarchy):
#     if dir in dir_hierarchy:
#         return find_value(acc + dir_hierarchy[dir], )

# def get_all_keys(d,dir_sizes,acc):
#     for key, value in d.items():
#         yield acc + dir_sizes[key]
#         if isinstance(value, dict):
#             yield from get_all_keys(value,dir_sizes,acc+dir_sizes[key])

# def part2(input_val):
#     print('Part 2')
#     return 0


paths = {'/':0}
def part1_1(input_val):

    working_dir = '/'
    running_sum = 0
    for line in input_val:
        if line.startswith('$ cd'):
            _,_,dir = line.split(' ')

            # set paths[/] = 0
            # wd = '/' 
            # paths[/] += running_sum
            # wd = '/a'
            # paths[/a] += running_sum
            # wd = /a/e
            # wd = /a
            # wd = /
            if dir != '..':
                working_dir = dir
                paths.setdefault(working_dir, running_sum)
                running_sum = 0
                # dir = '/' + dir
        elif line.startswith('dir'):
            # set paths[/a] = 0
            # set paths[/d] = 0
            # set paths /a/e = 0
            _,dir_name = line.split(' ')
            paths.setdefault(working_dir + '/' + dir_name, 0)
        elif line.startswith('$ ls'):
            continue
        else:
            # inc sum twice
            # inc sum * 3
            print(line)
            size, _ = line.split(' ')
            print(size)
            running_sum += int(size)
    
    print(paths)



"""
    / : 0
    /a : 0
    /d : 0
"""



sample = fp.read_file_stripped('input/day7_sample.txt')
full = fp.read_file_stripped('input/day7.txt')

part1_1(sample)
# part2(sample)



