class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cd = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1

            cd[tuple(count)].append(s)
        return list(cd.values())