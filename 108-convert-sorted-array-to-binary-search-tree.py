# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x);
    self.val = x
    self.left = None
    self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0:
            return None
        mid = n / 2
        result = TreeNode(nums[mid])
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid + 1:])
        result.left = left
        result.right = right
        return result