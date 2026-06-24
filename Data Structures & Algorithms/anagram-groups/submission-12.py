class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            res = [0] * 26
            for i in range(len(s)):
                res[ord(s[i])-ord("a")] += 1
            groups[tuple(res)].append(s)
        return list(groups.values())