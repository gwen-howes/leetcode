# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
            
        temp = root.left
        root.left = root.right
        root.right = temp

        if root.left != None:
            self.invertTree(root.left)
        if root.right != None:
            self.invertTree(root.right)

        return root
        