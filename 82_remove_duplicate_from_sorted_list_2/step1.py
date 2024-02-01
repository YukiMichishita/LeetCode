from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        unique_linked_list = sentinel
        current = head
        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                continue
            unique_linked_list.next = ListNode(current.val)
            unique_linked_list = unique_linked_list.next
            current = current.next

        return sentinel.next
