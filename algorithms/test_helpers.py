"""Shared runner and result checks for algorithm exercises."""

from collections.abc import Callable, Iterable
from copy import deepcopy
from typing import Any


def normalize_groups(groups: list[list[Any]]) -> list[list[Any]]:
    """Ignore group and element order, while preserving duplicates."""
    assert isinstance(groups, list), "Expected a list"
    assert all(isinstance(group, list) for group in groups), "Expected lists of elements"
    return sorted(sorted(group) for group in groups)


def check_two_sum(args: tuple, result: Any, expected: Any) -> None:
    """Accept any two distinct zero-based indices whose values reach the target."""
    nums, target = args
    assert isinstance(result, list) and len(result) == 2, "Expected two indices"
    i, j = result
    assert type(i) is int and type(j) is int, "Expected integer indices"
    assert 0 <= i < len(nums) and 0 <= j < len(nums), "Index out of range"
    assert i != j, "The same index was used twice"
    assert nums[i] + nums[j] == target, f"{nums[i]} + {nums[j]} != {target}"


def run_tests(
    solutions: Callable | Iterable[Callable],
    cases: Iterable[tuple[tuple, Any]],
    *,
    normalize: Callable | None = None,
    check: Callable | None = None,
    prepare: Callable | None = None,
    convert: Callable | None = None,
    unchanged: bool = False,
) -> int:
    """Run (arguments, expected) cases; print results and return an exit code.

    Each call receives fresh copies of its arguments. Optional hooks prepare
    inputs, convert outputs, normalize order, or check problem-specific rules.
    A custom check must raise AssertionError on failure.
    """
    if callable(solutions):
        solutions = [solutions]
    cases = list(cases)
    total = 0
    failed = 0
    for solve in solutions:
        for args, expected in cases:
            total += 1
            try:
                call_args = deepcopy(args)
                if prepare is not None:
                    call_args = prepare(call_args)
                result = solve(*call_args)
                if unchanged:
                    assert call_args == args, "The input must not be modified"
                if convert is not None:
                    result = convert(result)
                if check is not None:
                    check(args, result, expected)
                else:
                    assert type(result) is type(expected), (
                        f"Expected {type(expected).__name__}, got {type(result).__name__}"
                    )
                    actual = normalize(result) if normalize is not None else result
                    wanted = normalize(expected) if normalize is not None else expected
                    assert actual == wanted, f"Expected {expected!r}, got {result!r}"
            except Exception as error:
                failed += 1
                print(f"FAIL: {solve.__qualname__}: {args!r} => {type(error).__name__}: {error}")
            else:
                print(f"PASS: {solve.__qualname__}: {args!r} => {result!r}")
    print(f"Passed: {total - failed}, failed: {failed}")
    return 1 if failed else 0
