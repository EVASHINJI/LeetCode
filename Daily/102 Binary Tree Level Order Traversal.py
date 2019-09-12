# Url: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Related Topics:
# Tree BreadthFirstSearch

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        bfs = [root]
        ans = [[root.val]]
        while bfs:
            new = []
            line = []
            for n in bfs:
                if n.left: 
                    new.append(n.left)
                    line.append(n.left.val)
                if n.right:
                    new.append(n.right)
                    line.append(n.right.val)
            if new:
                ans.append(line)
            bfs = new
        return ans