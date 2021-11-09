// Url: https://leetcode.com/problems/path-sum-ii/
// Related Topics:
// Backtracking DepthFirstSearch Tree BinaryTree

// Example 1:
// Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
// Output: [[5,4,11,2],[5,8,4,5]]
// Explanation: There are two paths whose sum equals targetSum:
// 5 + 4 + 11 + 2 = 22
// 5 + 8 + 4 + 5 = 22

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func pathSum(root *TreeNode, targetSum int) [][]int {
    ans := [][]int{}
    var dfs func([]*TreeNode, []int, int)
    dfs = func (path []*TreeNode, vals []int, targetSum int) {
        node := path[len(path)-1]
        vals = append(vals, node.Val)
        targetSum -= node.Val
        if (node.Left == nil && node.Right == nil) {
            if targetSum == 0 {
                cp := make([]int, len(vals))
                copy(cp, vals)
                ans = append(ans, cp)
            }
        } else {
            if node.Left != nil {
                dfs(append(path, node.Left), vals, targetSum)
            }
            if node.Right != nil {
                dfs(append(path, node.Right), vals, targetSum)
            }
        }
        vals = vals[:len(path)-1]
        targetSum += targetSum
    }
    if root == nil {
        return ans
    }
    path := []*TreeNode{}
    path = append(path, root)
    dfs(path, []int{}, targetSum)
    return ans
}