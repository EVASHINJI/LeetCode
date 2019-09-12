// Url: https://leetcode.com/problems/invert-binary-tree/
// Related Topics:
// Tree

// Example 1:
// Input:
//      4
//    /   \
//   2     7
//  / \   / \
// 1   3 6   9
// Output:
//      4
//    /   \
//   7     2
//  / \   / \
// 9   6 3   1


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
    TreeNode* invertTree(TreeNode* root) {
        if (!root)
            return NULL;
        queue<TreeNode *> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode *node = q.front();
            q.pop();
        
            TreeNode* tmp = node->left;
            node->left = node->right;
            node->right = tmp;
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return root;
    }
};