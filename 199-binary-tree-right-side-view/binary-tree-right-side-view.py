# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        nested_res = []
        def rightView(node,level):
            if not node:
                return 0
            if level == len(nested_res):
                nested_res.append([])
            nested_res[level].append(node.val)
            rightView(node.left,level+1)
            rightView(node.right,level+1)
        rightView(root,0)
        return [res[-1] for res in nested_res]


    
        