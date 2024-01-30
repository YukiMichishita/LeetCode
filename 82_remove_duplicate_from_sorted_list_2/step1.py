import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def safe_val(node: Optional[ListNode]):
    if not node:
        return None
    return node.val


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_linked_list = ListNode()
        unique_list_head = unique_linked_list
        current = head
        previous_val = math.nan
        while current:
            if current.val != previous_val and current.val != safe_val(current.next):
                unique_linked_list.next = ListNode(current.val)
                unique_linked_list = unique_linked_list.next
            previous_val = current.val
            current = current.next

        return unique_list_head.next
