# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        temp = head
        count = []
        while (head != None):
            count.append(head.val)
            head = head.next
        head = temp
        def inserter(count):
            if (len(count) == 0):
                return None
            middle = (len(count)) // 2
            ans = TreeNode(count[middle])
            ans.right = inserter(count[middle + 1:])
            ans.left = inserter(count[:middle])
            return ans
        return inserter(count)
        
