# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def navigator(root):
    result = []
    if root:
        result.extend(navigator(root.left))
        result.append(root.val)
        result.extend(navigator(root.right))
    return result
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return navigator(root)
        