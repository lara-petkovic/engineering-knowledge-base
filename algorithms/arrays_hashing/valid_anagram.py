"""Valid Anagram (Easy).

Problem: https://leetcode.com/problems/valid-anagram/
Time: O(n+m)
Space: O(k_s + k_t)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1, dict2 = {}, {}

        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            dict2[t[i]] = dict2.get(t[i], 0) + 1
        return dict1 == dict2


if __name__ == "__main__":
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
        ("abc", "cba", True),
        ("abc", "abcd", False),
    ]
    for s, t, expected in cases:
        assert Solution().isAnagram(s, t) is expected, f"Failed for {s}, {t}"
    print(f"All {len(cases)} checks passed!")
