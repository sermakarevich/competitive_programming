def find_min_path(m):
    # allowed moves are down and right
    stack = [
        (m[0][0], 0, 1),
        (m[0][0], 1, 0)
    ]
    rows = len(m) - 1
    cols = len(m[0]) - 1
    sums = []
    while stack:
        s, row, col = stack.pop()
        s += m[row][col]
        if row < rows:
            stack.append((s, row + 1, col))
        if col < cols:
            stack.append((s, row, col + 1))
        if row == rows and col == cols:
            sums.append(s)
    print(len(sums))
    return min(sums)


m = [
    [3, 2, 1, 3],
    [1, 9, 2, 3],
    [9, 1, 5, 4]
]

print(find_min_path(m))