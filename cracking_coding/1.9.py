def is_substring(a: str, b: str):
    return a in b


def string_rotation(a: str, b: str):
    return is_substring(a, b+b)


a = 'waterbottle'
b = 'erbottlewat'
print(string_rotation(a, b))