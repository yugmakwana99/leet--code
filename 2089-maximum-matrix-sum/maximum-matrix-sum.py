class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        negative = 0
        minimum = float('inf')

        for row in matrix:
            for num in row:
                total += abs(num)

                if num < 0:
                    negative += 1

                minimum = min(minimum, abs(num))

        if negative % 2 == 1:
            total -= 2 * minimum

        return total