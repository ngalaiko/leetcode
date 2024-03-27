from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = abs(x)

        if x < 10:
            return True

        digits = []
        while x != 0:
            digits.append(x % 10)
            x = x // 10

        def is_palindrome(digits: List[int]) -> bool:
            if len(digits) <= 1:
                return True

            if digits[0] != digits[len(digits) - 1]:
                return False

            return is_palindrome(digits[1:len(digits) - 1])

        return is_palindrome(digits)


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(0))
