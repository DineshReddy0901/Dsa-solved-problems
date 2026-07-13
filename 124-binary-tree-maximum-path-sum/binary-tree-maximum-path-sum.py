# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        self.ans = float('-inf')
        def suM(node):
            if not node:
                return 0 
            left_max = max(suM(node.left),0)
            right_max = max(suM(node.right),0)
            self.ans = max(self.ans,left_max+right_max+node.val)
        
            return node.val + max(left_max,right_max)
        suM(root)
        return self.ans
            
    