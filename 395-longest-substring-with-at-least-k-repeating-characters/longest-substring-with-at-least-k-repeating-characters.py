class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or len(s) < k:
            return 0

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in count:
            if count[ch] < k:
                left = s.split(ch)
                return max(self.longestSubstring(part, k) for part in left)

        return len(s)