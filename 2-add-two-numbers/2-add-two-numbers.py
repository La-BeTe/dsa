# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def convert_list_node_to_num(listNode):
    result = 0
    power_of_10 = 0
    while True:
        result = (listNode.val * (10 ** power_of_10)) + result
        power_of_10 += 1
        listNode = listNode.next
        if not listNode:
            break
    return result

def stringToListNode(string):
    string = str(string)
    result = None
    for i in string:
        result = ListNode(i, result)
    return result
            
    
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = convert_list_node_to_num(l1) + convert_list_node_to_num(l2)
        return stringToListNode(result)
        