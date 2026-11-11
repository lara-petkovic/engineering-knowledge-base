"""Two Sum (Easy).

Problem: https://leetcode.com/problems/two-sum/
Given an integer list and a target, return the indices of two different values
that add up to the target.

Time: O(n)
Space: O(n)
"""

from algorithms.test_helpers import check_two_sum, run_tests


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}
        for i in range(len(nums)):
            if target - nums[i] in hm:
                return [hm[target - nums[i]], i]
            hm[nums[i]] = i
        return []


if __name__ == "__main__":
    cases = [
        (([2, 7, 11, 15], 9), None),
        (([3, 2, 4], 6), None),
        (([3, 3], 6), None),
        (([1, 2, 3, 4], 5), None),
    ]
    raise SystemExit(run_tests(Solution().twoSum, cases, check=check_two_sum))
