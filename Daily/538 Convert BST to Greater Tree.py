# Url: https://leetcode.com/problems/convert-bst-to-greater-tree/
# Related Topics:
# Tree

# Example:
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.postOrderTraverse(root, 0)
        return root
        
        
    def postOrderTraverse(self, root, val):
        if not root:
            return val
        root.val += self.postOrderTraverse(root.right, val)
        return self.postOrderTraverse(root.left, root.val)
        