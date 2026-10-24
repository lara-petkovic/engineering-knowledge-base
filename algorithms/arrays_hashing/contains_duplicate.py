"""Contains Duplicate (Easy).

Problem: https://leetcode.com/problems/contains-duplicate/
Time: O(n)
Space: O(n)
"""

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
        ([], False),
        ([1], False),
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([2, 2], True),
        ([0, -1, -1], True),
        ([0, -1, 1], False),
        ([3, 3, 3], True),
    ]
    for nums, expected in cases:
        original = nums.copy()
        assert Solution().containsDuplicate(nums) is expected, f"Failed for {nums}"
        assert nums == original, "The input must not be modified"
    print(f"All {len(cases)} checks passed!")
