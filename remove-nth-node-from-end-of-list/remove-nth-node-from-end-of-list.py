# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(None)
        temp_2 = head
        length = 0
        while (head != None):
            length = length + 1
            head = head.next
        head = temp_2
        temp_2 = temp
        counter = 1
        while (head != None):
            if (counter != length + 1 - n):
                temp.next = ListNode(head.val)
                temp = temp.next
            counter = counter + 1
            head = head.next
        temp = temp_2
        return temp.next
        
            
            
            
