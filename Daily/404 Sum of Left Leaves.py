# Url: https://leetcode.com/problems/sum-of-left-leaves/
# Related Topics:
# Tree

# Example:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.traverseWithFlag(root, False)
        
    def traverseWithFlag(self, root, isLeft):
        if not root:
            return 0
        if not root.left and not root.right:
            if isLeft:
                return root.val
            else:
                return 0
        return self.traverseWithFlag(root.left, True) + self.traverseWithFlag(root.right, False)