# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return sorts(nums)

def sorts (nums):
        if not nums:
            return None
        middle = len(nums)//2
        root = TreeNode(nums[middle])
        root.left = sorts(nums[:middle])
        root.right = sorts(nums[middle + 1:])
        return root





        