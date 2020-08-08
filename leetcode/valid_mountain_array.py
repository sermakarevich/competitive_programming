class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:
            return False
        m = 'i'
        prev = A[0]
        steps = 0
        for a in A[1:]:
            if m == 'i':
                if a > prev:
                    prev = a
                    steps += 1
                elif a == prev:
                    return False
                else:
                    if steps == 0:
                        return False
                    m = 'd'
            else:
                if a < prev:
                    prev = a
                else:
                    return False
        if m == 'i':
            return False
        return True

