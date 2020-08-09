def zero_matrix(m):
    rows = set()
    cols = set()
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 0:
                rows.add(r)
                cols.add(c)
    for r in rows:
        for c in range(len(m[0])):
            m[r][c] = 0
    for c in cols:
        for r in range(len(m)):
            m[r][c] = 0


def displayMatrix(mat):
    N = len(mat)
    for i in range(0, N):

        for j in range(0, N):
            print(mat[i][j], end=' ')
        print("")


mat = [
    [0, 2, 3, 4 ],
    [5, 6, 7, 8 ],
    [9, 4, 0, 3 ],
    [3, 4, 5, 6 ]
]

displayMatrix(mat)
print()
zero_matrix(mat)
displayMatrix(mat)