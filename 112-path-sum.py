# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # bfs
        if root is None:
            return False
        level = {root: sum - root.val}
        while len(level) > 0:
            next_level = {}
            for ele in level:
                if ele.left is None and ele.right is None and level[ele] == 0:
                    return True
                for child in [ele.left, ele.right]:
                    if child is not None:
                        next_level[child] = level[ele] - child.val
            level = next_level
        return False
        