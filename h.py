
def heuristic(node, goal):
    return abs(node - goal)

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

h = heuristic(start, goal)

print("Heuristic value:", h)
