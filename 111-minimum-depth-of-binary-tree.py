# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        min_depth = 1
        level = [root]
        while len(level) > 0:
            next_level = []
            for node in level:
                if node.left is None and node.right is None:
                    return min_depth
                for child in [node.left, node.right]:
                    if child is not None:
                        next_level.append(child)
            min_depth += 1
            level = next_level
        return min_depth
   