"""Group Anagrams (Medium).

Problem: https://leetcode.com/problems/group-anagrams/

This file contains:
1) the user's original solution using sorted strings
2) a better approach using a fixed-size letter-count array
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Original approach: sort each string and group by its sorted key."""
        hm = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in hm:
                hm[key] = []
            hm[key].append(s)
        return list(hm.values())


class SolutionBetter:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Better approach: count letters in a fixed 26-element array.

        Each word gets a key like (2, 1, 0, ..., 0), which represents the number
        of each letter in the word. This avoids sorting every string.
        """
        groups = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord("a")] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())


if __name__ == "__main__":
    cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["ab", "ba", "abc", "cba"], [["ab", "ba"], ["abc", "cba"]]),
        (["listen", "silent", "enlist", "hello"], [["listen", "silent", "enlist"], ["hello"]]),
    ]

    for strs, expected in cases:
        result1 = Solution().groupAnagrams(strs)
        result2 = SolutionBetter().groupAnagrams(strs)

        assert sorted(map(sorted, result1)) == sorted(map(sorted, expected)), (
            f"Failed for original solution: {strs}: {result1}"
        )
        assert sorted(map(sorted, result2)) == sorted(map(sorted, expected)), (
            f"Failed for optimized solution: {strs}: {result2}"
        )

    print(f"All {len(cases)} checks passed!")
    print("Original solution: O(n * k log k)")
    print("Better solution: O(n * k) with a 26-letter count key")
