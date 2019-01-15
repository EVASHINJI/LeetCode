# Url: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Related Topics:
# Tree DepthFirstSearch BreadthFirstSearch

# Example:


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depth = 1
        for c in root.children:
            depth = max(depth, self.maxDepth(c) + 1)
        return depth