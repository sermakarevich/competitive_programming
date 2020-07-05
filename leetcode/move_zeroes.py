class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        extend = 0
        for position, num in enumerate(nums):
            print(position, num, nums)
            if num == 0:
                del nums[position - extend]
                extend += 1
        return nums.extend([0] * extend)


arr = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(arr)
print(arr)
