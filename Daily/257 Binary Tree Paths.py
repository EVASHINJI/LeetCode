# Url: https://leetcode.com/problems/binary-tree-paths/
# Related Topics:
# Tree DepthFirstSearch

# Example:
# Input:
#    1
#  /   \
# 2     3
#  \
#   5
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)
        if not paths:
            paths.append(str(root.val))
        return paths