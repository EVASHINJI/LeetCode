# Url: https://leetcode.com/problems/add-one-row-to-tree/
# Related Topics:
# Tree

# Example:
# Input: 
# A binary tree as following:
#        4
#      /   \
#     2     6
#    / \   / 
#   3   1 5   
# v = 1
# d = 2
# Output: 
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     / 
#  3   1   5   


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: 'TreeNode', v: 'int', d: 'int') -> 'TreeNode':
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        if d == -1:
            new_root = TreeNode(v)
            new_root.right = root
            return new_root
        if root:
            root.left = self.addOneRow(root.left, v, abs(d) - 1)
            root.right = self.addOneRow(root.right, v, 1 - abs(d))
        return root