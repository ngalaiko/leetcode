class Solution:
    def intToRoman(self, num: int) -> str:
        m = num // 1000
        if m > 0:
            return 'M' * m + self.intToRoman(num % 1000)

        if num >= 900:
            return 'CM' + self.intToRoman(num - 900)

        d = num // 500
        if d > 0:
            return 'D' * d + self.intToRoman(num % 500)

        if num >= 400:
            return 'CD' + self.intToRoman(num - 400)

        c = num // 100
        if c > 0:
            return 'C' * c + self.intToRoman(num % 100)

        if num >= 90:
            return 'XC' + self.intToRoman(num - 90)

        l = num // 50
        if l > 0:
            return 'L' * l + self.intToRoman(num % 50)

        if num >= 40:
            return 'XL' + self.intToRoman(num - 40)

        x = num // 10
        if x > 0:
            return 'X' * x + self.intToRoman(num % 10)

        if num == 9:
            return 'IX'

        v = num // 5
        if v > 0:
            return 'V' * v + self.intToRoman(num % 5)

        if num == 4:
            return 'IV'

        return 'I' * num


if __name__ == '__main__':
    assert Solution().intToRoman(19) == "XIX"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"
