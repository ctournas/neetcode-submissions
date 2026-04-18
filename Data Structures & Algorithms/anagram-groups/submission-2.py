class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my = defaultdict(list)
        res = []
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] +=1
            my[tuple(count)].append(s)

        return list(my.values())

        


        