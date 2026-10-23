
def solve(board, row, n):
    if row == n:
        for r in board:
            print(" ".join(r))
        return True

    for col in range(n):
        if all(board[i][col] != 'Q' for i in range(row)) and \
           all(board[i][j] != 'Q'
               for i, j in zip(range(row-1, -1, -1),
                               range(col-1, -1, -1))) and \
           all(board[i][j] != 'Q'
               for i, j in zip(range(row-1, -1, -1),
                               range(col+1, n))):
            board[row][col] = 'Q'
            if solve(board, row + 1, n):
                return True
            board[row][col] = '.'

    return False

n = int(input("Enter N: "))
if n > 0 and solve([['.' for _ in range(n)] for _ in range(n)], 0, n):
    pass
else:
    print("No solution exists")
