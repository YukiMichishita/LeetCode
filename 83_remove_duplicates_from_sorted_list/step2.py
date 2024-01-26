from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        first_node_of_same_val = head
        while current:
            if first_node_of_same_val.val == current.val:
                current = current.next
                continue
            first_node_of_same_val.next = current
            first_node_of_same_val = current

        if first_node_of_same_val:
            first_node_of_same_val.next = None
        return head
