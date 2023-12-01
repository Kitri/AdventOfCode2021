dist = [['INF']*4] * 4
dist[1][0] = 2
print(dist)
# [[2, 'INF', 'INF', 'INF'], 
#  [2, 'INF', 'INF', 'INF'], 
#  [2, 'INF', 'INF', 'INF'], 
#  [2, 'INF', 'INF', 'INF']]

n = 5
mda = [[0] * 3 for _ in range(5)]
mda[1][0] = 2
print(mda)