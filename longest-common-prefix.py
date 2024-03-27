from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pos = 0
        while pos < len(strs[0]):
            for i in range(1, len(strs)):
                if pos >= len(strs[i]) or strs[0][pos] != strs[i][pos]:
                    return strs[0][:pos]

            pos += 1

        return strs[0][:pos]


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix(["ab", "a"]) == "a"
    assert Solution().longestCommonPrefix([""]) == ""
