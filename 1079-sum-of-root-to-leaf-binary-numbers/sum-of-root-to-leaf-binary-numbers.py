# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        
        def depth(node,current):
            if not node:
                return 0

            current = current*2+node.val

            if not node.left and not node.right:
                    return current

            return depth(node.left,current) + depth(node.right,current)
        return depth(root,0)
            