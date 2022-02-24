// Url: https://leetcode.com/problems/reorder-list/
// Related Topics:
// LinkedList TwoPointers Stack Recursion

// Example 1:
// Input: head = [1,2,3,4]
// Output: [1,4,2,3]

// Example 2:
// Input: head = [1,2,3,4,5]
// Output: [1,5,2,4,3]

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

    public void mergeList(ListNode head1, ListNode head2) {
        ListNode head1_tmp, head2_tmp;
        while (head1 != null && head2 != null) {
            head1_tmp = head1.next;
            head2_tmp = head2.next;

            head1.next = head2;
            head1 = head1_tmp;

            head2.next = head1;
            head2 = head2_tmp;
        }
    }

    public ListNode midNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public void reorderList(ListNode head) {
        if (head == null) return;
        ListNode mid = midNode(head);
        ListNode head2 = reverseList(mid.next);
        mid.next = null;
        mergeList(head, head2);
    }
}