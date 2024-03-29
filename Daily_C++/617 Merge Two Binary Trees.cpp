// Url: https://leetcode.com/problems/merge-two-binary-trees/
// Related Topics:
// Tree

// Example 1:
// Input: 
//     Tree 1                     Tree 2                  
//           1                         2                             
//          / \                       / \                            
//         3   2                     1   3                        
//        /                           \   \                      
//       5                             4   7                  
// Output: 
// Merged tree:
//          3
//         / \
//        4   5
//       / \   \ 
//      5   4   7


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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 && t2) {
            TreeNode *node = new TreeNode(t1->val + t2->val);
            node->left = mergeTrees(t1->left, t2->left);
            node->right = mergeTrees(t1->right, t2->right);
            return node;
        }
        return t1 ? t1: t2;
    }
};