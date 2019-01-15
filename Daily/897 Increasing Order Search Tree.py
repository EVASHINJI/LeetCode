# Url: https://leetcode.com/problems/increasing-order-search-tree/
# Related Topics:
# Tree DepthFirstSearch

# Example:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

#        5
#       / \
#     3    6
#    / \    \
#   2   4    8
#  /        / \ 
# 1        7   9

# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

#  1
#   \
#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6
#             \
#              7
#               \
#                8
#                 \
#                  9  


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        traversed = self.inorderTraverse(root)
        root_new = cur = TreeNode(traversed[0])
        for i in range(1, len(traversed)):
            cur.right = TreeNode(traversed[i])
            cur = cur.right
        return root_new
        
    def inorderTraverse(self, root):
        if not root:
            return []
        return self.inorderTraverse(root.left) + [root.val] + self.inorderTraverse(root.right)