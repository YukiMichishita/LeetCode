from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_value_safely(node: Optional[ListNode]) -> int:
    if not node:
        return 0
    return node.val


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        sum_head = sentinel
        carry = False
        while l1 or l2:
            sum_ = get_value_safely(l1) + get_value_safely(l2) + int(carry)
            carry = sum_ >= 10
            sum_head.next = ListNode(sum_ % 10)
            sum_head = sum_head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            sum_head.next = ListNode(1)

        return sentinel.next
