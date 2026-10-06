class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)

        total = sum(nums)
        current = 0
        ans = []

        for num in nums:
            current += num
            total -= num
            ans.append(num)

            if current > total:
                break

        return ans