// Url: https://leetcode.com/problems/validate-binary-search-tree/
// Related Topics:
// Tree DepthFirstSearch BinarySearchTree BinaryTree

// Example 1:
// Input: root = [2,1,3]
// Output: true

// Example 2:
// Input: root = [5,1,4,null,null,3,6]
// Output: false
// Explanation: The root node's value is 5 but its right child's value is 4.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func isValidBST(root *TreeNode) bool {
    inOrder := math.MinInt64
    stack := [] *TreeNode{}
    for len(stack) > 0 || root != nil {
        for root != nil {
            stack = append(stack, root)
            root = root.Left
        }
        root = stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        if root.Val <= inOrder {
            return false
        }
        inOrder = root.Val
        root = root.Right
    }
    return true
}