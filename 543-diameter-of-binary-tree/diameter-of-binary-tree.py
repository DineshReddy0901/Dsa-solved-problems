# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ans = 0
class Solution(object):
    def diameterOfBinaryTree(self, root):
            global ans
            ans=0
   
            def maxdepth(root):
                global ans
                if root is None:
                   return 0
                left = maxdepth(root.left)
                right = maxdepth(root.right)

                curr_ans = left+right
                ans = max(ans,curr_ans)
                return 1+max(left,right)
            maxdepth(root)
            return ans

     