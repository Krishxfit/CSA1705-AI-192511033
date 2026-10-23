
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

def dfs(start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=" ")
        visited.add(start)
        for node in graph[start]:
            dfs(node, visited)

print("BFS:")
bfs('A')

print("\nDFS:")
dfs('A')
