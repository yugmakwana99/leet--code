class Solution:
    def longestPalindrome(self, s):
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        ans = 0
        odd = False

        for freq in count.values():
            if freq % 2 == 0:
                ans += freq
            else:
                ans += freq - 1
                odd = True

        if odd:
            ans += 1

        return ans