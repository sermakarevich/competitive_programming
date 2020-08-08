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


def count_distinct_(target, arr):
    combinations = [set() for i in (target + 1)]
    for i in range(1, target + 1):
        comb_ = set()
        for j in range(len(arr)):
            if i == arr[j]:
                comb_.add([arr[j]])
            if i > arr[j] and combinations[i - arr[j]] != [set()]:
                for set_value in combinations[i - arr[j]]:
                    comb_.add(
                        sorted(set_value + [arr[j]])
                    )
                if combinations[i] == [None]:
                    combinations[i] = sorted([combinations[i - arr[j]] + [arr[j]]])
                else:
                    if sorted([combinations[i - arr[j]] + [arr[j]]]) not in combinations[i]:
                        combinations[i] = []
        print(ways)
    return ways[target]