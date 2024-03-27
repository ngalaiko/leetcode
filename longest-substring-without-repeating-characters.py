class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max = 0
        while end != len(s):
            c = s[end]

            while c in s[start:end] and start < end:
                start += 1

            end += 1

            l = end - start
            if l > max:
                max = l

        return max


if __name__ == '__main__':
    # s = "dvdf" # 3
    s = "abcabcbb"  # 3
    s = "bbbbb"  # 1
    s = "pwwkew"  # 3
    print(Solution().lengthOfLongestSubstring(s))
