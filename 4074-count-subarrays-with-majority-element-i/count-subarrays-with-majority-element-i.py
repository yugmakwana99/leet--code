class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        answer = 0

        for i in range(n):
            count = 0

            for j in range(i, n):
                if nums[j] == target:
                    count += 1

                if 2 * count > j - i + 1:
                    answer += 1

        return answer