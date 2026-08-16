class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        nums.sort()
        n = len(nums)

        mid = (n - 1) // 2
        end = n - 1

        result = [0] * n

        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[mid]
                mid -= 1
            else:
                result[i] = nums[end]
                end -= 1

        nums[:] = result