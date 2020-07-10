from typing import List


def kadanes(nums: List[int]) -> int:
    gm = nums[0]
    lm = nums[0]
    for val in nums[1:]:
        lm = max(val, lm + val)
        gm = max(gm, lm)
    return gm

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(kadanes(nums))