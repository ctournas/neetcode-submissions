class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        my_d = {}

        for num in nums:
            my_d[num] = 1 + my_d.get(num, 0)

        for num, cnt in my_d.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0 ,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        