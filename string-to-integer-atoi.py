class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1

        if i == len(s):
            return 0

        is_negative = False
        if s[i] == '-':
            is_negative = True
            i += 1
        elif s[i] == '+':
            i += 1

        def is_digit(c: str):
            return c >= '0' and c <= '9'

        digits = []
        while i < len(s) and is_digit(s[i]):
            digits.append(ord(s[i]) - ord('0'))
            i += 1

        i = 0
        r = 0
        for i in range(len(digits)):
            pow = len(digits) - 1 - i
            r += digits[i] * 10 ** pow

        if is_negative:
            if r > 2 ** 31:
                r = 2**31
            return r * -1

        if r > 2 ** 31 - 1:
            r = 2**31 - 1

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("  -42"))
    print(s.myAtoi("  42-"))
    print(s.myAtoi("42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))
    print(s.myAtoi(""))
    print(s.myAtoi("1"))
    print(s.myAtoi("21474836460"))
    print(s.myAtoi("+"))
    print(s.myAtoi(" "))
