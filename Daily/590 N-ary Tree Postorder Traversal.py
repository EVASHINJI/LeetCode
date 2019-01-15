# Url: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# Related Topics:
# Tree

# Example:


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        traverse = []
        for c in root.children:
            traverse += self.postorder(c)
        return traverse + [root.val]