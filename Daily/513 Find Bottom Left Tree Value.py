# Url: https://leetcode.com/problems/find-bottom-left-tree-value/
# Related Topics:
# Tree DepthFirstSearch BreadthFirstSearch

# Example 1:
# Input:
#     2
#    / \
#   1   3
# Output: 1
# Example 2: 
# Input:
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
# Output: 7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        line = [root]
        while line:
            next_line = []
            for node in line:
                if node.left: next_line.append(node.left)
                if node.right: next_line.append(node.right)
            if not next_line:
                return line[0].val
            line = next_line