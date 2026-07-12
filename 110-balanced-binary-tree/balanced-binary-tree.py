# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

        def maxDepth(self,root):
            if not root:
               return 0

            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            return 1+max(left,right)      
        def isBalanced(self, root):
            if not root:
               return True
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            if abs(left - right)>1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)
