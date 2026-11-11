"""Binary Search (Easy).

Problem: https://leetcode.com/problems/binary-search/
Given a sorted integer list and a target, return its index or -1 if it is absent.

Solution:
Time: O(log n)
Space: O(1)

MoreElegantSolution:
Time: O(log n)
Space: O(1)
"""

from algorithms.test_helpers import run_tests


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        i = len(nums) // 2
        while (right - left) > 1:
            temp = nums[i]
            if temp > target:
                right = i
                i = right - (right - left) // 2
            elif temp < target:
                left = i
                i = left + (right - left) // 2
            else:
                return i
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1


class MoreElegantSolution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1


if __name__ == "__main__":
    cases = [
        (([5], 5), 0),
        (([1, 3], 1), 0),
        (([-1, 0, 3, 5, 9, 12], 2), -1),
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([5], 3), -1),
        (([1, 3], 3), 1),
        (([1, 3], 2), -1),
        (([-10, -5, 0, 5, 10], 0), 2),
        (([-10, -5, 0, 5, 10], -10), 0),
        (([-10, -5, 0, 5, 10], 10), 4),
        (([-10, -5, 0, 5, 10], -20), -1),
        (([-10, -5, 0, 5, 10], 20), -1),
    ]
    raise SystemExit(run_tests([Solution().search, MoreElegantSolution().search], cases))
