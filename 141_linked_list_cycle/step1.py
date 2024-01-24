from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked = set()
        current_node = head
        while current_node:
            if current_node in checked:
                return True
            checked.add(current_node)
            current_node = current_node.next
        return False
