class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        cT, window = {}, {}

        for c in t:
            cT[c] = 1 + cT.get(c, 0)

        have, need = 0, len(cT)
        res, resLen = [-1, -1], float('infinity')

        l = 0
        for r in range(len(s)):
            c = s[r]

            window[c] = 1 + window.get(c, 0)
            if c in cT and cT[c] == window[c]:
                have += 1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                window[s[l]] -= 1
                if s[l] in cT and window[s[l]] < cT[s[l]]:
                    have -= 1
                l+=1
        l, r = res
        print(l, r )
        return s[l:r+1] if resLen != float('infinity') else ""


        