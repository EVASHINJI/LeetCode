# Url: https://leetcode.com/problems/add-two-numbers/
# Related Topics:
# Math LinkedList

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        l = root
        plus = 0
        while l1 or l2:
            i, j = 0, 0
            if l1: i = l1.val
            if l2: j = l2.val
            plus, cur = divmod(i+j+plus, 10)
            l.val = cur
            if (l1 and l1.next) or (l2 and l2.next):
                l.next = ListNode(0)
                l = l.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if plus:
            l.next = ListNode(plus)
        return root
                