
import heapq

def gbfs(graph, h, start, goal):
    queue = [(h[start], start)]
    visited = set()

    while queue:
        _, node = heapq.heappop(queue)

        if node == goal:
            print("Goal found:", node)
            return

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (h[neighbor], neighbor))

    print("Goal not found")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

h = {'A': 5, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 0}

gbfs(graph, h, 'A', 'F')
