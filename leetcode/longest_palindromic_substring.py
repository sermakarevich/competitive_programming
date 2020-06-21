class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = s[0] if len(s) > 0 else ''
        len_max = len(max_palindrome)
        for char_position_left in range(len(s) - 1):
            for char_position_right in range(len(s), char_position_left+1, -1):
                if char_position_right - char_position_left < len_max:
                    continue
                new_s = s[char_position_left:char_position_right]
                if new_s == new_s[::-1]:
                    if len(new_s) > len(max_palindrome):
                        max_palindrome = new_s
                        len_max = len(max_palindrome)
                continue
        return max_palindrome

    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = s[0] if len(s) > 0 else ''
        len_max = len(max_palindrome)
        reversed_s = s[::-1]
        length = len(s)
        for char_position_left in range(len(s) - 1):
            for char_position_right in range(len(s), char_position_left+1, -1):
                if char_position_right - char_position_left < len(max_palindrome):
                    continue
                if s[char_position_left:char_position_right] == reversed_s[length-char_position_right: length-char_position_left]:
                    if char_position_right - char_position_left > len_max:
                        max_palindrome = s[char_position_left:char_position_right]
                        len_max = len(max_palindrome)
                continue
        return max_palindrome