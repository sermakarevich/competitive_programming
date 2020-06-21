from random import randint

from algorithms.array import create_array
from algorithms.mergesort import merge_sort


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def binary_search_2(arr, low, high, val):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return binary_search_2(arr, low, mid-1, val)
        elif arr[mid] < val:
            return binary_search_2(arr, mid+1, high, val)
    else:
        return -1


# Test array
arr = create_array(size=10)
x = arr[randint(0, len(arr) - 1)]

# Function call
sorted_array = merge_sort(arr)
result = binary_search_2(sorted_array, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")