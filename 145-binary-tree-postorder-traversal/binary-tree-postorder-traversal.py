# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []

        def Postorder(node):
            if not node:
                return 0
            left = Postorder(node.left)
            right =Postorder(node.right)

            return result.append(node.val)
            
        Postorder(root)
        return result
        
    


        
        