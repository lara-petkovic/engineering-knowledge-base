"""Valid Palindrome (Easy).

Problem: https://leetcode.com/problems/valid-palindrome/
Time: O(n)
Space: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



if __name__ == "__main__":
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        (" ", True),
        ("   ", True),
        ("!!!", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("abcba", True),
        ("abc", False),
        ("0P", False),
        ("ab_a", True),
        ("ab@a", True),
        ("Aba", True),
        ("12321", True),
        ("12345", False),
        ("a1b1a", True),
        (".,a@A!,", True),
        ("a.b,c!b a", True),
        ("a!b", False),
    ]

    failed = 0

    for s, expected in cases:
        try:
            result = Solution().isPalindrome(s)
            assert isinstance(result, bool), (f"Expected bool, got {type(result).__name__}")
            assert result == expected, (f"Expected {expected}, got {result}")

        except Exception as error:
            failed += 1
            print(f"FAIL: s={s!r} => {error}")
        else:
            print(f"PASS: s={s!r} => {result}")

    print(f"\nPassed: {len(cases) - failed}, failed: {failed}")
