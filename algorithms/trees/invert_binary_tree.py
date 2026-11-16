"""Invert Binary Tree (Easy).

Problem: https://leetcode.com/problems/invert-binary-tree/

Time: O(n)
Space: O(h) - h is the height of the tree
"""

from algorithms.test_helpers import run_tests
from algorithms.trees.helpers import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":

    def solve_and_check_root(root):
        result = Solution().invertTree(root)
        assert result is root, "Expected the original root to be returned"
        return result

    def check_tree(args, result, expected):
        pending = [(result, expected)]
        while pending:
            node, wanted = pending.pop()
            if wanted is None:
                assert node is None, "Expected an empty subtree"
            else:
                assert isinstance(node, TreeNode), "Expected a TreeNode"
                value, left, right = wanted
                assert node.val == value, f"Expected {value}, got {node.val}"
                pending.append((node.left, left))
                pending.append((node.right, right))

    cases = [
        ((None,), None),
        ((TreeNode(1),), (1, None, None)),
        ((TreeNode(1, TreeNode(2), TreeNode(3)),), (1, (3, None, None), (2, None, None))),
        ((TreeNode(1, TreeNode(2)),), (1, None, (2, None, None))),
        ((TreeNode(1, right=TreeNode(2)),), (1, (2, None, None), None)),
        (
            (TreeNode(1, TreeNode(2, right=TreeNode(3))),),
            (1, None, (2, (3, None, None), None)),
        ),
        (
            (
                TreeNode(
                    4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)),
                ),
            ),
            (
                4,
                (7, (9, None, None), (6, None, None)),
                (2, (3, None, None), (1, None, None)),
            ),
        ),
        ((TreeNode(0, TreeNode(-1), TreeNode(-1)),), (0, (-1, None, None), (-1, None, None))),
    ]
    raise SystemExit(run_tests(solve_and_check_root, cases, check=check_tree))
