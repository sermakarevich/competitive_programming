def min_coin_change(target, arr):
    ways = [0] + [0] * target
    for i in range(target + 1):
        for j in range(len(arr)):
            if i >= arr[j]:
                if i == arr[j]:
                    ways[i] = 1
                elif ways[i] == 0 and ways[i - arr[j]] != 0:
                    ways[i] = ways[i - arr[j]] + 1
                elif ways[i] > 0 and ways[i - arr[j]] > 0:
                    ways[i] = min(ways[i], ways[i - arr[j]] + 1)
            print(ways)
    return ways[target]


a = [3, 5]
t = 22
print(min_coin_change(target=t, arr=a))
