from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ordered_nodes = []
        nodes_to_check = deque([(root, 0)])
        while nodes_to_check:
            node, level = nodes_to_check.popleft()
            if not node:
                continue
            if len(ordered_nodes) <= level:
                ordered_nodes.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    ordered_nodes[level].append(node.val)
                else:
                    ordered_nodes[level].appendleft(node.val)
            nodes_to_check.append((node.left, level + 1))
            nodes_to_check.append((node.right, level + 1))
        return [list(node) for node in ordered_nodes]

# DFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ordered_values = []
        def traverse_recursively(node, level):
            if not node:
                return
            if len(ordered_values) <= level:
                ordered_values.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    ordered_values[level].append(node.val)
                else:
                    ordered_values[level].appendleft(node.val)
            traverse_recursively(node.left, level + 1)
            traverse_recursively(node.right, level + 1)
        traverse_recursively(root, 0)
        return [list(node) for node in ordered_values]

