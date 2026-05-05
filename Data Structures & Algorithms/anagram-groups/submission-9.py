class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter)-ord('a')] += 1
            dicti[tuple(count)].append(s)
        return list(dicti.values())
        