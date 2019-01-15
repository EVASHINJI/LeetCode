# Url: https://leetcode.com/problems/search-in-a-binary-search-tree/
# Related Topics:
# Tree

# Example:
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3

# And the value to search: 2
# You should return this subtree:

#       2     
#      / \   
#     1   3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)