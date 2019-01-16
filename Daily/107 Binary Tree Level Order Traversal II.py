# Url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Related Topics:
# Tree BreadthFirstSearch

# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, line = [], [root]
        while line:
            next_line, val = [], []
            for item in line:
                val.append(item.val)
                if item.left: next_line.append(item.left)
                if item.right: next_line.append(item.right)
            ans.append(val)
            line = next_line
        return ans[::-1]