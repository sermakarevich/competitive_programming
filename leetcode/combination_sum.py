def count_distinct_ways_dp(target, arr):
    ways = [1] + [0] * target
    for i in range(1, target + 1):
        for j in range(len(arr)):
            if i >= arr[j]:
                ways[i] += ways[i - arr[j]]
        print(ways)
    return ways[target]


a = [1, 2]
t = 4
print(count_distinct_ways_dp(target=t, arr=a))
