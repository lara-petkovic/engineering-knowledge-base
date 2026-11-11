"""Map Word Weights (Easy).

Problem: https://leetcode.com/problems/map-word-weights/

Solution:
Time: O(C + W^2), where C is the total number of letters and W is len(words)
Space: O(26 + W), including the result
"""

import string

from algorithms.test_helpers import run_tests


class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        reverse_letters = string.ascii_lowercase[::-1]
        result = []

        for word in words:
            sum = 0
            for letter in word:
                sum += weights[ord(letter) - ord("a")]

            result.append(reverse_letters[sum % 26])
        return "".join(result)


if __name__ == "__main__":
    alphabet_weights = list(range(26))
    cases = [
        ((["a", "az", "bc", "zzz"], alphabet_weights), "zawc"),
        ((["a", "ab", "xyz"], [1] * 26), "yxw"),
        ((["a", "leetcode"], [0] * 26), "zz"),
        (([], alphabet_weights), ""),
    ]
    raise SystemExit(run_tests(Solution().mapWordWeights, cases))
