/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        int left = 0;
        int right = 0;
        
        left = MaxDepth(root.left);
        right = MaxDepth(root.right);
        
        if (left > right) {
            return left + 1;
        } else {
            return right + 1;
        }
        
    }
}