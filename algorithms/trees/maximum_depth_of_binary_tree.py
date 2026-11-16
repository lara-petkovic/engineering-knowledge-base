"""Maximum Depth of Binary Tree (Easy).

Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Time: O(n)
Space: O(h)
"""

from algorithms.test_helpers import run_tests
from algorithms.trees.helpers import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


if __name__ == "__main__":
    cases = [
        ((None,), 0),
        ((TreeNode(1),), 1),
        ((TreeNode(1, TreeNode(2), TreeNode(3)),), 2),
        (
            (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),),
            3,
        ),
        ((TreeNode(1, TreeNode(2, TreeNode(3))),), 3),
        ((TreeNode(1, right=TreeNode(2, right=TreeNode(3))),), 3),
        ((TreeNode(1, TreeNode(2, right=TreeNode(3, TreeNode(4)))),), 4),
        ((TreeNode(0, TreeNode(-1), TreeNode(-1)),), 2),
    ]
    raise SystemExit(run_tests(Solution().maxDepth, cases))
