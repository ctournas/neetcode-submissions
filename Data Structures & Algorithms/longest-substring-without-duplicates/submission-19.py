class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        r = 0 
        res = 0

        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)

            res = max(res, r-l+1)
            mp[s[r]] = r
            r+= 1
        return res

        
        