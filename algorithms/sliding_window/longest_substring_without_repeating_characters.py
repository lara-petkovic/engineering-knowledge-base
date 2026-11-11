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
        r = 0
        st = set()
        res = 0

        for i in range(len(s)):
            if s[i] not in st:
                st.add(s[i])
                r += 1
            else:
                while s[i] in st:
                    st.remove(s[left])
                    left += 1

                st.add(s[i])
                r += 1
            res = max(res, r - left)
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
