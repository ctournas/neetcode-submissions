from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = Counter(s1)
        l = 0
        r = len(s1)-1

        while r < len(s2):
            cs2 = Counter(s2[l:r+1])
            if cs1 == cs2:
                return True
            r+=1
            l+=1
        return False


        

        