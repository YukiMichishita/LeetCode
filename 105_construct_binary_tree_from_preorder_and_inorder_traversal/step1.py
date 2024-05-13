from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_value = preorder[0] 
        num_of_left_nodes = inorder.index(root_value)
        preorder_left = preorder[1:1 + num_of_left_nodes]
        preorder_right = preorder[1 + num_of_left_nodes:]
        inorder_left = inorder[:num_of_left_nodes]
        inorder_right = inorder[num_of_left_nodes + 1:]
        root = TreeNode(root_value)
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
