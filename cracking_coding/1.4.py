from collections import Counter


def is_odd(n):
    return n % 2 != 0


def is_palindrome_permutation(a: str):
    a = a.replace(' ', '')
    counts = Counter(a)
    t = 1
    for v in counts.values():
        if is_odd(v):
            t -= 1
            if t < 0:
                return False
    return True


a = 'taco coa'
print(is_palindrome_permutation(a))

a = 'street'
print(is_palindrome_permutation(a))