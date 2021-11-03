// Url: https://leetcode.com/problems/partition-list/
// Related Topics:
// LinkedList TwoPointers

// Example 1:
// Input: head = [1,4,3,2,5,2], x = 3
// Output: [1,2,2,4,3,5]

// Example 2:
// Input: head = [2,1], x = 2
// Output: [1,2]

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
    if head == nil {
        return head
    }
    dummy1 := &ListNode{Val:0, Next:nil}
    dummy2 := &ListNode{Val:0, Next:nil}
    less_head, other_head := dummy1, dummy2
    cur := head
    for cur != nil {
        if cur.Val < x {
            less_head.Next = cur
            less_head = cur
        } else {
            other_head.Next = cur
            other_head = cur
        }
        cur = cur.Next
    }
    if less_head == dummy1 {
        return head
    }
    less_head.Next = dummy2.Next
    other_head.Next = nil
    return dummy1.Next
}