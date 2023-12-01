from collections import defaultdict, deque
import sys

def sample_bfs_graph() -> dict:
    return {
        'A': ['B','C'],
        'B': ['D'],
        'C': ['E','F'],
        'D': [],
        'E': [],
        'F': []
    } # Traverse output A,B,C,D,E,F

def sample_dfs_graph() -> dict:
    return {
        'A': ['B','D'],
        'B': ['C'],
        'C': [],
        'D': ['E','F'],
        'E': [],
        'F': []
    } # Traverse output A,B,C,D,E,F

"""
BFS, Breadth-First Search, is a vertex-based technique 
for finding the shortest path in the graph. It uses a 
Queue data structure that follows first in first out. 
In BFS, one vertex is selected at a time when it is 
visited and marked then its adjacent are visited and 
stored in the queue. It is slower than DFS. 
"""
def bfs(start_node: str, graph: dict) -> list:
    visited: set = set()
    queue: deque = deque()
    visited_sequence: list = []

    queue.append(start_node)
    visited.add(start_node)

    while queue:
        current_node: str = queue.pop()
        visited_sequence.append(current_node)
        print(current_node, end=" ")

        adjacent_nodes: list = graph[current_node]
        for node in adjacent_nodes:
            if node not in visited:
                queue.appendleft(node)
                visited.add(node)
    
    return visited_sequence


"""
DFS, Depth First Search, is an edge-based technique. 
It uses the Stack data structure and performs two stages, 
first visited vertices are pushed into the stack, and 
second if there are no vertices then visited vertices are popped. 
"""
def DFSUtil(node: str, visited: set, graph: dict, visited_sequence: list):

    visited.add(node)
    visited_sequence.append(node)
    print(node, end=' ')

    adjacent_nodes = graph[node]
    for neighbour in adjacent_nodes:
        if neighbour not in visited:
            DFSUtil(neighbour, visited, graph, visited_sequence)

    return visited_sequence

def dfs(start_node: str, dfs_graph: dict) -> list:
    visited: set = set()

    return DFSUtil(start_node, visited, dfs_graph, [])


""" 
 - Finds the shortest path between all pairs of vertices in graph 
 - Original algorithm only provides the distances between vertices
 - Modification can allow to reconstruct path (next list)
 - https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
"""
def floyd_algorithm():
    vertices = [0,1,2,3]
    edges = {
        (0,2): -2, 
        (1,0): 4, 
        (1,2): 3,
        (2,3): 2, 
        (3,1): -1
    }
    dist = [[sys.maxsize] * len(vertices) for _ in range(len(vertices))]
    next = [[None] * len(vertices) for _ in range(len(vertices))]

    for edge, weight in edges.items():
        dist[edge[0]][edge[1]] = weight
        next[edge[0]][edge[1]] = edge[1]
    
    for v in vertices:
        dist[v][v] = 0
        dist[v][v] = v

    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                # can also do
                # dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]
    print(dist)
    print(next)
    return (dist, next)

def floyd_path(graph, u, v):
    if graph[u][v] == None:
        return []
    path = [u]
    while u != v:
        u = next[u][v]
        path.append(u)
    
    print(path)
    return path

dist, next = floyd_algorithm()
assert floyd_path(next, 3, 2) == [3,1,0,2]
assert floyd_path(next, 0, 3) == [0,2,3]

print()
print('BFS:', end='')
assert bfs('A', sample_bfs_graph()) == ['A','B','C','D','E','F']
print()

print('DFS: ', end='')
assert dfs('A', sample_dfs_graph()) == ['A','B','C','D','E','F']
print()
