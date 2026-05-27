class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countDict=defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i])-ord('a')]+=1
            countDict[tuple(count)].append(s)

        return list(countDict.values())
        