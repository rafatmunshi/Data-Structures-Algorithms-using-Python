# 1. start with the column 0 in the recursion
# first check base case- if column n is reached, means solution is achieved and return true and print the current state of the board
# 2. a. try for all rows in this column-
# b. if the queen can be placed here- safe- mark this row and column with 1 , then recursively check for all other columns
# c. if all queens in next columns can be placed as well, this is the right position which would give correct solution so return true
# d. if backtracking happens means this position doesnt lead to solution, then unmark this row and column go to step a
# 3. If all rows tried in this column and no position gives solution, then return false to trigger backtracking.

N = 4

def isSafe(board, row, col):
    # Only check for left side
    # row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # lower diagonal
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQueens(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0
    return False


def printBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def NQueensProblem():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if not solveNQueens(board, 0):
        print("Solution for this N Queens problem doesnt exist")
        return False

    printBoard(board)
    return True

NQueensProblem()