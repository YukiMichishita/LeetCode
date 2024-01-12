from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            # 元の木のノードへの参照を返しているので書き換えが相互に影響する。問題になる場合はdeepcopyにする。
            return root2
        if not root2:
            # 元の木のノードへの参照を返しているので書き換えが相互に影響する。問題になる場合はdeepcopyにする。
            return root1
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged
