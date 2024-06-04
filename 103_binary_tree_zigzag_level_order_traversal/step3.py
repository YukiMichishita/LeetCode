from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes_to_check = deque([(root, 0)])
        depth_to_ordered_values = defaultdict(deque)
        while nodes_to_check:
            node, depth = nodes_to_check.popleft() 
            if not node:
                continue
            if depth % 2 == 0:
                depth_to_ordered_values[depth].append(node.val)
            else:
                depth_to_ordered_values[depth].appendleft(node.val)
            nodes_to_check.append((node.left, depth + 1))
            nodes_to_check.append((node.right, depth + 1))
        return [list(values) for values in depth_to_ordered_values.values()]
