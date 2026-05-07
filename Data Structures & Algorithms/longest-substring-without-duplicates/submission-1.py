class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        res = 0 


        while r < len(s):
            if s[r] in s[l:r]:
                l+=1
            else:
                res = max(res, len(s[l:r]))
                r+= 1
        
        return res+1 if s else 0


        