"""Zigzag Conversion (Medium).

Problem: https://leetcode.com/problems/zigzag-conversion/

Solution:
Time: O(N), where N is len(s)
Space: O(N)
"""

from algorithms.test_helpers import run_tests


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        row = 0
        direction = 1

        for char in s:
            rows[row] += char

            if row == numRows - 1:
                direction = -1
            elif row == 0:
                direction = 1

            row += direction

        return "".join(rows)


if __name__ == "__main__":
    cases = [
        (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
        (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        (("A", 1), "A"),
        (("AB", 3), "AB"),
        (("", 3), ""),
    ]
    raise SystemExit(run_tests(Solution().convert, cases))
