class Solution2:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        prev = None
        result = 0
        for c in s:
            val = romans[c]
            if prev and val > prev:
                result -= 2 * prev
            else:
                prev = val
            result += val

        return result


class Solution:
    mapping = {
        'I':             1,
        'V':             5,
        'X':             10,
        'L':             50,
        'C':             100,
        'D':             500,
        'M':             1000,
    }
    def romanToInt(self, s: str) -> int:
        val = 0
        next_symbol_is_used = False
        for index in range(len(s) - 1):
            if next_symbol_is_used:
                next_symbol_is_used = False
                continue
            first_value = self.mapping[s[index]]
            next_value = self.mapping[s[index+1]]
            if first_value >= next_value:
                val += first_value
            else:
                val += next_value - first_value
                next_symbol_is_used = True
        if not next_symbol_is_used:
            val += self.mapping[s[-1]]
        return val