class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 1 if len(s) > 0 else 0
        seen = {}
        max_length_ = 0
        previous_symbol_position = 0
        for position, symbol in enumerate(s):
            if symbol not in seen or seen[symbol] < previous_symbol_position:
                seen[symbol] = position
                max_length_ += 1
            else:
                previous_symbol_position = seen[symbol]
                seen[symbol] = position
                if max_length_ > max_length:
                    max_length = max_length_
                max_length_ = position - previous_symbol_position
        if max_length_ >  max_length:
            max_length = max_length_
        return max_length