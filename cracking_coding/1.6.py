def string_compression(s: str):
    s_ = []
    count = 0
    for i in s:
        if count == 0:
            s_.append(i)
            count += 1
        elif i == s_[-1]:
            count += 1
        else:
            s_.append(str(count))
            s_.append(i)
            count = 1
    s_.append(str(count))
    s_ = ''.join(s_)
    if len(s) <= len(s_):
        return s
    return s_


s = 'aabcccccaaa'
print(string_compression(s))
s = 'abfrgl'
print(string_compression(s))