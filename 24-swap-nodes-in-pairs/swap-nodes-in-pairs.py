# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        save = head
        n = head.next
        temp = n.next
        n.next = save
        save.next = temp
        prev = save
        save = save.next
        head = n
        while save and save.next:
            n = save.next
            prev.next = n
            temp = n.next
            n.next = save
            save.next = temp
            prev = save
            if save.next:
                save = save.next
        return head
                

