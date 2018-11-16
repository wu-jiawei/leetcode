# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def InorderTraversal(self, root1, temp_ls):
            # temp_ls will be a list representing the inorder traversal
            # of tree
            if root1 == None:
                return
            self.InorderTraversal(root1.left, temp_ls)
            temp_ls.append(root1.val)
            self.InorderTraversal(root1.right, temp_ls)
            return 

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        temp_ls = []
        self.InorderTraversal(root, temp_ls)
        for val in temp_ls:
            print("{}\t".format(val))
    
        beg = 0
        end = len(temp_ls) - 1
        while beg < end:
            if temp_ls[beg] != temp_ls[end]:
                return False
            beg += 1
            end -= 1
        
        return True

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = None #TreeNode(3)
root.left.right = TreeNode(3)
root.right = TreeNode(2)
root.right.left = None # TreeNode(4)
root.right.right = TreeNode(3)

print("symmetric? {}".format(Solution().isSymmetric(root)))
