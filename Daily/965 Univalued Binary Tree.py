# Url: https://leetcode.com/problems/univalued-binary-tree/
# Related Topics:
# Tree

# Example:
# Input: [1,1,1,1,1,null,1]
# Output: true


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverseTree(root, root.val)
    
    def traverseTree(self, root, val):
        if not root:
            return True
        if root.val != val:
            return False
        return self.traverseTree(root.left, val) and self.traverseTree(root.right, val)