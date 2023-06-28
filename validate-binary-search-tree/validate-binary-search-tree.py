# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        answer = []
        def inorder(root):
            if (root):
                inorder(root.left)
                answer.append(root.val)
                inorder(root.right)
        inorder(root)
        print(answer)
        for i in range(len(answer)):
            if (i == 0):
                continue
            elif (answer[i] <= answer[i - 1]):
                return False
        return True