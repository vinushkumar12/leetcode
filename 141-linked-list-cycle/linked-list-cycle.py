# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        while f and s:
            s = s.next
            if f.next != None:
                f = f.next.next
            else:
                return False
            if f == s and s.next != None:
                return True
        return False
        