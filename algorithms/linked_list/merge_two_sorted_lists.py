"""Merge Two Sorted Lists (Easy).

Problem: https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists into one sorted linked list and return its head.

Time: O(m + n)
Space: O(1)
"""

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


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


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    values = []
    seen = set()
    while head is not None:
        if id(head) in seen:
            raise AssertionError("Result contains a cycle")
        seen.add(id(head))
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    cases = [
        ([], [], []),
        ([], [0], [0]),
        ([0], [], [0]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([1], [2], [1, 2]),
        ([2], [1], [1, 2]),
        ([1], [1], [1, 1]),
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([1, 2], [3, 4, 5], [1, 2, 3, 4, 5]),
        ([3, 4, 5], [1, 2], [1, 2, 3, 4, 5]),
        ([1], [2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([0, 0], [0, 0, 0], [0, 0, 0, 0, 0]),
        ([-5, -3, -1], [-4, -2, 0], [-5, -4, -3, -2, -1, 0]),
        ([-10, 0, 10], [-5, 0, 5], [-10, -5, 0, 0, 5, 10]),
    ]
    failed = 0
    for first, second, expected in cases:
        try:
            result = Solution().mergeTwoLists(build_linked_list(first), build_linked_list(second))
            actual = linked_list_to_list(result)
            assert actual == expected, f"Expected {expected}, got {actual}"
        except Exception as error:
            failed += 1
            print(f"FAIL: {first} + {second} => {type(error).__name__}: {error}")
        else:
            print(f"PASS: {first} + {second} => {actual}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
