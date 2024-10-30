# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        res = True

        def dfs(root):
            nonlocal res

            if not root: return 0

            right = dfs(root.right)
            left = dfs(root.left)

            difference = right - left
        
            if difference <= -2 or difference >= 2:
                res = False

            return max(right, left) + 1

        dfs(root)
        return res