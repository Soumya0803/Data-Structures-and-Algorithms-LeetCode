class Solution:
    def uniquePaths(self, m, n):
        if m == n == 1: return 1

        matrix = [[0 for i in range(n)] for j in range(m)]

        # For the 1st row
        for i in range(1, n):
            matrix[0][i] = 1

        # For the 1st col
        for i in range(1, m):
            matrix[i][0] = 1

        # For other cell
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

        return matrix[m - 1][n - 1]