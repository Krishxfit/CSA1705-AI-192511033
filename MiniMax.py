
def minimax(depth, node, maximizing, values):
    if depth == 3:
        return values[node]

    if maximizing:
        best = float('-inf')
        for i in range(2):
            best = max(best, minimax(depth + 1,
                      node * 2 + i, False, values))
        return best
    else:
        best = float('inf')
        for i in range(2):
            best = min(best, minimax(depth + 1,
                      node * 2 + i, True, values))
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value:", minimax(0, 0, True, values))
