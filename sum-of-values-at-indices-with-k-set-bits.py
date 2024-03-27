from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def bits_set(n):
            bits = 0
            if n >= 512:
                n -= 512
                bits += 1

            if n >= 256:
                n -= 256
                bits += 1

            if n >= 128:
                n -= 128
                bits += 1

            if n >= 64:
                n -= 64
                bits += 1

            if n >= 32:
                n -= 32
                bits += 1

            if n >= 16:
                n -= 16
                bits += 1

            if n >= 8:
                n -= 8
                bits += 1

            if n >= 4:
                n -= 4
                bits += 1

            if n >= 2:
                n -= 2
                bits += 1

            if n >= 1:
                n -= 1
                bits += 1

            return bits

        s = 0
        for i in range(len(nums)):
            if bits_set(i) == k:
                s += nums[i]

        return s


if __name__ == '__main__':
    assert Solution().sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1) == 13
    assert Solution().sumIndicesWithKSetBits([4, 3, 2, 1], 2) == 1
