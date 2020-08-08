def drop_index(a, i):
    return [a[j] for j in range(len(a)) if j != i]


def is_one_edit(a: str, b: str):
    if a == b:
        return True
    a = list(a)
    b = list(b)
    if len(a) < len(b):
        a, b = b, a
    if len(a) > len(b):
        for i in range(len(a)):
            a_ = drop_index(a, i)
            if a_ == b:
                return True
    if len(a) == len(b):
        for i in range(len(a)):
            a_ = drop_index(a, i)
            b_ = drop_index(b, i)
            if a_ == b_:
                return True
    return False


a, b, = 'pale', 'ple'
print(is_one_edit(a, b))
a, b = 'pales', 'pale'
print(is_one_edit(a, b))
a, b = 'pale', 'bale'
print(is_one_edit(a, b))
a, b = 'pale', 'bae'
print(is_one_edit(a, b))

