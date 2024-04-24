from typing import Optional
from math import inf
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# step1と同様、根からDFSでチェックしていく
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_nodes_recursively(node, lower_bound, upper_bound):
            if not node:
                return True
            if not lower_bound < node.val < upper_bound:
                return False
            if not check_nodes_recursively(node.left, lower_bound, node.val):
                return False
            return check_nodes_recursively(node.right, node.val, upper_bound)
        return check_nodes_recursively(root, -inf, inf)

# BFS
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 最初単なるリストにしていたがリストの先頭を取り出すのは遅いのでdequeに変更した。
        # LeetCodeでのRuntimeはほぼ変わらなかったが、入力が最大で10^4程度で小さいためか。
        nodes_to_check = deque([(root, -inf, inf)])
        while nodes_to_check:
            node, lower_bound, upper_bound = nodes_to_check.popleft()
            if not node:
                continue
            if not lower_bound < node.val < upper_bound:
                return False
            nodes_to_check.append((node.left, lower_bound, node.val))
            nodes_to_check.append((node.right, node.val, upper_bound))
        return True
