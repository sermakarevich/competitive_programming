from collections import deque


class Solution:
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    open_ = set(pairs.keys())
    close_ = set(pairs.values())

    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        seq = deque()
        for symbol in s:
            if symbol in self.open_:
                seq.append(symbol)
            else:
                if len(seq) == 0:
                    return False
                last_symbol = seq.pop()
                if self.pairs[last_symbol] != symbol:
                    return False
        if len(seq):
            return False
        else:
            return True
