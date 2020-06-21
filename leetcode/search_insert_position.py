from typing import List


class Solution:
    def binary_search(self, arr, low, high, val):
        mid = (high + low) // 2
        if high >= low:
            if arr[mid] == val:
                return mid
            elif arr[mid] > val:
                return self.binary_search(arr, low, mid - 1, val)
            else:
                return self.binary_search(arr, mid + 1, high, val)
        else:
            return mid + 1

    def searchInsert(self, nums: List[int], target: int) -> int:
        position = self.binary_search(nums, 0, len(nums) - 1, target)
        return position
