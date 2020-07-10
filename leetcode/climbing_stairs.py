class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            for i in range(n-2):
                ans = a+b
                a, b = b, ans
                print(a, b, ans)
            return ans


s = Solution()
print(s.climbStairs(6))
