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

# inorder traversal(stack)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def append_left_nodes(node, nodes):
            while node:
                nodes.append(node)
                node = node.left

        nodes_to_check = []
        append_left_nodes(root, nodes_to_check)
        lower_bound = -inf
        while nodes_to_check:
            current = nodes_to_check.pop()
            if current.val <= lower_bound:
                return False
            lower_bound = current.val
            if current.right:
                if current.right.val <= current.val:
                    return False
                append_left_nodes(current.right, nodes_to_check)
        return True

# inorder traversal(再帰) 最初に全てのノードをinorderでソートしたリストを作ってからそれを探索する。
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_sort(node, nodes):
            if not node:
                return
            if node.left:
                inorder_sort(node.left, nodes)
            nodes.append(node)
            if node.right:
                inorder_sort(node.right, nodes)

        inordered_nodes = []
        inorder_sort(root, inordered_nodes)
        prev_value = -inf
        for node in inordered_nodes:
            if node.val <= prev_value:
                return False
            prev_value = node.val
        return True

        
