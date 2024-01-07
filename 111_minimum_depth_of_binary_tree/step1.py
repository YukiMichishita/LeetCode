import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        if not (root.left or root.right):
            return 1

        l = math.inf
        r = math.inf
        if root.left:
            l = self.dfs(root.left)
        if root.right:
            r = self.dfs(root.right)

        return min(l, r) + 1
