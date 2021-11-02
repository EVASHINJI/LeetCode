// Url: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Related Topics:
// LinkedList TwoPointers

// Example 1:
// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]

// Example 2:
// Input: head = [1], n = 1
// Output: []

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    if head == nil {
        return nil
    }
    dynamic_head := &ListNode{Val: -1, Next: head}
    cur := dynamic_head
    for n >= 0 {
        cur = cur.Next
        n--
    }
    prev := dynamic_head
    for cur != nil {
        prev, cur = prev.Next, cur.Next
    }
    prev.Next = prev.Next.Next
    return dynamic_head.Next
}