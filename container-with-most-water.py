from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(left, right):
            h = min(height[left], height[right])
            w = right - left
            return h*w

        l = 0
        r = len(height) - 1
        m = 0
        while l != r:
            m = max(m, area(l, r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return m


if __name__ == '__main__':
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
    assert Solution().maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
