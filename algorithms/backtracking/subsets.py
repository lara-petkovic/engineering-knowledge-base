"""Subsets (Medium).

Problem: https://leetcode.com/problems/subsets/
Given a list of unique integers, return all possible subsets.

Time: O(n * 2**n)
Space: O(n) auxiliary, O(n * 2**n) including output
"""


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
        ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        ([-1], [[], [-1]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ([-1, 0, 1], [[], [-1], [0], [1], [-1, 0], [-1, 1], [0, 1], [-1, 0, 1]]),
        ([3, 1, 2], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ([-10, 10], [[], [-10], [10], [-10, 10]]),
        ([0, 2], [[], [0], [2], [0, 2]]),
    ]
    failed = 0
    for nums, expected in cases:
        try:
            result = Solution().subsets(nums.copy())
            assert isinstance(result, list), f"Expected a list, got {type(result).__name__}"
            assert all(isinstance(subset, list) for subset in result), "Expected lists of elements"
            # Ignore subset order and element order, while preserving duplicates for comparison.
            normalized_result = sorted(tuple(sorted(subset)) for subset in result)
            normalized_expected = sorted(tuple(sorted(subset)) for subset in expected)
            assert normalized_result == normalized_expected, f"Expected {expected}, got {result}"
        except Exception as error:
            failed += 1
            print(f"FAIL: nums={nums} => {type(error).__name__}: {error}")
        else:
            print(f"PASS: nums={nums} => {result}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
