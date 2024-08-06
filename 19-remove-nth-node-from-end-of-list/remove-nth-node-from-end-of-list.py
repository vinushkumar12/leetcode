# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        save = head
        length = 0
        while save:
            length += 1
            save = save.next
        x = 0
        if n == length:
            return head.next
        save = head
        prev = None
        nexts = head.next
        while save:
            x += 1
            if x == length - n + 1:
                prev.next = nexts
            prev = save
            save = save.next
            if save:
                nexts = nexts.next
        return head
