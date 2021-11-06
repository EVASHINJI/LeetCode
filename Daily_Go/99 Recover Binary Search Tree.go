// Url: https://leetcode.com/problems/recover-binary-search-tree/
// Related Topics:
// Tree DepthFirstSearch BinarySearchTree BinaryTree

// Example 1:
// Input: root = [1,3,null,null,2]
// Output: [3,1,null,null,2]
// Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

// Example 2:
// Input: root = [3,1,4,null,null,2]
// Output: [2,1,4,null,null,3]
// Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func update(pred, cur, x, y *TreeNode) (*TreeNode, *TreeNode) {
    if pred.Val > cur.Val {
        if pred.Val > x.Val {
            x = pred
        }
        if cur.Val < y.Val {
            y = cur
        }
    }
    return x, y
}

func recoverTree(root *TreeNode)  {
    var lastOrder *TreeNode
    x, y := &TreeNode{Val: math.MinInt64}, &TreeNode{Val: math.MaxInt64}
    
    cur := root
    for cur != nil {
        if cur.Left == nil {
            if lastOrder != nil {
                x, y = update(lastOrder, cur, x, y)
            }
            lastOrder = cur
            cur = cur.Right
        } else {
            pred := cur.Left
            for pred.Right != nil && pred.Right != cur {
                pred = pred.Right
            }
            if pred.Right == nil {
                pred.Right = cur
                cur = cur.Left
            } else {
                x, y = update(pred, cur, x, y)
                pred.Right = nil
                lastOrder = cur
                cur = cur.Right
            }
        }
    }
    x.Val, y.Val = y.Val, x.Val
}