# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None
        vals = []
        temp = head
        while (temp != None):
            vals.append(temp.val)
            temp = temp.next
        vals.sort()
        temp = head
        for i in vals:
            head.val = i
            head = head.next
        head = temp
        return head

        
        