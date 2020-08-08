def rotate_matrix_left(mat):
    # https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
    N = len(mat)
    for x in range(0, int(N / 2)):
        for y in range(x, N - x - 1):
            # store current cell in temp variable
            temp = mat[x][y]
            # move values from right to top: 3, 2, 1, 0
            mat[x][y] = mat[y][N - 1 - x]
            # move values from bottom to right:
            mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
            # move values from left to bottom
            mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
            # assign temp to left
            mat[N - 1 - y][x] = temp


def rotate_matrix_right(matrix):
    # https://leetcode.com/problems/rotate-image/discuss/778406/simple-python-solution
    k = 0
    while k < len(matrix) // 2:
        i = 0
        l = len(matrix) - 1
        while i < l - k * 2:
            matrix[i + k][l - k], \
            matrix[k][i + k], \
            matrix[l - i - k][k],\
            matrix[l - k][l - i - k] = \
                matrix[k][i + k], \
                matrix[l - i - k][k],\
                matrix[l - k][l - i - k],\
                matrix[i + k][l - k]
            i += 1
        k += 1


def displayMatrix(mat):
    N = len(mat)
    for i in range(0, N):

        for j in range(0, N):
            print(mat[i][j], end=' ')
        print("")


mat = [
    [1, 2, 3, 4 ],
    [5, 6, 7, 8 ],
    [9, 10, 11, 12 ],
    [13, 14, 15, 16 ]
]
displayMatrix(mat)
print()
rotate_matrix_right(mat)
displayMatrix(mat)
print()
rotate_matrix_left(mat)
displayMatrix(mat)