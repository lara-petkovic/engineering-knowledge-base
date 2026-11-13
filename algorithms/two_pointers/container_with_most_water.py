"""Container With Most Water (Medium).

Problem: https://leetcode.com/problems/container-with-most-water/

Time: O(n)
Space: O(1)
"""

from algorithms.test_helpers import run_tests


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


if __name__ == "__main__":
    cases = [
        (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
        (([1, 1],), 1),
        (([1, 2],), 1),
        (([0, 0],), 0),
        (([0, 5],), 0),
        (([5, 5, 5, 5],), 15),
        (([1, 2, 3, 4, 5],), 6),
        (([5, 4, 3, 2, 1],), 6),
        (([1, 10, 1, 1, 10, 1],), 30),
        (([10, 1, 1, 1, 10],), 40),
        (([10000, 10000],), 10000),
    ]
    raise SystemExit(run_tests(Solution().maxArea, cases, unchanged=True))
