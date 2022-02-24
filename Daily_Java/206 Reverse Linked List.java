// Url: https://leetcode.com/problems/reverse-linked-list/
// Related Topics:
// LinkedList Recursion

// Example 1:
// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]

// Example 2:
// Input: head = [1,2]
// Output: [2,1]

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
    public ListNode reverseList(ListNode head) {
        ListNode fake = new ListNode();
        while (head != null) {
            ListNode next = head.next;
            head.next = fake.next;
            fake.next = head;
            head = next;
        }
        return fake.next;
    }
}