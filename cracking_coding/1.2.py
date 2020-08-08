from collections import Counter


def is_permutation(a: str, b: str):
    a = sorted(a)
    b = sorted(b)
    return a == b


def is_permutation_counts(a: str, b: str):
    a = Counter(a)
    b = Counter(b)
    return a == b


a = 'ser'
b = 'res'
print(is_permutation(a, b))
print(is_permutation_counts(a, b))

a = 'mak'
b = 'makarevich'
print(is_permutation(a, b))
print(is_permutation_counts(a, b))
