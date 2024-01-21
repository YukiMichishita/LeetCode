import copy
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return copy.deepcopy(root2)
        if not root2:
            return copy.deepcopy(root1)

        merged_left = self.mergeTrees(root1.left, root2.left)
        merged_right = self.mergeTrees(root1.right, root2.right)
        return TreeNode(val=root1.val + root2.val, left=merged_left, right=merged_right)
