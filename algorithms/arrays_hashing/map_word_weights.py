"""Map Word Weights (Easy).

Problem: https://leetcode.com/problems/map-word-weights/

Solution:
Time: O(C + W^2), where C is the total number of letters and W is len(words)
Space: O(26 + W), including the result
"""

import string


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
        (["a", "az", "bc", "zzz"], alphabet_weights, "zawc"),
        (["a", "ab", "xyz"], [1] * 26, "yxw"),
        (["a", "leetcode"], [0] * 26, "zz"),
        ([], alphabet_weights, ""),
    ]
    failed = 0
    for words, weights, expected in cases:
        try:
            result = Solution().mapWordWeights(words, weights)
            assert isinstance(result, str), f"Expected a string, got {type(result).__name__}"
            assert result == expected, f"Expected {expected!r}, got {result!r}"
        except Exception as error:
            failed += 1
            print(f"FAIL: words={words} => {type(error).__name__}: {error}")
        else:
            print(f"PASS: words={words} => {result!r}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
