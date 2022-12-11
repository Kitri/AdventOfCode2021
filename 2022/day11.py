from common import file_parser as fp
from functools import partial
from collections import deque

def apply_operation(sym, num1, num2):
    if num1 == 'old':
        num1 = num2

    match sym:
        case '+': return num1 + num2
        case '*': return num1 * num2

def parse_rules(input_list):
    rules = []
    monkey_items = []
    current_monkey = -1 
    line_counter = 0
    for line in input_list:
        if line.startswith('Monkey'):
            current_monkey += 1
            line_counter = 0
            rules.append({'inspection_score': 0})
        elif line_counter > 0:
            match line_counter:
                case 1: 
                    _, items = line.split(':')
                    levels = deque()
                    for item in items.split(','):
                        levels.append(int(item.strip()))
                    monkey_items.append(levels)
                    rules[current_monkey]['worry_levels'] = [int(x.strip()) for x in items.split(',')]
                case 2:
                    _, expr = line.split(' = ')
                    _,op,num = expr.split(' ')
                    if num != 'old':
                        num = int(num)
                    rules[current_monkey]['operation'] = partial(apply_operation, op, num)
                    rules[current_monkey]['op'] = op
                    rules[current_monkey]['opnum'] = num
                case 3:
                    _, test = line.split(': ')
                    _,_,num = test.split(' ')
                    rules[current_monkey]['test'] = int(num)
                case 4:
                    _, newmonkey = line.split(':')
                    x = newmonkey.split(' ')
                    rules[current_monkey]['true'] = int(x[-1])
                case 5:
                    _, newmonkey = line.split(':')
                    y = newmonkey.split(' ')
                    rules[current_monkey]['false'] = int(y[-1])

        line_counter += 1

    monkey_inspections = [0] * len(rules)
    
    return (rules, monkey_inspections, monkey_items)

def do_one_round(rules, with_relief=True, gcd = 1):
    for monkey in rules:
        for item in monkey['worry_levels']:
            worry_after_op = monkey['operation'](item) 
            monkey['inspection_score'] += 1
            worry_after_relief = int(worry_after_op / 3) if with_relief else int(worry_after_op%gcd)
            new_monkey = monkey['false']
            if worry_after_relief % monkey['test'] == 0:
                new_monkey = monkey['true']

            rules[new_monkey]['worry_levels'].append(worry_after_relief)
        monkey['worry_levels'].clear()
    return rules


def do_one_round_optimised(rules, inspection_scores, monkey_items, with_relief=True, gcd=1):
    for idx,monkey in enumerate(rules):
        while monkey_items[idx]:
            item = monkey_items[idx].popleft()
            inspection_scores[idx] += 1
            worry_after_op = monkey['operation'](item) 
            worry_after_relief = int(worry_after_op / 3) if with_relief else int(worry_after_op%gcd)
            new_monkey = monkey['false']
            if worry_after_op % monkey['test'] == 0:
                new_monkey = monkey['true']

            monkey_items[new_monkey].append(worry_after_relief)
    return (inspection_scores, monkey_items)

""" 
modulo rules (= means triple equals means congruent)
if a = b%n then b = a%n
if a = b%n & b = c%n then a = c%n
if a = b%n and c = d%n then a + c = (b + d) % n; and ac = bd % n
if ac = bc%nc then a = b%n
"""

def part1(monkey_rules):
    rules,_,_ = parse_rules(monkey_rules)
    for _ in range(20):
        rules = do_one_round(rules)

    scores = [r['inspection_score'] for r in rules]
    max1, max2 = sorted(scores)[-2:]
    return max1 * max2

def part2(monkey_rules, iterations):
    rules, monkey_inspections, monkey_items = parse_rules(monkey_rules)
    gcd = 1
    for r in rules:
        gcd *= int(r['test'])

    for _ in range(iterations):
        monkey_inspections, monkey_items = do_one_round_optimised(rules, monkey_inspections, monkey_items, False, gcd)

    max1, max2 = sorted(monkey_inspections)[-2:]
    return max1 * max2



sample = fp.read_file_stripped('input/day11_sample.txt')
full = fp.read_file_stripped('input/day11.txt')

assert part1(sample) == 10605
print('Part1', part1(full))

assert part2(sample, 20) == 10197
p2_sample_1000 = part2(sample, 1000)
assert p2_sample_1000 == 27019168, p2_sample_1000
p2_sample_10000 = part2(sample, 10000)
assert p2_sample_10000 == 2713310158, p2_sample_10000

print('Part2', part2(full, 10000))