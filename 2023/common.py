import itertools
import math
import heapq
from collections import deque

# Function to read input from a file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Function to convert a list of strings to a list of integers
def convert_to_integers(data):
    return [int(item) for item in data]

# Function for finding the two numbers that sum to a target in a list
def find_two_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return num, complement
        seen.add(num)
    return None

# Function to generate permutations of a list
def generate_permutations(items):
    return list(itertools.permutations(items))

# Function to calculate the factorial of a number
def calculate_factorial(n):
    return math.factorial(n)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function for inorder tree traversal
def inorder_traversal(root):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.value)
        result += inorder_traversal(root.right)
    return result

# Function for preorder tree traversal
def preorder_traversal(root):
    result = []
    if root:
        result.append(root.value)
        result += preorder_traversal(root.left)
        result += preorder_traversal(root.right)
    return result

# Function for postorder tree traversal
def postorder_traversal(root):
    result = []
    if root:
        result += postorder_traversal(root.left)
        result += postorder_traversal(root.right)
        result.append(root.value)
    return result


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function for breadth-first search (BFS) on a tree
def bfs(root):
    result = []
    if root:
        queue = deque([root])
        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return result

# Function for depth-first search (DFS) on a tree
def dfs(root):
    result = []
    if root:
        stack = [root]
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
    return result


## DFS and BFS without class

# Function for breadth-first search (BFS) on a graph represented as an adjacency list
def bfs(graph, start):
    visited = set()
    result = []
    queue = deque([start])

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.add(current)
            result.append(current)
            queue.extend(graph[current] - visited)

    return result

# Function for depth-first search (DFS) on a graph represented as an adjacency list
def dfs(graph, start):
    visited = set()
    result = []

    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph[node] - visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return result


# Function for Dijkstra's algorithm on a graph represented as an adjacency list
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Function for A* algorithm on a graph represented as an adjacency list
def astar(graph, start, goal, heuristic):
    open_set = [(0 + heuristic(start, goal), 0, start)]
    came_from = {}

    while open_set:
        _, current_cost, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in came_from or new_cost < came_from[neighbor]:
                came_from[neighbor] = current_node
                heapq.heappush(open_set, (new_cost + heuristic(neighbor, goal), new_cost, neighbor))

    return None  # No path found



def examples():
    # Read input from a file
    input_data = read_input('input.txt')

    # Convert strings to integers
    int_data = convert_to_integers(input_data)

    # Find two numbers that sum to a target
    target_sum = 2020
    result = find_two_sum(int_data, target_sum)
    print(f"Two numbers that sum to {target_sum}: {result[0]} and {result[1]}")

    # Generate permutations of a list
    items = [1, 2, 3]
    permutations = generate_permutations(items)
    print(f"Permutations of {items}: {permutations}")

    # Calculate factorial of a number
    factorial_result = calculate_factorial(5)
    print(f"Factorial of 5: {factorial_result}")

    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Inorder traversal
    inorder_result = inorder_traversal(root)
    print(f"Inorder Traversal: {inorder_result}")

    # Preorder traversal
    preorder_result = preorder_traversal(root)
    print(f"Preorder Traversal: {preorder_result}")

    # Postorder traversal
    postorder_result = postorder_traversal(root)
    print(f"Postorder Traversal: {postorder_result}")

    # Create a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Breadth-first search
    bfs_result = bfs(root)
    print(f"BFS Result: {bfs_result}")

    # Depth-first search
    dfs_result = dfs(root)
    print(f"DFS Result: {dfs_result}")

    # Create a sample graph represented as an adjacency list
    graph = {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F', 'G'},
        'D': {'B'},
        'E': {'B', 'H'},
        'F': {'C'},
        'G': {'C'},
        'H': {'E'}
    }

    # Breadth-first search
    bfs_result = bfs(graph, 'A')
    print(f"BFS Result: {bfs_result}")

    # Depth-first search
    dfs_result = dfs(graph, 'A')
    print(f"DFS Result: {dfs_result}")


    # Create a sample graph represented as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 3, 'E': 1},
        'C': {'A': 4, 'F': 2, 'G': 5},
        'D': {'B': 3},
        'E': {'B': 1, 'H': 2},
        'F': {'C': 2},
        'G': {'C': 5},
        'H': {'E': 2}
    }

    # Dijkstra's algorithm
    dijkstra_result = dijkstra(graph, 'A')
    print(f"Dijkstra's Shortest Paths: {dijkstra_result}")

    # A* algorithm with a simple heuristic function
    heuristic_function = lambda node, goal: 0  # Replace with an actual heuristic function
    astar_result = astar(graph, 'A', 'H', heuristic_function)
    print(f"A* Shortest Path: {astar_result}")