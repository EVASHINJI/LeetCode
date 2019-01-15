# Url: https://leetcode.com/problems/trim-a-binary-search-tree/
# Related Topics:
# Tree 

# Example:
# Input: 
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1

#   L = 1
#   R = 3

# Output: 
#       3
#      / 
#    2   
#   /
#  1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            root = self.trimBST(root.right, L, R)
        elif root.val > R:
            root = self.trimBST(root.left, L, R)
        else:
            root.right = self.trimBST(root.right, L, R)
            root.left = self.trimBST(root.left, L, R)
        return root