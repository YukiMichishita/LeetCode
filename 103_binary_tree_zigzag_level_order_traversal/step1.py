from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ordered_nodes = []
        nodes_to_check = deque([(root, 0)])

        while nodes_to_check:
            node, level = nodes_to_check.popleft()
            if not node:
                continue
            if len(ordered_nodes) <= level:
                ordered_nodes.append([node.val])
            else:
                ordered_nodes[level].append(node.val)
            nodes_to_check.append((node.left, level + 1))
            nodes_to_check.append((node.right, level + 1))

        for i in range(len(ordered_nodes)):
            if i % 2 != 0:
                ordered_nodes[i].reverse()

        return ordered_nodes
