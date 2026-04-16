class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_num = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_num:
                return [prev_num[diff], i]
            prev_num[num] = i