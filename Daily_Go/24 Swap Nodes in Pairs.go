// Url: https://leetcode.com/problems/swap-nodes-in-pairs/
// Related Topics:
// LinkedList Recursion

// Example 1:
// Input: head = [1,2,3,4]
// Output: [2,1,4,3]

// Example 2:
// Input: head = []
// Output: []

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    dynamic_head := &ListNode{Val: -1, Next: head}
    prev, ptr1 := dynamic_head, head
    for ptr1 != nil && ptr1.Next != nil {
        ptr2 := ptr1.Next
        next := ptr2.Next
        prev.Next = ptr2
        ptr2.Next = ptr1
        ptr1.Next = next
        prev = ptr1
        ptr1 = next
    }
    return dynamic_head.Next
}