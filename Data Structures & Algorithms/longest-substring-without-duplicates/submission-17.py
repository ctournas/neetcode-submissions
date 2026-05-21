class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        res = 0
        l=0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            
            res = max(res, len(s[l:r + 1]))
            mp[s[r]] = r
        
        return res

        