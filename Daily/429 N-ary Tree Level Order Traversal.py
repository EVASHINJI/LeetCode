# Url: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Related Topics:
# Tree BreadthFirstSearch

# Example:


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        line, ans = [root], []
        while line:
            next_line, cur_line_val = [], []
            for i in line:
                cur_line_val.append(i.val)
                for c in i.children:
                    next_line.append(c)
            ans.append(cur_line_val)
            line = next_line
        return ans