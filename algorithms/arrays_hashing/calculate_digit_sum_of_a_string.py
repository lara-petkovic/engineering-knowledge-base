"""Calculate Digit Sum of a String (Easy).

Problem: https://leetcode.com/problems/calculate-digit-sum-of-a-string/

Time: O(r * n^2) - r is the number of rounds
Space: O(n)
"""

from algorithms.test_helpers import run_tests


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""

            while s:
                part = s[:k]
                new_s += str(sum(int(x) for x in part))
                s = s[k:]

            s = new_s
        return s


if __name__ == "__main__":
    cases = [
        (("11111222223", 3), "135"),
        (("00000000", 3), "000"),
        (("5", 2), "5"),
        (("123", 3), "123"),
        (("001", 3), "001"),
        (("1234", 3), "64"),
        (("12345", 2), "15"),
        (("99999", 2), "99"),
        (("9999", 2), "99"),
        (("0" * 100, 2), "00"),
    ]
    raise SystemExit(run_tests(Solution().digitSum, cases))
