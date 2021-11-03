// Url: https://leetcode.com/problems/rotate-list/
// Related Topics:
// LinkedList TwoPointers

// Example 1:
// Input: head = [1,2,3,4,5], k = 2
// Output: [4,5,1,2,3]

// Example 2:
// Input: head = [0,1,2], k = 4
// Output: [2,0,1]

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || k == 0 {
        return head
    }
    l := 0
    cur := head
    tail := head
    for cur != nil {
        l++
        if cur.Next == nil {
            tail = cur
        }
        cur = cur.Next
    }
    k = k % l
    if k == 0 {
        return head
    }
    n := l - k - 1
    cur = head
    for n > 0 {
        cur = cur.Next
        n--
    }
    tail.Next = head
    new_head := cur.Next
    cur.Next = nil
    return new_head
}