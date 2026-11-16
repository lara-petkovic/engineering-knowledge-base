"""Path Sum (Easy).

Problem: https://leetcode.com/problems/path-sum/

Time: O(n)
Space: O(h) - h is the tree height
"""

from algorithms.test_helpers import run_tests
from algorithms.trees.helpers import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )


if __name__ == "__main__":
    cases = [
        ((None, 0), False),
        ((TreeNode(1), 1), True),
        ((TreeNode(1), 2), False),
        ((TreeNode(0), 0), True),
        ((TreeNode(1, TreeNode(2)), 1), False),
        ((TreeNode(1, TreeNode(2)), 3), True),
        ((TreeNode(1, right=TreeNode(2)), 3), True),
        ((TreeNode(1, TreeNode(2), TreeNode(3)), 5), False),
        ((TreeNode(5, TreeNode(-3)), 2), True),
        ((TreeNode(-2, right=TreeNode(-3)), -5), True),
        ((TreeNode(1, TreeNode(-1, TreeNode(2))), 0), False),
        (
            (
                TreeNode(
                    5,
                    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, right=TreeNode(1))),
                ),
                22,
            ),
            True,
        ),
    ]
    raise SystemExit(run_tests(Solution().hasPathSum, cases))
