# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        elif not root: return False

        def sameTree(p, q) :
            if not p and not q: return True

            if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            else:
                return False

        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        