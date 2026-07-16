class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = r = 0
        rep = {}

        while r < len(s):
            if s[r] in rep:
                l = max(rep[s[r]]+1, l)

            res = max(res, r-l+1)
            rep[s[r]] = r

            r += 1
        
        return res