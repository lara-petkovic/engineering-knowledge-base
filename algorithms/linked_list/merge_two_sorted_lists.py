"""Merge Two Sorted Lists (Easy).

Problem: https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists into one sorted linked list and return its head.

Time: O(m + n)
Space: O(1)
"""

from __future__ import annotations

from algorithms.linked_list.helpers import ListNode, linked_list_to_list, prepare_linked_lists
from algorithms.test_helpers import run_tests


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        res = ListNode()
        temp = res

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        temp.next = list1 if list1 else list2
        return res.next


if __name__ == "__main__":
    cases = [
        (([], []), []),
        (([], [0]), [0]),
        (([0], []), [0]),
        (([], [1, 2, 3]), [1, 2, 3]),
        (([1, 2, 3], []), [1, 2, 3]),
        (([1], [2]), [1, 2]),
        (([2], [1]), [1, 2]),
        (([1], [1]), [1, 1]),
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([1, 2], [3, 4, 5]), [1, 2, 3, 4, 5]),
        (([3, 4, 5], [1, 2]), [1, 2, 3, 4, 5]),
        (([1], [2, 3, 4, 5]), [1, 2, 3, 4, 5]),
        (([0, 0], [0, 0, 0]), [0, 0, 0, 0, 0]),
        (([-5, -3, -1], [-4, -2, 0]), [-5, -4, -3, -2, -1, 0]),
        (([-10, 0, 10], [-5, 0, 5]), [-10, -5, 0, 0, 5, 10]),
    ]
    raise SystemExit(
        run_tests(
            Solution().mergeTwoLists,
            cases,
            prepare=prepare_linked_lists,
            convert=linked_list_to_list,
        )
    )
