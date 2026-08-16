class Solution(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[0]]

        half = 1 << (n - 1)
        small = 1 << (2 * (n - 1))

        prev = self.specialGrid(n - 1)

        grid = [[0] * (half * 2) for _ in range(half * 2)]

        for i in range(half):
            for j in range(half):
                grid[i][j + half] = prev[i][j]
                grid[i + half][j + half] = prev[i][j] + small
                grid[i + half][j] = prev[i][j] + 2 * small
                grid[i][j] = prev[i][j] + 3 * small

        return grid