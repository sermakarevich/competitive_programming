class Solution:
    def rotate(self, matrix) -> None:
        iters = len(matrix) // 2
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1

        for i in range(iters):
            for ind in range(rows - i * 2):
                print(matrix[ind + i][cols - i])
                (
                    matrix[ind + i][cols - i],
                    matrix[rows - ind - i][cols - i],
                    matrix[ind + i][i],
                    matrix[i][cols - ind - i]
                ) = (
                    matrix[i][ind + i],
                    matrix[ind + i][cols - i],
                    matrix[rows - i][ind + i],
                    matrix[ind + i][cols - i]
                )

m = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.rotate(m)