// Url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
// Related Topics:
// Tree BinaryTree DepthFirstSearch

// Example 1:
// Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
// Output: 3
// Explanation: The LCA of nodes 5 and 1 is 3.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (root.val == p.val || root.val == q.val) return root;
        TreeNode isLeft = lowestCommonAncestor(root.left, p, q);
        TreeNode isRight = lowestCommonAncestor(root.right, p, q);
        if (isLeft != null && isRight != null) return root;
        return isLeft != null ? isLeft : isRight;
    }
}