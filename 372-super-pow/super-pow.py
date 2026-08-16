class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337

        def power(x, n):
            result = 1

            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % MOD

                x = (x * x) % MOD
                n //= 2

            return result

        result = 1

        for digit in b:
            result = (power(result, 10) * power(a, digit)) % MOD

        return result