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
        l1_head = l1
        l2_head = l2
        dummy_sum_head = ListNode()
        sum_head = dummy_sum_head
        carry = False
        while l1_head or l2_head:
            sum_ = get_value_safely(l1_head) + get_value_safely(l2_head) + int(carry)
            carry = sum_ > 9
            sum_head.next = ListNode(sum_ % 10)
            sum_head = sum_head.next
            if l1_head:
                l1_head = l1_head.next
            if l2_head:
                l2_head = l2_head.next

        if carry:
            sum_head.next = ListNode(1)

        return dummy_sum_head.next
