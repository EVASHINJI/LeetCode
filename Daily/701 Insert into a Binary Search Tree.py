# Url: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Related Topics:
# Tree

# Example:
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        return root