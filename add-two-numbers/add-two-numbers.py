# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while (l1 != None):
            num1 = num1 + str(l1.val)
            l1 = l1.next
        while (l2 != None):
            num2 = num2 + str(l2.val)
            l2 = l2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        print(num1)
        print(num2)
        ans = str(int(num1) + int(num2))
        answer = ListNode()
        temp = answer
        for i in reversed(ans):
            answer.next = ListNode(int(i))
            answer = answer.next
        answer = temp
        return answer.next
        
