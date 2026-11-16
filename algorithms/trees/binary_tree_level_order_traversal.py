"""Binary Tree Level Order Traversal (Medium).

Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

Time: O(n)
Space: O(w) - w is the maximum width of the tree
"""

from __future__ import annotations

from collections import deque

from algorithms.test_helpers import run_tests
from algorithms.trees.helpers import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        res = []
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            res.append(level)

        return res


if __name__ == "__main__":
    cases = [
        ((None,), []),
        ((TreeNode(1),), [[1]]),
        (
            (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),),
            [[3], [9, 20], [15, 7]],
        ),
        ((TreeNode(1, TreeNode(2, TreeNode(3))),), [[1], [2], [3]]),
        ((TreeNode(1, right=TreeNode(2, right=TreeNode(3))),), [[1], [2], [3]]),
        (
            (TreeNode(1, TreeNode(2, right=TreeNode(4)), TreeNode(3, TreeNode(5))),),
            [[1], [2, 3], [4, 5]],
        ),
        ((TreeNode(0, TreeNode(-1), TreeNode(-1)),), [[0], [-1, -1]]),
    ]
    raise SystemExit(run_tests(Solution().levelOrder, cases))
