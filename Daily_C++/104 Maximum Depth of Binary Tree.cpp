// Url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
// Related Topics:
// Tree DepthFirstSearch

// Example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its depth = 3.


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
    int maxDepth(TreeNode* root) {
        if (!root)
            return 0;
        queue<TreeNode*> q;
        q.push(root);
        int ans = 0;
        while (!q.empty()) {
            ans++;
            for (int i = 0, len = q.size(); i < len; i++) {
                TreeNode* n = q.front();
                q.pop();
                
                if (n->left) q.push(n->left);
                if (n->right) q.push(n->right);
            }
        }
        return ans;
    }
};