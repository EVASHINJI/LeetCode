# Url: https://leetcode.com/problems/symmetric-tree/
# Related Topics:
# Tree DepthFirstSearch BreadthFirstSearch

# Example:
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        pairs = [(root.left, root.right)]
        while pairs:
            left, right = pairs.pop()
            if left and right:
                if left.val == right.val:
                    pairs.append((left.left, right.right))
                    pairs.append((left.right, right.left))
                else:
                    return False
            elif not left and not right:
                continue
            else:
                return False
        return True