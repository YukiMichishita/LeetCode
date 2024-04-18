from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, lower_bound, upper_bound) -> bool:
            if not node:
                return True
            if not lower_bound < node.val < upper_bound:
                return False
            if not is_valid(node.left, lower_bound, node.val):
                return False
            return is_valid(node.right, node.val, upper_bound)
        return is_valid(root, -inf, inf)
