# Url: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Related Topics:
# Tree DepthFirstSearch BreadthFirstSearch

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        mi = min(left, right)
        if mi == 0:
            return max(left, right) + 1
        else:
            return mi + 1