"""Checks for shared runner behavior and problem-specific validation."""

import io
import unittest
from contextlib import redirect_stdout

from algorithms.linked_list.helpers import ListNode, linked_list_to_list
from algorithms.test_helpers import check_two_sum, normalize_groups, run_tests


class RunnerTests(unittest.TestCase):
    def run_quietly(self, *args, **kwargs):
        output = io.StringIO()
        with redirect_stdout(output):
            status = run_tests(*args, **kwargs)
        return status, output.getvalue()

    def test_failure_does_not_skip_remaining_cases(self):
        def solve(value):
            if value == 0:
                raise ValueError("test error")
            return value

        status, output = self.run_quietly(solve, [((0,), 0), ((1,), 1)])
        self.assertEqual(status, 1)
        self.assertIn("Passed: 1, failed: 1", output)
        self.assertIn("ValueError: test error", output)

    def test_inputs_are_fresh_for_each_solution(self):
        def solve(values):
            return values.pop()

        cases = [(([1, 2],), 2)]
        status, output = self.run_quietly([solve, solve], cases)
        self.assertEqual(status, 0)
        self.assertEqual(cases[0][0][0], [1, 2])
        self.assertIn("Passed: 2, failed: 0", output)

    def test_input_mutation_can_be_rejected(self):
        def solve(values):
            values.append(3)
            return True

        status, _ = self.run_quietly(solve, [(([1],), True)], unchanged=True)
        self.assertEqual(status, 1)

    def test_bool_is_not_accepted_as_int(self):
        status, _ = self.run_quietly(lambda: True, [((), 1)])
        self.assertEqual(status, 1)

    def test_normalization_preserves_duplicate_counts(self):
        self.assertEqual(normalize_groups([[2, 1], [3]]), [[1, 2], [3]])
        status, _ = self.run_quietly(lambda: [[1], [1]], [((), [[1]])], normalize=normalize_groups)
        self.assertEqual(status, 1)

    def test_two_sum_accepts_alternative_indices(self):
        check_two_sum(([1, 2, 3, 4], 5), [1, 2], None)
        with self.assertRaises(AssertionError):
            check_two_sum(([2, 3], 4), [0, 0], None)

    def test_linked_list_cycle_is_a_failed_case(self):
        node = ListNode(1)
        node.next = node
        status, output = self.run_quietly(lambda: node, [((), [1])], convert=linked_list_to_list)
        self.assertEqual(status, 1)
        self.assertIn("cycle", output)


if __name__ == "__main__":
    unittest.main()
