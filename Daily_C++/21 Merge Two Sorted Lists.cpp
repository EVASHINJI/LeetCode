// Url: https://leetcode.com/problems/merge-two-sorted-lists/
// Related Topics:
// LinkedList

// Example:
// Input: 1->2->4, 1->3->4
// Output: 1->1->2->3->4->4


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) return l2;
        if (!l2) return l1;
        ListNode* head;
        if (l1->val < l2->val) {
            head = l1;
            l1 = l1->next;
        } else {
            head = l2;
            l2 = l2->next;
        }
        ListNode* rest = head;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                rest->next = l1;
                l1 = l1->next;
            } else {
                rest->next = l2;
                l2 = l2->next;
            }
            rest = rest->next;
        }
        if (l1) rest->next = l1;
        if (l2) rest->next = l2;
        return head;
    }
};