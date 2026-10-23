
import heapq

def ucs(graph, start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node == goal:
            print("Minimum cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))

    print("Goal not found")

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

ucs(graph, 'A', 'F')
