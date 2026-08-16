class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return len(nums)

        nums.sort()
        threshold = nums[-k]

        return sum(1 for num in nums if num < threshold)