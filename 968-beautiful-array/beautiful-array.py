class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [1]

        left = self.beautifulArray((n + 1) // 2)
        right = self.beautifulArray(n // 2)

        left = [x * 2 - 1 for x in left]
        right = [x * 2 for x in right]

        return left + right