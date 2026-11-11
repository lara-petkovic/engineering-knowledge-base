"""Add Two Numbers (Medium).

Problem: https://leetcode.com/problems/add-two-numbers/

The digits of each non-negative number are stored in reverse order in a linked
list. Return their sum in the same format.

Solution:
Time: O(m^2 + n^2)
Space: O(m + n)

OptimalSolution:
Time: O(max(m, n))
Space: O(max(m, n))
"""

from __future__ import annotations

from algorithms.linked_list.helpers import ListNode, linked_list_to_list, prepare_linked_lists
from algorithms.test_helpers import run_tests


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        current1 = l1
        current2 = l2
        first_num_str = ""
        second_num_str = ""

        while current1:
            first_num_str += str(current1.val)
            current1 = current1.next

        while current2:
            second_num_str += str(current2.val)
            current2 = current2.next

        res_str = str(int(first_num_str[::-1]) + int(second_num_str[::-1]))[::-1]

        res = ListNode()
        current = res

        for num in res_str:
            current.next = ListNode(int(num))
            current = current.next

        return res.next


class OptimalSolution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


if __name__ == "__main__":
    cases = [
        (([2, 4, 3, 1], [5, 6, 4]), [7, 0, 8, 1]),
        (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
        (([0], [0]), [0]),
        (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
        (([1], [9, 9]), [0, 0, 1]),
    ]
    raise SystemExit(
        run_tests(
            [Solution().addTwoNumbers, OptimalSolution().addTwoNumbers],
            cases,
            prepare=prepare_linked_lists,
            convert=linked_list_to_list,
        )
    )
