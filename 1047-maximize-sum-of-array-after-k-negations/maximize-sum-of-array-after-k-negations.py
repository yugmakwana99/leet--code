class Solution:
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()

        i = 0

        # Convert negative numbers to positive
        while i < len(nums) and k > 0:
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            i += 1

        # If K is still odd, flip the smallest number
        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)