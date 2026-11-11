"""Best Time to Buy and Sell Stock (Easy).

Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Given a list of stock prices, return the maximum profit from one buy followed
by one sell. The buy must happen before the sell. Return 0 if no profit is
possible.

Example:
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5
"""

from algorithms.test_helpers import run_tests


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = float("inf")
        best_profit = 0

        for price in prices:
            lowest_price = min(lowest_price, price)
            best_profit = max(best_profit, price - lowest_price)

        return best_profit


if __name__ == "__main__":
    cases = [
        (([7, 1, 5, 3, 6, 4],), 5),
        (([7, 6, 4, 3, 1],), 0),
        (([1, 2],), 1),
        (([2, 4, 1],), 2),
        (([3, 2, 6, 5, 0, 3],), 4),
        (([1],), 0),
        (([1, 2, 3, 4, 5],), 4),
        (([2, 2, 2],), 0),
    ]
    raise SystemExit(run_tests(Solution().maxProfit, cases))
