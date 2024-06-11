from typing import List, Optional
from collections import deque

# 任意のiとjについて、i < j ⇒ preorder[i]はpreorder[j]と同じ階層かより上の階層にある
# 任意のiとjについて、i < j ⇒ inorder[i]はinorder[j]よりも左側にある

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# step1 O(N^2) 分割統治法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_value = preorder[0]
        num_left_children = inorder.index(root_value)
        preorder_left = preorder[1:1 + num_left_children]
        preorder_right = preorder[1 + num_left_children:]
        inorder_left = inorder[:num_left_children]
        inorder_right = inorder[num_left_children + 1:]
        root = TreeNode(root_value)
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root


# O(N^2) rootから順に左右どちらに入れるかを毎回探索する。一番動作がわかりやすかったが一番遅かった。
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        value_to_inorder_index = {}
        for index, value in enumerate(inorder):
            value_to_inorder_index[value] = index

        root = TreeNode(preorder[0])
        for value in preorder[1:]:
            current = root
            inorder_index = value_to_inorder_index[value]
            while True:
                if inorder_index < value_to_inorder_index[current.val]:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(value)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(value)
                        break
        return root
                    

# O(N) HashMapを用いたstep1の改善
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        value_to_inorder_index = {}
        for index, value in enumerate(inorder):
            value_to_inorder_index[value] = index

        def build_tree_implementation(left, right):
            nonlocal preorder_root_index
            if left >= right:
                return None
            node_value = preorder[preorder_root_index]
            preorder_root_index += 1
            num_left_children = value_to_inorder_index[node_value]
            node = TreeNode(node_value)
            node.left = build_tree_implementation(left, num_left_children)
            node.right = build_tree_implementation(num_left_children + 1, right)
            return node

        preorder_root_index = 0
        return build_tree_implementation(0, len(preorder))
        
# O(N) 再帰を使わずにqueueを使った実装
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        value_to_preorder_index = {}
        for index, value in enumerate(preorder):
            value_to_preorder_index[value] = index
        value_to_inorder_index = {}
        for index, value in enumerate(inorder):
            value_to_inorder_index[value] = index

        root_value = preorder[0]
        root = TreeNode(root_value)
        nodes_to_check = deque([(root, 0, len(inorder) - 1)])
        while nodes_to_check:
            node, inorder_start, inorder_end = nodes_to_check.popleft()
            preorder_index = value_to_preorder_index[node.val]
            inorder_index = value_to_inorder_index[node.val]
            num_left_children = inorder_index - inorder_start
            num_right_children = inorder_end - inorder_index
            if num_left_children:
                left_child = TreeNode(preorder[preorder_index + 1])
                node.left = left_child
                nodes_to_check.append((left_child, inorder_start, inorder_index - 1))
            if num_right_children:
                right_child = TreeNode(preorder[preorder_index + num_left_children + 1])
                node.right = right_child
                nodes_to_check.append((right_child, inorder_index + 1, inorder_end))
        return root
