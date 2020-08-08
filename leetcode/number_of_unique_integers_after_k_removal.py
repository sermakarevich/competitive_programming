from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for val in arr:
            d[val] = d.get(val, 0) + 1
        d = sorted(d.items(), key=lambda x: -x[1])
        print(d)
        while d:
            _, c = d.pop()
            if k >= c:
                k -= c
            else:
                print('2', d, k)
                return len(d) + 1
        print('len d',len(d))
        return 0


a = [4, 3, 1, 1, 3, 3, 2]
a = [1, 2, 2, 2, 2]
k = 4

s = Solution()
print(s.findLeastNumOfUniqueInts(arr=a, k=k))
