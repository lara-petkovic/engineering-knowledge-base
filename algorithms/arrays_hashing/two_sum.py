"""Two Sum (Easy).

Problem: https://leetcode.com/problems/two-sum/
Time: O(n)
Space: O(n)
"""


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
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4], 5),
    ]
    failed = 0
    for nums, target in cases:
        try:
            result = Solution().twoSum(nums, target)
            assert len(result) == 2, f"Expected two indices, got {result}"
            i, j = result
            assert 0 <= i < len(nums) and 0 <= j < len(nums), "Index out of range"
            assert i != j, "The same index was used twice"
            assert nums[i] + nums[j] == target, f"{nums[i]} + {nums[j]} != {target}"
        except Exception as error:
            failed += 1
            print(f"FAIL: nums={nums}, target={target} => {error}")
        else:
            print(f"PASS: nums={nums}, target={target} => {result}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
