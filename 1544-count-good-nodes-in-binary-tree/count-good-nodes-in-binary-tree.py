# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        
        
        def dfs(node,max_till_now):
            if not node:
                return 0
            count =0
            if node.val >=max_till_now:
                count =1
            max_till_now = max(max_till_now,node.val)
            count+= dfs(node.left,max_till_now)
            count+= dfs(node.right,max_till_now)
            return count
        return dfs(root,root.val)
        
        