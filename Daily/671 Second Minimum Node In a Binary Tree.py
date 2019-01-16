# Url: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Related Topics:
# Tree

# Example:
# Input: 
#     2
#    / \
#   2   5
#      / \
#     5   7
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        mi, ans = root.val, float('inf')
        q = [root]
        while q:
            node = q.pop()
            if not node.left:
                if mi < node.val < ans:
                    ans = node.val
            else:
                q.extend([node.left, node.right])

        return ans if ans < float('inf') else -1