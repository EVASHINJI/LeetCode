// Url: https://leetcode.com/problems/linked-list-cycle/
// Related Topics:
// HashTable LinkedList TwoPointers

// Example 1:
// Input: head = [3,2,0,-4], pos = 1
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (true) {
            try {
                slow = slow.next;
                fast = fast.next.next;
            } catch (Exception e) {
                return false;
            }
            if (slow == fast) return true;
        }
    }
}