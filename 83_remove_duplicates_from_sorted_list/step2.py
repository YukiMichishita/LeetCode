from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        seeking_next = head
        while current:
            while seeking_next and seeking_next.val == current.val:
                seeking_next = seeking_next.next
            current.next = seeking_next
            current = seeking_next

        return head
