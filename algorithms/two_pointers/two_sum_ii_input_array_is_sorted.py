"""Two Sum II - Input Array Is Sorted (Medium).

Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Time: O(n)
Space: O(1)
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1

        while left <= right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif target - numbers[left] > numbers[right]:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2], 3, [1, 2]),
        ([3, 3], 6, [1, 2]),
        ([0, 0, 3, 4], 0, [1, 2]),
        ([-8, -5, -3, -1], -8, [2, 3]),
        ([-10, -3, 0, 4, 9], -1, [1, 5]),
        ([1, 2, 4, 8, 16], 24, [4, 5]),
        ([1, 2, 4, 8, 16], 6, [2, 3]),
        ([1, 2, 2, 4, 7], 4, [2, 3]),
        ([-1000, -500, 0, 500, 1000], -1000, [1, 3]),
    ]
    failed = 0
    for numbers, target, expected in cases:
        try:
            result = Solution().twoSum(numbers, target)
            assert isinstance(result, list), f"Expected a list, got {type(result).__name__}"
            assert result == expected, f"Expected 1-based indices {expected}, got {result}"
        except Exception as error:
            failed += 1
            print(f"FAIL: numbers={numbers}, target={target} => {type(error).__name__}: {error}")
        else:
            print(f"PASS: numbers={numbers}, target={target} => {result}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
