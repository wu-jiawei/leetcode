# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
   

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        # check if two trees are mirror image of each other
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)