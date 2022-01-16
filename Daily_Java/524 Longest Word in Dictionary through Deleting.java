// Url: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
// Related Topics:
// LinkedList TwoPointers

// Example 1:
// Input: head = [1,2,3,3,4,4,5]
// Output: [1,2,5]

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode fakeHead = new ListNode(head.val - 1, head);

        ListNode pred = fakeHead;
        while (head != null) {
            if (head.next != null && head.val == head.next.val) {
                while (head.next != null && head.val == head.next.val) {
                    head = head.next;
                }
                pred.next = head.next;
            } else {
                pred = head;
            }
            head = head.next;
        }
        return fakeHead.next;
    }
}