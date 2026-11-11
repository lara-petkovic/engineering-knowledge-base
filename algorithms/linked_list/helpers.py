"""Shared linked-list nodes and test helpers."""

from __future__ import annotations

from collections.abc import Iterable


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


def build_linked_list(values: Iterable[int]) -> ListNode | None:
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


def prepare_linked_lists(args: tuple[list[int], ...]) -> tuple[ListNode | None, ...]:
    return tuple(build_linked_list(values) for values in args)
