# Url: https://leetcode.com/problems/diameter-of-binary-tree/
# Related Topics:
# Tree

# Example:
# Given a binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxDiameter = 0
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.maxDiameter
        
    def traverse(self, root):
        if not root:
            return -1
        left = self.traverse(root.left) + 1
        right = self.traverse(root.right) + 1
        self.maxDiameter = max(self.maxDiameter, left + right)
        return max(left, right)