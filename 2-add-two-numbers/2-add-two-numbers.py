# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    CARRY = 0
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 or l2 or self.CARRY:
            _sum = 0 + self.CARRY
            if l1 and l1.val:
                _sum += l1.val
            if l2 and l2.val:
                _sum += l2.val
            self.CARRY = int(_sum / 10)
            if self.CARRY > 0:
                _sum = _sum % 10
            l1_next = l1 and l1.next
            l2_next = l2 and l2.next
            result = ListNode(_sum, self.addTwoNumbers(l1_next, l2_next))
            return result
        return None
        