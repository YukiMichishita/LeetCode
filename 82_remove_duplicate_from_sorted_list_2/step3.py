from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        last_unique_node = dummy
        current = head
        val_to_remove = None

        while current:
            if current.val == val_to_remove:
                current = current.next
                continue
            if current.next and current.val == current.next.val:
                val_to_remove = current.val
                continue
            last_unique_node.next = ListNode(current.val)
            last_unique_node = last_unique_node.next
            current = current.next

        return dummy.next
