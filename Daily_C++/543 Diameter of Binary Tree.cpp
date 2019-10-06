// Url: https://leetcode.com/problems/diameter-of-binary-tree/
// Related Topics:
// Tree

// Example:
// Given a binary tree
//           1
//          / \
//         2   3
//        / \     
//       4   5    
// Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int bfs(TreeNode* node, int &ans) {
        if (!node) return 0;
        int left_diame = 0, right_diame = 0;
        int left_depth = bfs(node->left, left_diame);
        int right_depth = bfs(node->right, right_diame);
        ans = max(left_depth+right_depth, max(left_diame, right_diame));
        return max(left_depth, right_depth) + 1;   
    }

public:
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        bfs(root, ans);
        return ans;
    }
};