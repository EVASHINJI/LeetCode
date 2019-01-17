# Url: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Related Topics:
# Tree DepthFirstSearch BreadthFirstSearch

# Example:
# Input: 
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
# Output: [1, 3, 9]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        line = [root]
        while line:
            next_line = []
            ma = line[0].val
            for node in line:
                if node.left: next_line.append(node.left)
                if node.right: next_line.append(node.right)
                ma = max(ma, node.val)
            ans.append(ma)
            line = next_line
        return ans