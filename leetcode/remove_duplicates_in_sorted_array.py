from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                del nums[index]
            else:
                index += 1
        return len(nums)