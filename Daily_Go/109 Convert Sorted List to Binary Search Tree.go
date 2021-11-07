// Url: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
// Related Topics:
// LinkedList DivideAndConquer Tree BinarySearchTree BinaryTree

// Example 1:
// Input: head = [-10,-3,0,5,9]
// Output: [0,-3,9,-10,null,5]
// Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func sortedArrayToBST(vals []int, start int, end int) *TreeNode {
    if start >= end {
        return nil
    }
    mid := start + (end - start) / 2
    return &TreeNode{Val:vals[mid], 
                    Left:sortedArrayToBST(vals, start, mid),
                    Right:sortedArrayToBST(vals, mid+1, end)}
}

func sortedListToBST(head *ListNode) *TreeNode {
    vals := []int{}
    for head != nil {
        vals = append(vals, head.Val)
        head = head.Next
    }
    return sortedArrayToBST(vals, 0, len(vals))
}