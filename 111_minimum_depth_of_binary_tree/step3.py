import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left = math.inf
        right = math.inf
        if root.left:
            left = self.minDepth(root.left) + 1
        if root.right:
            right = self.minDepth(root.right) + 1
        return min(left, right)
