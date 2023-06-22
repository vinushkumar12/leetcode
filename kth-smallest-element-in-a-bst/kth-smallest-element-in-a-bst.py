# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorderTraversal(root):
    result = []
    if root:
        result.extend(inorderTraversal(root.left))
        result.append(root.val)
        result.extend(inorderTraversal(root.right))
    return result

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = inorderTraversal(root)
        return result[k-1]
