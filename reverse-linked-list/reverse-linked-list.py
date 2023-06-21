# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:      
       prev = head
       temp = []
       while (head != None): 
           temp.append(head.val)
           head = head.next    
       i = len(temp) - 1
       head = prev
       while (i >= 0):
            head.val = temp[i]
            i = i - 1
            head = head.next
       head = prev
       return head

