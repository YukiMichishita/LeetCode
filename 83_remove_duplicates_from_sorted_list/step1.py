from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        former = head
        while current:
            if former.val < current.val:
                former = former.next
            if former.val == current.val:
                current = current.next
                former.next = current
        return head
