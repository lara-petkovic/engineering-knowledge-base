"""String to Integer (atoi) (Medium).

Problem: https://leetcode.com/problems/string-to-integer-atoi/
"""

from algorithms.test_helpers import run_tests


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        sign = 1
        if s.startswith("-"):
            sign = -1
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        num = 0

        for char in s:
            if "0" <= char <= "9":
                digit = ord(char) - ord("0")
                num = num * 10 + digit
            else:
                break

        num *= sign

        return max(-(2**31), min(num, 2**31 - 1))


if __name__ == "__main__":
    cases = [
        (("42",), 42),
        (("   -042",), -42),
        (("1337c0d3",), 1337),
        (("0-1",), 0),
        (("words and 987",), 0),
        (("+1",), 1),
        (("",), 0),
        (("   ",), 0),
        (("+-12",), 0),
        (("2147483648",), 2147483647),
        (("-91283472332",), -2147483648),
    ]
    raise SystemExit(run_tests(Solution().myAtoi, cases))
