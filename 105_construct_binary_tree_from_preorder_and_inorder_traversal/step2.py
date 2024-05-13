from typing import List, Optional

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
        num_of_left_nodes = inorder.index(root_value)
        preorder_left = preorder[1:1 + num_of_left_nodes]
        preorder_right = preorder[1 + num_of_left_nodes:]
        inorder_left = inorder[:num_of_left_nodes]
        inorder_right = inorder[num_of_left_nodes + 1:]
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
            root_value = preorder[preorder_root_index]
            preorder_root_index += 1
            num_of_left_nodes = value_to_inorder_index[root_value]
            root = TreeNode(root_value)
            root.left = build_tree_implementation(left, num_of_left_nodes)
            root.right = build_tree_implementation(num_of_left_nodes + 1, right)
            return root

        preorder_root_index = 0
        return build_tree_implementation(0, len(preorder))
