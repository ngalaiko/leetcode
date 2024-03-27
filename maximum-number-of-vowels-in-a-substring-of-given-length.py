class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def is_vowel(c: str) -> bool:
            return c in vowels

        def count_vowels(s: str) -> int:
            return sum(list(map(lambda x: 1 if is_vowel(x) else 0, s)))

        count = count_vowels(s[:k])
        m = count
        for i in range(1, len(s) - k+1):
            if is_vowel(s[i-1]):
                count -= 1
                count = max(0, count)

            if is_vowel(s[i+k - 1]):
                count += 1

            m = max(m, count)

        return m


if __name__ == '__main__':
    assert Solution().maxVowels("abciiidef", 3) == 3
    assert Solution().maxVowels("aeiou", 2) == 2
    assert Solution().maxVowels("leetcode", 3) == 2
