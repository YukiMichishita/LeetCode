from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        diff_from_target = targetSum - root.val
        if not (root.left or root.right):
            return diff_from_target == 0

        return self.hasPathSum(root.left, diff_from_target) or self.hasPathSum(root.right, diff_from_target)
