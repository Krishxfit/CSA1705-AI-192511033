
def is_safe(graph, colors, node, color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def map_coloring(graph, m, colors, node=0):
    if node == len(graph):
        return True

    for color in range(1, m + 1):
        if is_safe(graph, colors, node, color):
            colors[node] = color

            if map_coloring(graph, m, colors, node + 1):
                return True

            colors[node] = 0

    return False

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors = [0] * len(graph)
names = ["Red", "Green", "Blue"]

if map_coloring(graph, 3, colors):
    for i, color in enumerate(colors):
        print("Region", i, ":", names[color - 1])
else:
    print("No solution exists")
