# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        def zigzag(node,level):
            if not node:
                return 0
            if level ==len(res):
                res.append([])
            if level%2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0,node.val)
            zigzag(node.left,level+1)
            zigzag(node.right,level+1)
        zigzag(root,0)
        return res


        

        