// Url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
// Related Topics:
// Tree BinarySearchTree BinaryTree

// Example 1:
// Input: root = [3,9,20,null,null,15,7]
// Output: [[3],[20,9],[15,7]]

// Example 2:
// Input: root = [1]
// Output: [[1]]

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func zigzagLevelOrder(root *TreeNode) [][]int {
    ans := [][]int {}
    line := []*TreeNode {}
    if root != nil {
        line = append(line, root)
    }
    for len(line) > 0 {
        newLine := []*TreeNode {}
        newAnsLine := []int {}
        for _, node := range line {
            newAnsLine = append(newAnsLine, node.Val)
            if node.Left != nil {
                newLine = append(newLine, node.Left)
            }
            if node.Right != nil {
                newLine = append(newLine, node.Right)
            }
        }
        if len(ans) % 2 == 1 {
            for i, n := 0, len(newAnsLine); i < n/2; i++ {
                newAnsLine[i], newAnsLine[n-i-1] = newAnsLine[n-i-1], newAnsLine[i]
            }
        }
        ans = append(ans, newAnsLine)
        line = newLine
    }
    return ans
}