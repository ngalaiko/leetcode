class Solution:
    translation = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return self.translation[s]
        elif s[:2] in self.translation:
            return self.translation[s[:2]] + self.romanToInt(s[2:])
        else:
            return self.translation[s[:1]] + self.romanToInt(s[1:])


if __name__ == '__main__':
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
