"""
The Fisher-Yates algorithm is remarkably similar to the brute force solution.
On each iteration of the algorithm, we generate a random integer between the current
index and the last index of the array.
Then, we swap the elements at the current index and the chosen index -
this simulates drawing (and removing) the element from the hat,
as the next range from which we select a random index will not include the most recently processed one.
 One small, yet important detail is that it is possible to swap an element with itself -
 otherwise, some array permutations would be more likely than others.
"""
import random


class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
