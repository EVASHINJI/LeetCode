# Url: https://leetcode.com/problems/cousins-in-binary-tree/
# Related Topics:
# Tree BreadthFirstSearch

# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        bfs = [(root, None)]
        while bfs:
            new = []
            for n, _ in bfs:
                if n.left: new.append((n.left, n))
                if n.right: new.append((n.right, n))
            x_in, y_in = None, None
            for n, pa in new:
                if n.val == x: x_in = pa
                if n.val == y: y_in = pa
            if x_in and y_in and x_in != y_in:
                return True
            if x_in or y_in:
                return False
            bfs = new
        return False
                    