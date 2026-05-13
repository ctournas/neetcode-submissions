class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res = []

        for i in range(len(nums)):
            if len(nums[i:i+k]) != k:
                break
            res.append(max(nums[i:i+k]))
            
        return res
        