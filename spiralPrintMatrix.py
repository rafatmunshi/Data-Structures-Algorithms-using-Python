arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
row = 4
col = 4


def spiralPrintMatrix(arr, row, col):
    '''
    x- starting row index
    y - starting col index
    row - ending row index
    col- ending column index
    '''
    x = 0
    y = 0
    while x < row and y < col:
        # print the first row
        for i in range(y, col):
            print(arr[x][i], end=" ")
        x += 1

        # print the last column
        for i in range(x, row):
            print(arr[i][col - 1], end=" ")
        col -= 1

        # print the last row
        if x < row:
            for i in range(col - 1, y - 1, -1):
                print(arr[row - 1][i], end=" ")
            row -= 1

        # print first column
        if y < col:
            for i in range(row - 1, x - 1, -1):
                print(arr[i][y], end=" ")
            y += 1


spiralPrintMatrix(arr, row, col)
