from common import file_parser as fp

"""
/          : 23352670 
  /a       : 94269
    /a/e   : 584
  /d       : 20967737
    /d/x   : 100


/
cd a-> /a/
"""
def part1(input_list):
    current_path = ''
    paths = {}
    num_acc = 0
    for line in input_list:
        if line.startswith('$ cd'):
            ch_dir = line.split(' ')[-1]
            if num_acc != 0:
                paths[current_path] = num_acc
                print('setting',current_path,num_acc)
                num_acc = 0
            if ch_dir == '..':
                current_path = current_path[:current_path.rindex('/')]
                if current_path == '':
                    current_path = '/'
            else:
                if current_path != '/' and ch_dir != '/':
                    ch_dir = '/' + ch_dir
                current_path += ch_dir
                paths.setdefault(current_path, 0)
            print(current_path)
        elif line == '$ ls':
            continue
        elif line.startswith('dir'):
            dir = line.split(' ')[-1]
            if current_path != '/':
                dir = '/' + dir

            paths.setdefault(current_path + dir, 0)
        else:
            num = int(line.split(' ')[0])
            num_acc += num
            print('calc num', num)
    
    paths[current_path] = num_acc
    print(paths)

    # todo: calc all dirs
    return 1
    
sample = fp.read_file_stripped('input/day7_sample.txt')
full = fp.read_file_stripped('input/day7.txt')

print(part1(sample))
