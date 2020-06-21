from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        """
        for left_index in range(len(nums) - 1):
            for right_index in range(left_index+1, len(nums)):
                if nums[left_index] + nums[right_index] == target:
                    return [left_index, right_index]


class Solution(object):
    def twoSum(self, nums, target):
        seen_dict = {}
        for i, n in enumerate(nums):
            if not n in seen_dict:
                seen_dict[n] = i

            if seen_dict.get(target - n) and seen_dict[target - n] != i:
                return [seen_dict[target - n], i]
