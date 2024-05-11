# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        answer = ListNode()
        temp = answer
        while list1:
            if list2 and list1.val <= list2.val:
                answer.next = list1
                list1 = list1.next
            elif list2 and list1.val > list2.val:
                answer.next = list2
                list2 = list2.next
            elif list1 and list2 is None:
                answer.next = list1
                return temp.next
            answer = answer.next
        if list2:
            answer.next = list2
        if list1:
            answer.next = list1
        return temp.next

                
        
        

        