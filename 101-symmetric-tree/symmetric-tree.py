# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        # nested_res = []
        # res_la = []
        # def rightView(node,level):
        #     if not node:
        #         return 0
        #     if level == len(nested_res):
        #         nested_res.append([])
        #     nested_res[level].append(node.val)
        #     rightView(node.left,level+1)
        #     rightView(node.right,level+1)
        # rightView(root,0)
        if not root:
            return 0
        def symme(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return symme(left.left,right.right) and symme(left.right,right.left)
        return symme(root.left,root.right)
        
        
        
        