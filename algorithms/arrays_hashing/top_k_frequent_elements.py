"""Top K Frequent Elements (Medium).

Problem: https://leetcode.com/problems/top-k-frequent-elements/
Solution:
Time: O(n log n)
Space: O(n)

BetterSolution:
Time: O(n)
Space: O(n)
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1
        sorted_hm = dict(sorted(hm.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_hm.keys())[:k]


class BetterSolution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency_by_number = {}

        for number in nums:
            if number not in frequency_by_number:
                frequency_by_number[number] = 0

            frequency_by_number[number] += 1

        numbers_by_frequency = []
        for _ in range(len(nums) + 1):
            numbers_by_frequency.append([])

        for number, frequency in frequency_by_number.items():
            numbers_by_frequency[frequency].append(number)

        most_frequent_numbers = []

        for frequency in range(len(nums), 0, -1):
            numbers = numbers_by_frequency[frequency]

            for number in numbers:
                most_frequent_numbers.append(number)

                if len(most_frequent_numbers) == k:
                    return most_frequent_numbers

        return []


if __name__ == "__main__":
    cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 4, 4, 4], 1, [4]),
        ([1, 2, 2, 3, 3, 3], 1, [3]),
        ([-1, -1, -1, 0, 0, 2], 2, [-1, 0]),
        ([5, 5, 5, 5, 2, 2, 2, 9, 9, 1], 3, [5, 2, 9]),
        ([3, 1, 2], 3, [1, 2, 3]),
        ([10, 10, 20, 20, 30], 2, [10, 20]),
    ]
    failed = 0
    for nums, k, expected in cases:
        try:
            result = Solution().topKFrequent(nums, k)
            assert isinstance(result, list), f"Expected a list, got {type(result).__name__}"
            assert len(result) == k, f"Expected {k} elements, got {result}"
            assert sorted(result) == sorted(expected), f"Expected {expected}, got {result}"
        except Exception as error:
            failed += 1
            print(f"FAIL: nums={nums}, k={k} => {error}")
        else:
            print(f"PASS: nums={nums}, k={k} => {result}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
