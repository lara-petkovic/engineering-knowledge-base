"""Same Tree (Easy).

Problem: https://leetcode.com/problems/same-tree/
Check whether two binary trees have the same structure and node values.
Compare each pair of nodes, then recursively compare their left and right
subtrees. Stop as soon as a difference is found.

Time: O(n) in the worst case, where n is the total number of input nodes.
Space: O(h) for the recursion stack, where h is the maximum input tree height.
"""

from algorithms.test_helpers import run_tests
from algorithms.trees.helpers import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    cases = [
        ((None, None), True),
        ((TreeNode(1), None), False),
        ((None, TreeNode(1)), False),
        ((TreeNode(1), TreeNode(1)), True),
        ((TreeNode(1), TreeNode(2)), False),
        (
            (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))),
            True,
        ),
        ((TreeNode(1, TreeNode(2)), TreeNode(1, right=TreeNode(2))), False),
        (
            (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(4))),
            False,
        ),
        ((TreeNode(1, TreeNode(2)), TreeNode(1, TreeNode(2, TreeNode(3)))), False),
        (
            (TreeNode(1, TreeNode(2, TreeNode(3))), TreeNode(1, TreeNode(2, TreeNode(3)))),
            True,
        ),
        ((TreeNode(0, TreeNode(-1)), TreeNode(0, TreeNode(-1))), True),
        (
            (TreeNode(1, TreeNode(1)), TreeNode(1, right=TreeNode(1))),
            False,
        ),
    ]
    raise SystemExit(run_tests(Solution().isSameTree, cases))
