from typing import Optional, List
from collections import deque
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# step1の改善
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        frontier = [root]
        ordered_nodes = []
        while frontier:
            ordered_nodes.append([node.val for node in frontier])
            new_frontier = []
            for node in frontier:
                if node.left:
                    new_frontier.append(node.left)
                if node.right:
                    new_frontier.append(node.right)
            frontier = new_frontier

        for i in range(len(ordered_nodes)):
            if i % 2 != 0:
                ordered_nodes[i].reverse()

        return ordered_nodes

# BFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth_to_ordered_values = defaultdict(deque)
        nodes_to_check = deque([(root, 0)])
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

# DFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        depth_to_ordered_values = defaultdict(deque)
        def traverse_recursively(node, depth):
            if not node:
                return
            if depth % 2 == 0:
                depth_to_ordered_values[depth].append(node.val)
            else:
                depth_to_ordered_values[depth].appendleft(node.val)
            traverse_recursively(node.left, depth + 1)
            traverse_recursively(node.right, depth + 1)
        traverse_recursively(root, 0)
        return [list(values) for values in depth_to_ordered_values.values()]

# ノードの探索自体をジグザグに行う
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        current_depth_nodes = [root]
        depth_to_ordered_values = defaultdict(list)
        depth = 0
        while current_depth_nodes:
            next_depth_nodes = []
            while current_depth_nodes:
                node = current_depth_nodes.pop()
                if not node:
                    continue
                depth_to_ordered_values[depth].append(node.val)
                if depth % 2 == 0:
                    next_depth_nodes.append(node.left)
                    next_depth_nodes.append(node.right)
                else:
                    next_depth_nodes.append(node.right)
                    next_depth_nodes.append(node.left)
            current_depth_nodes = next_depth_nodes
            depth += 1

        return list(depth_to_ordered_values.values())

