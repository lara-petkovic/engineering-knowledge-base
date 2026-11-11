"""3. Longest Substring Without Repeating Characters (Medium).

Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time: O(N), where N is len(s), assuming average O(1) set operations.
Space: O(min(N, K)), where K is the size of the input character set.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0
        r = 0
        st = set()
        res = 0

        for i in range(len(s)):
            if s[i] not in st:
                st.add(s[i])
                r += 1
            else:
                while s[i] in st:
                    st.remove(s[l])
                    l += 1

                st.add(s[i])
                r += 1
            res = max(res, r - l)
        return res


if __name__ == "__main__":
    cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("abba", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        (" ", 1),
        ("a b!a", 4),
        ("aAbB", 4),
    ]
    failed = 0
    for s, expected in cases:
        try:
            result = Solution().lengthOfLongestSubstring(s)
            assert type(result) is int, f"Expected an int, got {type(result).__name__}"
            assert result == expected, f"Expected {expected}, got {result}"
        except Exception as error:
            failed += 1
            print(f"FAIL: s={s!r} => {type(error).__name__}: {error}")
        else:
            print(f"PASS: s={s!r} => {result}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
