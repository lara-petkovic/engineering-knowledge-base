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


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


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


def build_linked_list(values: list[int]) -> ListNode | None:
    head = ListNode()
    current = head

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return head.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values


if __name__ == "__main__":
    cases = [
        ([2, 4, 3, 1], [5, 6, 4], [7, 0, 8, 1]),
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([1], [9, 9], [0, 0, 1]),
    ]
    failed = 0
    for first, second, expected in cases:
        for solution_type in (Solution, OptimalSolution):
            try:
                result = solution_type().addTwoNumbers(
                    build_linked_list(first),
                    build_linked_list(second),
                )
                actual = linked_list_to_list(result)
                assert actual == expected, f"Expected {expected}, got {actual}"
            except Exception as error:
                failed += 1
                print(
                    f"FAIL: {solution_type.__name__}: {first} + {second} "
                    f"=> {type(error).__name__}: {error}"
                )
            else:
                print(f"PASS: {solution_type.__name__}: {first} + {second} => {actual}")
    print(f"Passed: {len(cases) - failed}, failed: {failed}")
    raise SystemExit(1 if failed else 0)
