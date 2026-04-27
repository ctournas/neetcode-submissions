class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_d = defaultdict(list)
        res = []

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            my_d[tuple(count)].append(word)
        return list(my_d.values())