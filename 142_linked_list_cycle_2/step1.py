from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checked = set()
        current = head
        while current:
            if current in checked:
                return current
            checked.add(current)
            current = current.next
        return None
