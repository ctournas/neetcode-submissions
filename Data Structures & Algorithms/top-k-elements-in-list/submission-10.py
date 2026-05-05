class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        frq = [[] for i in range(len(nums)+1)]

        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        for num, cnt in counter.items():
            frq[cnt].append(num)

        res = []
        for i in range(len(frq)-1, 0, -1):
            for num in frq[i]:
                res.append(num)
                if len(res) == k:
                    return res



        