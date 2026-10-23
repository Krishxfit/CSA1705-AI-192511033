
from collections import deque

def water_jug():
    capacity = (4, 3)
    target = 2
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)

        if a == target or b == target:
            print("Goal reached!")
            return

        next_states = [
            (capacity[0], b), (a, capacity[1]),
            (0, b), (a, 0),
            (a - min(a, capacity[1] - b),
             b + min(a, capacity[1] - b)),
            (a + min(b, capacity[0] - a),
             b - min(b, capacity[0] - a))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

water_jug()
