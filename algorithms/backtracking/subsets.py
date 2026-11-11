"""Subsets (Medium).

Problem: https://leetcode.com/problems/subsets/
Given a list of unique integers, return all possible subsets.

Time: O(n * 2**n)
Space: O(n) auxiliary, O(n * 2**n) including output
"""

from algorithms.test_helpers import normalize_groups, run_tests


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            # Don't choose nums[i]
            backtrack(i + 1)

            # Choose nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return res


if __name__ == "__main__":
    cases = [
        (([1, 2, 3],), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        (([0],), [[], [0]]),
        (([-1],), [[], [-1]]),
        (([1, 2],), [[], [1], [2], [1, 2]]),
        (([-1, 0, 1],), [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]),
        (([3, 1, 2],), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        (([-10, 10],), [[], [-10], [10], [-10, 10]]),
        (([0, 2],), [[], [0], [2], [0, 2]]),
    ]
    raise SystemExit(run_tests(Solution().subsets, cases, normalize=normalize_groups))
