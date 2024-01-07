from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def merge(self, node1: Optional[TreeNode], node2: Optional[TreeNode], merged: Optional[TreeNode]):

        node1_value = 0
        node1_left = None
        node1_right = None
        if node1:
            node1_value = node1.val
            node1_left = node1.left
            node1_right = node1.right

        node2_value = 0
        node2_left = None
        node2_right = None
        if node2:
            node2_value = node2.val
            node2_left = node2.left
            node2_right = node2.right
        merged.val = node1_value + node2_value

        if node1_left or node2_left:
            new_left = TreeNode()
            merged.left = new_left
            self.merge(node1_left, node2_left, new_left)

        if node1_right or node2_right:
            new_right = TreeNode()
            merged.right = new_right
            self.merge(node1_right, node2_right, new_right)

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 or root2):
            return None
        merged = TreeNode()
        self.merge(root1, root2, merged)
        return merged
