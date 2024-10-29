# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        diameter = 0

        diameter = self.maxDepth(root.left) + self.maxDepth(root.right)

        diameter = max(self.diameterOfBinaryTree(root.left), diameter)
        diameter = max(self.diameterOfBinaryTree(root.right), diameter)

        return diameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1