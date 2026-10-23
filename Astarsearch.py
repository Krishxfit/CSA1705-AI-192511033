
import heapq

def astar(graph, h, start, goal):
    queue = [(h[start], 0, start)]
    visited = set()

    while queue:
        f, cost, node = heapq.heappop(queue)

        if node == goal:
            print("Minimum cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_cost = cost + weight
                    heapq.heappush(
                        queue,
                        (new_cost + h[neighbor], new_cost, neighbor)
                    )

    print("Goal not found")

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 5)],
    'E': [('F', 1)],
    'F': []
}

h = {'A': 4, 'B': 4, 'C': 3, 'D': 5, 'E': 1, 'F': 0}

astar(graph, h, 'A', 'F')
