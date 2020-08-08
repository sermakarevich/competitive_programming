Sorting:
1. Selection sort - find index of minimal value and change its place with current index. Iterate over index from 0 to len(A) - 1. Complexity O(N**2)
2. Bubble sort - change places of two nearby values if next one is smaller than the current one. Do this while no values changes their places over the cycle. O(N**2)
3. Merge sort - split array into two parts until only 1 element left in a subarray. Merge back comparing two sorted aray element by element. Complexity O(N log N)
4. Quick sort - pick random index, iterate over values comparing each value to the index value - split array into less, equal, more. Repeat until no elements left in the subarrays. Complexity O(N log N)    

Binary search on sorted array - define low and high indexes, pick mid index and compare if its equal to target value. If target is higher recurse on mid+1:high, if lower - recurse on low:mid-1. If high < low - return None (element does not exist within the array).