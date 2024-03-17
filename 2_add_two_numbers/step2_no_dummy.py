from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_value_safely(node: Optional[ListNode]) -> int:
    if not node:
        return 0
    return node.val

# 戻り値は(和, 繰り上がり)
def add_one_digit(val1: int, val2: int, carry: int) -> (int, int):
    digit = val1 + val2 + carry
    return (digit % 10, digit // 10)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit, carry = add_one_digit(get_value_safely(l1), get_value_safely(l2), 0)
        l1 = l1.next
        l2 = l2.next
        root = ListNode(digit)
        sum_head = root
        while l1 or l2:
            digit, carry = add_one_digit(get_value_safely(l1), get_value_safely(l2), carry)
            sum_head.next = ListNode(digit)
            sum_head = sum_head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            sum_head.next = ListNode(1)

        return root
