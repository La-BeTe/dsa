# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def convert_list_node_to_num(list_node):
    result = 0
    power_of_10 = 0
    while True:
        result = (list_node.val * (10 ** power_of_10)) + result
        power_of_10 += 1
        list_node = list_node.next
        if not list_node:
            break
    return result

def convert_num_to_list_node(num):
    print(str(num)[-1])
    if num == 0:
        return ListNode(0, None)
    num = int(num)
    return ListNode(num % 10, convert_num_to_list_node(num / 10)) if num >= 1 else None
    
            
    
    
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
        