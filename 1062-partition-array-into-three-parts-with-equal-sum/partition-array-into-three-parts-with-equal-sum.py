class Solution:
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        count = 0
        current = 0

        for num in arr:
            current += num

            if current == target:
                count += 1
                current = 0

        return count >= 3