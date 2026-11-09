"""Zigzag Conversion (Medium).

Problem: https://leetcode.com/problems/zigzag-conversion/

Solution:
Time: O(N), where N is len(s)
Space: O(N)
"""


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
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("AB", 3, "AB"),
        ("", 3, ""),
    ]
    failed = 0
    for s, num_rows, expected in cases:
        try:
            result = Solution().convert(s, num_rows)
            assert isinstance(result, str), f"Expected a string, got {type(result).__name__}"
            assert result == expected, f"Expected {expected!r}, got {result!r}"
        except Exception as error:
            failed += 1
            print(f"FAIL: s={s!r}, numRows={num_rows} => {type(error).__name__}: {error}")
        else:
            print(f"PASS: s={s!r}, numRows={num_rows} => {result!r}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
