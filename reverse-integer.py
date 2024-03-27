class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)

        digits = []

        while x != 0:
            digits.append(x % 10)
            x = x//10

        r = 0
        for i in range(0, len(digits)):
            pow = len(digits) - i - 1
            r += digits[i] * (10 ** pow)

        if r >= 2**31:
            return 0

        if is_negative:
            return r * -1

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-321))
