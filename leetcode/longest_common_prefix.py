from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        result = ''
        if len(strs) == 0:
            return result
        while True:
            if len(strs[0]) == index:
                return result
            for str_ in strs[1:]:
                if len(str_) == index:
                    return result
                if str_[index] != strs[0][index]:
                    return result
            result += strs[0][index]
            index += 1
