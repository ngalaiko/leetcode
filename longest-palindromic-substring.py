class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(0, len(s)):
            for j in range(i, len(s) + 1):
                sub = s[i:j]
                if is_palindrome(sub) and len(sub) > len(longest):
                    longest = sub

        return longest


cache = {}


def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s)-1]:
        return False
    else:
        middle = s[1:len(s)-1]
        if middle in cache:
            return cache[middle]
        result = is_palindrome(middle)
        cache[middle] = result
        return result


if __name__ == '__main__':
    s = "a"
    print(Solution().longestPalindrome(s))
