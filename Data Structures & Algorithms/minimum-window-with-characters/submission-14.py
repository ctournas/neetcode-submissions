class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, countS = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        need, have = len(countT), 0
        res, resLen = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            c = s[r]
            countS[c] = 1 + countS.get(c, 0)

            if c in countT and countT[c] == countS[c]:
                have += 1

            while need == have:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l+1

                countS[s[l]] -= 1    
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l+= 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
                


        
        