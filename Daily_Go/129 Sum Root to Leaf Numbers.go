// Url: https://leetcode.com/problems/sum-root-to-leaf-numbers/
// Related Topics:
// DepthFirstSearch Tree BinaryTree

// Example 1:
// Input: root = [1,2,3]
// Output: 25
// Explanation:
// The root-to-leaf path 1->2 represents the number 12.
// The root-to-leaf path 1->3 represents the number 13.
// Therefore, sum = 12 + 13 = 25.

// Example 2:
// Input: root = [4,9,0,5,1]
// Output: 1026
// Explanation:
// The root-to-leaf path 4->9->5 represents the number 495.
// The root-to-leaf path 4->9->1 represents the number 491.
// The root-to-leaf path 4->0 represents the number 40.
// Therefore, sum = 495 + 491 + 40 = 1026.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func sumNumbers(root *TreeNode) int {
    if root == nil {
        return 0
    }
    sum := 0
    var dfs func(*TreeNode, int)
    dfs = func(node *TreeNode, num int) {
        if node.Left == nil && node.Right == nil {
            sum += num + node.Val
        } else {
            num = num + node.Val
            if node.Left != nil {
                dfs(node.Left, num * 10)
            }
            if node.Right != nil {
                dfs(node.Right, num * 10)
            }
        }
    }
    dfs(root, 0)
    return sum
}