"""Contains Duplicate (Easy).

Problem: https://leetcode.com/problems/contains-duplicate/
Given an integer list, return True if any value appears more than once.

Time: O(n)
Space: O(n)
"""

from algorithms.test_helpers import run_tests


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False


if __name__ == "__main__":
    cases = [
        (([],), False),
        (([1],), False),
        (([1, 2, 3, 4],), False),
        (([1, 2, 3, 1],), True),
        (([2, 2],), True),
        (([0, -1, -1],), True),
        (([0, -1, 1],), False),
        (([3, 3, 3],), True),
    ]
    raise SystemExit(run_tests(Solution().containsDuplicate, cases, unchanged=True))
