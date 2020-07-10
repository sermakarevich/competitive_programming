def max_product_array(nums):
    min_p, max_p, ans = nums[0], nums[0], nums[0]
    for val in nums[1:]:
        max_p, min_p = max(val, max_p * val, min_p * val), min(val, max_p * val, min_p * val)
        ans = max(ans, max_p)
    return ans


nums = [-1, 2, 3 -6, -12]
print(max_product_array(nums))