from common import file_parser as fp
import sys, re

def part1(input_list):
    return 0


# graph = {
#     'AA': ['DD', 'II', 'BB'],
#     'BB': ['CC', 'AA'],
#     'CC': ['DD', 'BB'],
#     'DD': ['CC', 'AA', 'EE'],
#     'EE': ['FF', 'DD'],
#     'FF': ['EE', 'GG'],
#     'GG': ['FF', 'HH'],
#     'HH': ['GG'],
#     'II': ['AA', 'JJ'],
#     'JJ': ['II']
# }
# flows = {
#     'BB': 13,
#     'CC': 2,
#     'DD': 20,
#     'EE': 3,
#     'HH': 22,
#     'JJ': 21
# }


sample = fp.read_file_stripped('input/day16_sample.txt')
full = fp.read_file_stripped('input/day16.txt')

# print(part1(sample))

lines = [re.split('[\\s=;,]+', x) for x in full]
graph = {x[1]: set(x[10:]) for x in lines}
flows = {x[1]: int(x[5]) for x in lines if int(x[5]) != 0}
print(flows)
I = {x: 1<<i for i, x in enumerate(flows)}
# 1,2,4,7,16,32
# 1 << 0; 1 << 1; 1 << 2; 1 << 3
dist = {x: {y: 1 if y in graph[x] else float('+inf') for y in graph} for x in graph}
print()
print(dist)
print()
# Floyd
for k in dist:
    for i in dist:
        for j in dist:
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

def visit(v, minutes, state, flow, answer):
    answer[state] = max(answer.get(state, 0), flow)
    for u in flows:
        newminutes = minutes - dist[v][u] - 1
        if I[u] & state or newminutes <= 0: continue
        visit(u, newminutes, state | I[u], flow + newminutes * flows[u], answer)
    return answer    

# visited = visit('AA', 30, 0, 0, {})
# print(visited)
total1 = max(visit('AA', 30, 0, 0, {}).values())
visited2 = visit('AA', 26, 0, 0, {})
total2 = max(v1+v2 for k1, v1 in visited2.items() 
                   for k2, v2 in visited2.items() if not k1 & k2)
print(total1, total2)

# x << y Returns x with the bits shifted to the left by y places
# 5 << 1 = 10 = 5 * 2^1
# 5 << 2 = 20  = 5 * 2^2