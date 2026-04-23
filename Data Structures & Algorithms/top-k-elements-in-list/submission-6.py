class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_d = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            my_d[n] = 1 + my_d.get(n, 0)

        for n, cnt in my_d.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res