"""3. Longest Substring Without Repeating Characters (Medium).

Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time: O(N), where N is len(s), assuming average O(1) set operations.
Space: O(min(N, K)), where K is the size of the input character set.
"""

from algorithms.test_helpers import run_tests


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 0
        window_chars = set()
        res = 0

        for i in range(len(s)):
            if s[i] not in window_chars:
                window_chars.add(s[i])
                right += 1
            else:
                while s[i] in window_chars:
                    window_chars.remove(s[left])
                    left += 1

                window_chars.add(s[i])
                right += 1
            res = max(res, right - left)
        return res


if __name__ == "__main__":
    cases = [
        (("abcabcbb",), 3),
        (("bbbbb",), 1),
        (("pwwkew",), 3),
        (("",), 0),
        (("a",), 1),
        (("abcdef",), 6),
        (("abba",), 2),
        (("dvdf",), 3),
        (("tmmzuxt",), 5),
        ((" ",), 1),
        (("a b!a",), 4),
        (("aAbB",), 4),
    ]
    raise SystemExit(run_tests(Solution().lengthOfLongestSubstring, cases))
