"""Group Anagrams (Medium).

Problem: https://leetcode.com/problems/group-anagrams/

Group the strings that are anagrams of each other and return the groups.

Solution:
Time: O(n * k log k)
Space: O(n * k)

OptimalSolution:
Time: O(n * k)
Space: O(n * k)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hm = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in hm:
                hm[key] = []
            hm[key].append(s)
        return list(hm.values())


class OptimalSolution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
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
        result2 = OptimalSolution().groupAnagrams(strs)

        assert sorted(map(sorted, result1)) == sorted(map(sorted, expected)), (
            f"Failed for original solution: {strs}: {result1}"
        )
        assert sorted(map(sorted, result2)) == sorted(map(sorted, expected)), (
            f"Failed for optimized solution: {strs}: {result2}"
        )

    print(f"All {len(cases)} checks passed!")
    print("Solution: O(n * k log k)")
    print("OptimalSolution: O(n * k) with a 26-letter count key")
