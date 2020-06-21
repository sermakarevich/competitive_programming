from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for num in nums[::-1]:
            if num == val:
                nums.pop(len(nums) - 1 - index)
            else:
                index += 1
        print(nums)
        return len(nums)


s = Solution()
s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
