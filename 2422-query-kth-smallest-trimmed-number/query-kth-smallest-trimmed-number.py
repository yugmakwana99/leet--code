class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []

        for k, trim in queries:
            arr = []

            for i in range(len(nums)):
                arr.append((nums[i][-trim:], i))

            arr.sort()

            answer.append(arr[k - 1][1])

        return answer