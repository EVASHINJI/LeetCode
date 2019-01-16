# Url: https://leetcode.com/problems/same-tree/
# Related Topics:
# Tree DepthFirstSearch

# Example:
# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]
# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (not p) ^ (not q):
            return False
        if not p:
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
