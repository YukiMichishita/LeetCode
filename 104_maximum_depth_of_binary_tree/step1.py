from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root, 0)

    def dfs(self, root: TreeNode, depth):
        depth += 1
        l = depth
        r = depth

        if root.left:
            l = self.dfs(root.left, depth)

        if root.right:
            r = self.dfs(root.right, depth)

        return max(l, r)
