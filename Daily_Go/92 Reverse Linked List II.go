// Url: https://leetcode.com/problems/reverse-linked-list-ii/
// Related Topics:
// LinkedList

// Example 1:
// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]

// Example 2:
// Input: head = [5], left = 1, right = 1
// Output: [5]

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseLinkedList(head *ListNode) *ListNode {
    if head == nil {
        return head
    }
    var pre *ListNode
    cur := head
    for cur != nil {
        nxt := cur.Next
        cur.Next = pre
        pre = cur
        cur = nxt
    }
    return pre
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
    dummy := &ListNode{Val: -1, Next: head}
    cur := dummy
    i := 0
    for ; i < left - 1; i++ {
        cur = cur.Next
    }
    pre := cur
    if pre == nil || pre.Next == nil {
        return head
    }
    leftNode := pre.Next
    for ; i < right; i++ {
        cur = cur.Next
    }
    rightNode := cur
    cur = cur.Next
    rightNode.Next = nil
    pre.Next = reverseLinkedList(leftNode)
    leftNode.Next = cur
    return dummy.Next
}